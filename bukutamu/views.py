from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import get_object_or_404, render

from django.http import Http404
from .models import Tamu, Kedatangan
from django.utils import timezone
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'bukutamu/index.html')


def form (request):
    formdata = {}
    formdata ["UID"] = request.POST['UID']
    
    try:
        # searching existing tamu's data
        tamu = Tamu.objects.get(uid = request.POST['UID'])
        if (tamu.signed_in == True):
            tamu.signed_in = False
            tamu.save()
            kedatangan = tamu.kedatangan_set.get(out = False)
            kedatangan.signout()
            kedatangan.save()
            return HttpResponseRedirect(reverse('bukutamu:index'))

        formdata["flag"] = True
        
        formdata['tamu'] = tamu

    except (KeyError, Tamu.DoesNotExist):
        formdata["flag"] = False
    return render(request, "bukutamu/test.html", formdata)


def signin(request):
    try:
        tamu = Tamu.objects.get(uid = request.POST['UID'])
        tamu.signed_in = True
        tamu.image = request.POST['Image']
        tamu.save()
    except (KeyError, Tamu.DoesNotExist):
        #if not exist create new
        tamu = Tamu(
            uid = request.POST['UID'],
            tipeid = request.POST['TID'],
            nama_tamu = request.POST['Nama'],
            no_hp_tamu = request.POST['NoHP'],
            jenis_kelamin = request.POST['Kelamin'],
            perusahaan = request.POST['Institusi'],
            terakhir_datang = timezone.now(),
            image = request.POST['Image']
            )
        tamu.save()
    
    if request.POST['Luka'] == 'True':
        luka = True
    else:
        luka = False

    suhu = request.POST['SuhuBadan']
    suhu = suhu.replace(',','.')
    suhu = float(suhu)

    tamu.kedatangan_set.create(
        tanggal_kedatangan = timezone.now(),
        bertemu_dengan = request.POST['Bertemu'],
        alasan_kedatangan = request.POST['Keperluan'],
        tanggal_keluar = timezone.now(),
        lama_kedatangan = timezone.now() - timezone.now(),
        suhu_badan = suhu,
        terdapat_luka_terbuka = luka,
        out = False
        )
    return HttpResponseRedirect(reverse('bukutamu:index'))

def test(request):
    return render(request, 'bukutamu/test.html')

def formtest(request):
    return HttpResponse(request.POST)