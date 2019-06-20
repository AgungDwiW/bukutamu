from django.shortcuts import render
from bukutamu.models import Kedatangan, Tamu, Departemen
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.http import JsonResponse
from .models import Pelaporan
from django.utils import timezone
import json
from time import strftime
from django.db.models import Q
import math
from django.conf import settings
from django.core.mail import send_mail


@login_required
def bukutamu(request):
    kedatangans = Kedatangan.objects.all()
    content = []
    counter = 1
    kedatangans = kedatangans.order_by('-id')
    for kedatangan in kedatangans:
        tamu = Tamu.objects.get(id = kedatangan.tamu_id)
        temp = {}
        temp['no'] = counter
        counter += 1
        temp['id'] = tamu.id
        temp['nama'] = tamu.nama_tamu
        temp['tanggal'] = kedatangan.tanggal_keluar
        temp['alasan'] = kedatangan.alasan_kedatangan
        temp['bertemu'] = kedatangan.bertemu_dengan
        temp['keperluan'] = kedatangan.alasan_kedatangan
        temp['uid'] = tamu.uid
        if (kedatangan.tanggal_keluar == kedatangan.tanggal_kedatangan):
            temp['status'] = "Didalam"
        else:
            temp['status'] = "Keluar"
        content.append(temp)
    contents = {}
    contents['items'] = content
    #return HttpResponse(contets)
    return render(request, 'pelaporan/bukutamu.html',contents)

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('pelaporan:bukutamu'))
    return render(request,'pelaporan/index.html') 
    
@login_required
def users(request):
    tamus = Tamu.objects.all()
    context = {}
    content = []
    counter = 1
    for tamu in tamus:
        temp = {}
        temp['no'] = counter
        counter+=1
        temp['nama'] = tamu.nama_tamu
        temp['tanggal'] = tamu.terakhir_datang
        temp['uid'] = tamu.uid
        temp['kelamin'] = tamu.jenis_kelamin
        temp['hp'] = tamu.no_hp_tamu
        temp['status'] = "Didalam" if tamu.signed_in else "Keluar"
        temp['perusahaan'] = tamu.perusahaan
        temp['tipeid'] = tamu.tipeid
        content.append(temp)
    context ['items'] = content

    return render(request,'pelaporan/users.html', context) 


@login_required
def users_detail(request, pk):
    try:
        tamu = Tamu.objects.get(uid=pk)
    except :
        raise Http404()
    context = {}
    context['tamu'] = tamu
    context['kedatangan'] = tamu.kedatangan_set.all()
    context['pelanggaran'] = tamu.pelaporan_set.all()
    counter_bulan = [0 for a in range(12)]
    bulan = [0 for a in range(12)]
    bulan_pel = [0 for a in range(12)]
    for item in context['kedatangan']:
        bulan_cur = item.tanggal_kedatangan.strftime("%m")
        bulan_cur = int(bulan_cur)
        counter_bulan[bulan_cur]+=1
        kedatangan = item.lama_kedatangan
        kedatangan = kedatangan.seconds + (kedatangan.days * 24*3600)
        kedatangan2 = kedatangan/3600
        kedatangan2 = math.floor(kedatangan2)
        if (kedatangan%3600 > (40*60)):
            kedatangan2+=1
        bulan[bulan_cur]+=kedatangan2
        lama = item.lama_kedatangan
        if kedatangan == 0:
            continue
    context['bulan_jam'] = bulan
    context['bulan'] = counter_bulan
    for item in context['pelanggaran']:
        bulan_cur = item.tanggal_pelanggaran.strftime("%m")
        bulan_cur = int(bulan_cur)
        bulan_pel[bulan_cur]+=1
    context ['bulan_pel']= bulan_pel

    return render(request,'pelaporan/users_detail.html', context) 

@login_required
def lapor(request):
    context = {}
    items = []
    tamus = Tamu.objects.all()
    for tamu in tamus:
        temp =  {}
        temp['nama'] = tamu.nama_tamu
        temp['uid'] = tamu.uid
    context['items'] =  tamus
    context['json'] = json.dumps(items)
    return render(request, 'pelaporan/pelaporan.html', context)
# Create your views here.

@login_required
def get_tamu(request, uid):
    tamu = Tamu.objects.get(uid=uid)
    respons = {}
    respons['nama'] = tamu.nama_tamu
    respons['hp'] = tamu.no_hp_tamu
    respons['perusahaan'] = tamu.perusahaan
    respons['tipeid'] = tamu.tipeid
    kedatangans = tamu.kedatangan_set.all()
    kedatangans = kedatangans.order_by('-id')
    kedatangans = list(kedatangans)
    kedatangans = kedatangans[:4]
    temp2 = {}
    for kedatangan in kedatangans:
        temp2[kedatangan.id] = kedatangan.tanggal_kedatangan.strftime("%d/%m/%Y %H:%M")
    respons['kedatangan'] = temp2
    return JsonResponse(respons)

