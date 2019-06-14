from django.shortcuts import render
from bukutamu.models import Kedatangan, Tamu
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.http import JsonResponse
from .models import Pelaporan
from bukutamu.models import Tamu
from django.utils import timezone
import json
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
        pk = int(pk)
        tamu = Tamu.objects.get(uid=pk)
    except :
        raise Http404()
    context = {}
    context['tamu'] = tamu
    kedatangans = Kedatangan.objects.filter(tamu_id = tamu.id)
    kedatangans = kedatangans.order_by('-id')
    kedatangans = list(kedatangans)
    kedatangans = kedatangans[:-3]
    context['kedatangan'] = kedatangans
    return HttpResponse(context)
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
        temp['tipeid'] = tamu.tipeid
        temp['institusi'] = tamu.perusahaan
        temp['hp'] = tamu.no_hp_tamu
        items.append(temp)
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
    return JsonResponse(respons)

@login_required
def submit(request):
    tamu = Tamu.objects.get(uid = request.POST['uid_pelaku'])

    tamu.pelaporan_set.create(
        nama_pelapor = request.POST['nama_pelapor'],
        uid_pelapor = request.POST['uid_pelapor'],
        tid_pelapor = request.POST['tid_pelapor'],
        tanggal_pelanggaran = request.POST['tgl_langgar'],
        tanggal_pelaporan = timezone.now(),
        tipe_aktivitas_12 = request.POST['aktivitas_12'],
        sub_kategori = request.POST['Subkategori'],
        positif =request.POST['positivity'],
        action_plan1 = request.POST['AP1'],
        action_plan2 = request.POST['AP2'],
        keterangan = request.POST['keterangan'],
    )
    return HttpResponseRedirect(reverse('pelaporan:listlapor'))

@login_required
def list_pelaporan(request):
    pelaporans = Pelaporan.objects.all()
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

