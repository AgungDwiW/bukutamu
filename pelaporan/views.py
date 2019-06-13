from django.shortcuts import render
from bukutamu.models import Kedatangan, Tamu
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

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
    return render(request, 'pelaporan/pelaporan.html')
# Create your views here.
