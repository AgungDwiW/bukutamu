from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import get_object_or_404, render
from base64 import b64decode
from django.core.files.base import ContentFile
from django.http import Http404
from .models import Tamu, Kedatangan
from django.utils import timezone
from django.urls import reverse
import re


# Create your views here.

def index(request):
    return render(request, 'bukutamu/index.html')

def b64toMime(b64_text):
    image_data = b64decode(b64_text)
    image = ContentFile(image_data, 'whatup.png')
    return image

def form (request):
    formdata = {}
    formdata ["uid"] = request.POST['UID']
    
    try:
        # searching existing tamu's data
        tamu = Tamu.objects.get(uid = request.POST['UID'])
        if (tamu.signed_in == True):
            tamu.signed_in = False
            
            return render(request, "bukutamu/form.html", formdata)

        formdata["flag"] = True
        
        formdata['tamu'] = tamu

    except (KeyError, Tamu.DoesNotExist):
        formdata["flag"] = False
    return render(request, "bukutamu/form.html", formdata)


def signin(request):
    image = request.POST['Image']
    image = b64decode(image)
    image = ContentFile(image, request.POST['UID'])
    try:
        tamu = Tamu.objects.get(uid = request.POST['UID'])
        tamu.signed_in = True
        tamu.image = image
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
            image = None,
            signed_in = True
            )
        tamu.image = image
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

def signout(request):s
    tamu = Tamu.objects.get(uid = request.POST['UID'])
    tamu.save()
    kedatangan = tamu.kedatangan_set.get(out = False)
    kedatangan.signout()
    kedatangan.save()
    
    
def test(request):
    return render(request, 'bukutamu/test.html')

def formtest(request):
    pass