@login_required
def get_pelanggaran(request, uid, tipe12, sub):
    dic = {'status':False}
    # try:
    #     tamu = Tamu.objects.get(uid = uid)
    # except:
    #     return JsonResponse(dic)
    tamu = Tamu.objects.get(uid = uid)
    tipe12 = tipe12.replace("_"," ")
    sub= sub.replace("_"," ")
    pelanggaran = tamu.pelaporan_set.filter(tipe_aktivitas_12 = tipe12, sub_kategori = sub)
    context = {}
    lists =[]
    for item in pelanggaran:
        temp = {}
        temp['ap1'] = ""
        temp['ap2'] = ""
        temp['tanggal'] = item.tanggal_pelanggaran.strftime("%d/%m/%Y")
        temp['area'] = item.area
        temp['departemen'] = item.departemen.nama_departemen
        if (item.action_plan1!= ""):
            temp['ap1'] = item.action_plan1
        if (item.action_plan2 != ""):
            temp['ap2'] = item.action_plan2
        lists.append(temp)
    context['pelanggaran'] = lists
    return JsonResponse(context)
    # except:
    #     return JsonResponse(dic)



@login_required
def submit(request):
    try:
        tamu = Tamu.objects.get(uid = request.POST['uid_pelaku'])
    except:
        return HttpResponseRedirect(reverse('pelaporan:listlapor'))
    temp = Kedatangan.objects.get(id = request.POST["tgl_langgar"])
    temp = temp.departemen
    ap1 =  request.POST['AP1'] 
    ap2 =  request.POST['AP2'] 
    tamu.pelaporan_set.create(
        nama_pelapor = request.POST['nama_pelapor'],
        uid_pelapor = request.POST['uid_pelapor'],
        tid_pelapor = request.POST['tid_pelapor'],
        tanggal_pelanggaran = Kedatangan.objects.get(id = request.POST['tgl_langgar']).tanggal_kedatangan,
        tanggal_pelaporan = timezone.now(),
        tipe_aktivitas_12 = request.POST['aktivitas_12'],
        sub_kategori = request.POST['Subkategori'],
        positif =request.POST['positivity'],
        action_plan1 = ap1,
        action_plan2 = ap2,
        keterangan = request.POST['keterangan'],
        departemen = temp,
        area = int(request.POST['area']),
    )
    if (tamu.pelaporan_set.count()>=3):
        email_to = [temp.email]
        email_from=settings.EMAIL_HOST_USER
        subject = "pelanggaran melebihi baatas oleh:" + tamu.nama_tamu
        message = "detail tamu:<br> Nama"+tamu.nama_tamu+"<br>"+"institusi tamu :"+tamu.perusahaan
        send_mail(subject, message, settings.EMAIL_HOST_USER,
            email_to, fail_silently=True)
        

    return HttpResponseRedirect(reverse('pelaporan:listlapor'))

@login_required
def list_pelaporan(request):
    pelaporans = Pelaporan.objects.all()
    pelaporans = pelaporans.order_by('-id')
    context = {}
    content = []
    counter = 1
    for pelaporan in pelaporans:
        temp = {}
        tamu = Tamu.objects.get(id = pelaporan.pelaku_id)
        temp['no'] = counter
        counter+=1
        temp['nama_pelapor'] = pelaporan.nama_pelapor
        temp['tanggal'] = pelaporan.tanggal_pelanggaran.date()
        temp['uid_pelaku'] = tamu.uid
        temp['nama_pelaku'] = tamu.nama_tamu
        temp['12'] = pelaporan.tipe_aktivitas_12
        temp['subkategori'] = pelaporan.sub_kategori
        temp['positivity'] = "positif" if pelaporan.positif  else "negative"
        temp['ap1'] = pelaporan.action_plan1
        temp['ap2'] = pelaporan.action_plan2
        temp['keterangan'] = pelaporan.keterangan
        content.append(temp)
    context ['items'] = content

    return render(request,'pelaporan/listpelaporan.html', context) 

@login_required
def dashboard(request):
    kedatangans = Kedatangan.objects.all()
    bulan =[0 for a in range(12)]
    for kedatangan in kedatangans:
        cur_month = kedatangan.tanggal_kedatangan.strftime('%m')
        cur_month = int(cur_month)
        bulan[cur_month]+=1
    tamus = Tamu.objects.all()
    perusahaan = {}
    for tamu in tamus:
        if tamu.perusahaan in perusahaan:
            perusahaan[tamu.perusahaan]+=1
        else:
            perusahaan[tamu.perusahaan] = 1
    bulan_pel = [0 for a in range (12)]
    area_pel = [0 for a in range(5)]
    departemen_pel = {}
    pelanggarans = Pelaporan.objects.all()
    departemens = Departemen.objects.all()
    # test = []
    perusahaan_pel = {}
    for departemen in departemens:
        departemen_pel[departemen.nama_departemen] = len(departemen.pelaporan_set.all())
    for pelaporan in pelanggarans:
        tamu = pelaporan.pelaku
        a = tamu.perusahaan 
        if tamu.perusahaan in perusahaan_pel:
            perusahaan_pel[tamu.perusahaan]+=1
        else:
            perusahaan_pel[tamu.perusahaan] = 1
        cur_month = pelaporan.tanggal_pelanggaran.strftime('%m')
        cur_month = int(cur_month)
        bulan_pel[cur_month]+=1
        area_pel [pelaporan.area-1] +=1            
        # test.append(pelaporan.area)
    
    context = [perusahaan, bulan]
    context = {'perusahaan' : perusahaan, 'perusahaan_pel':perusahaan_pel, 'bulan' : bulan, 'bulan_pel' : bulan_pel, 'area' : area_pel, 'departemen_pel':departemen_pel}
    # return JsonResponse(context)    
    return render(request, 'pelaporan/dashboard.html', context)

def test(request):
    return render(request, 'pelaporan/test.html')