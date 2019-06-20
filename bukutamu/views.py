from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import get_object_or_404, render
from base64 import b64decode
from django.core.files.base import ContentFile
from django.http import Http404
from .models import Tamu, Kedatangan, Departemen
from django.utils import timezone
from django.urls import reverse
import re
import os
from django.http import JsonResponse
# Create your views here.

def index(request):
    
    return render(request, 'bukutamu/index.html')

def b64toMime(b64_text):
    image_data = b64decode(b64_text)
    return image_data

def form (request):
    formdata = {}
    formdata ["uid"] = request.POST['UID']
    formdata['flag_auth'] ="true"
    try:
        # searching existing tamu's data
        tamu = Tamu.objects.get(uid = request.POST['UID'])
        if (tamu.jenis_kelamin == "Perempuan"):
            formdata["kelamin"] = True
        if (tamu.tipeid == "SIM"):
            formdata["tipid"] = True
        
        formdata["flag"] = True
        if (tamu.signed_in == True):
            formdata["flag"] = False
            kedatangan = tamu.kedatangan_set.get(out = False)
            a = kedatangan.departemen
            departemens = [a]
            formdata["kedatangan"]= kedatangan
            formdata['sakit'] = len(kedatangan.sakit) != 0
        else:
            departemens = Departemen.objects.all()
        formdata['departemen'] = departemens
        formdata['tamu'] = tamu
        # return JsonResponse()
        pelanggaran = tamu.pelaporan_set.count()
        formdata['flag_auth'] ="true"
        if (formdata['flag'] and pelanggaran >= 3):
            formdata['flag_auth'] ="false"
        kedatangan_dulu = tamu.kedatangan_set.all()
        kedatangan_dulu = kedatangan_dulu.order_by('-id')
        kedatangan_dulu = list(kedatangan_dulu)
        if len(kedatangan_dulu)>3:
            kedatangan_dulu= kedatangan_dulu[:3]
            a = kedatangan_dulu[2]
            kedatangan_dulu[2] = kedatangan_dulu[0]
            kedatangan_dulu[0]=a
        for item in kedatangan_dulu:
            item.tanggal_keluar = item.tanggal_keluar.date()

        formdata["history"] = kedatangan_dulu
        # tamu.image = tamu.image.url
        # tamu.image = tamu.image.split("/")
        # tamu.image = tamu.image[len(tamu.image)-1]

    except (KeyError, Tamu.DoesNotExist):
        departemens = Departemen.objects.all()
        formdata['departemen'] = departemens
        formdata["flag"] = True

    return render(request, "bukutamu/form.html", formdata)


def signin(request):
    image = request.POST['Image']
    image = b64decode(image)
    image = ContentFile(image, request.POST['UID'])

    try:
        tamu = Tamu.objects.get(uid = request.POST['UID'])
        tamu.signed_in = True
        tamu.delete_image()
        tamu.image = image
        tamu.save()
        pelanggaran = tamu.pelaporan_set.filter(positif = False).count()
        
        if (pelanggaran >= 3):
            tamu.signed_in = False
            tamu.save()
            return HttpResponseRedirect(reverse('bukutamu:index'))

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
            signed_in = True,
            )
        tamu.image = image
        tamu.save()
    a = timezone.now()
    tamu.kedatangan_set.create(
        tanggal_kedatangan = a,
        bertemu_dengan = request.POST['Bertemu'],
        alasan_kedatangan = request.POST['Keperluan'],
        tanggal_keluar = a,
        lama_kedatangan = a - a,
        suhu_badan = request.POST['Suhu'],
        terdapat_luka_terbuka = request.POST['Luka'],
        out = False,
        sakit = request.POST['Sakit'],
        departemen = Departemen.objects.get(id = request.POST['departemen'])
        )
    return HttpResponseRedirect(reverse('bukutamu:index'))

def signout(request):
    tamu = Tamu.objects.get(uid = request.POST['UID'])
    tamu.signed_in = False
    tamu.save()
    kedatangan = tamu.kedatangan_set.get(out = False)
    kedatangan.signout()
    kedatangan.save()
    return HttpResponseRedirect(reverse('bukutamu:index'))

def test(request):
    return render(request, 'bukutamu/test.html')

def laporan(request):
    return render(request, 'bukutamu/laporan.html')