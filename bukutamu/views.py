from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import get_object_or_404, render

from django.http import Http404
from .models import Tamu, Kedatangan
from django.utils import timezone
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'bukutamu/index.html')

def signin(request):
	try:
		tamu = Tamu.objects.get(uid = request.POST['UID'])
	except (KeyError, Tamu.DoesNotExist):
		#if not exist create new
		tamu = Tamu(
			uid = request.POST['UID'],
			tipeid = request.POST['TID'],
			nama_tamu = request.POST['Nama'],
			no_hp_tamu = request.POST['NoHP'],
			jenis_kelamin = request.POST['Kelamin'],
			perusahaan = request.POST['Institusi'],
			terakhir_datang = timezone.now()
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
	return HttpResponseRedirect(reverse('bukutamu:out'))

def out (request):
    return render(request, 'bukutamu/out.html')

def signout(request):
	try:
		tamu = Tamu.objects.get(uid = request.POST['UID'])
	except (KeyError, Tamu.DoesNotExist):
		#tamu not found
		return HttpResponseRedirect(reverse('bukutamu:out'))
	tamu.terakhir_datang = timezone.now()
	try :
		kedatangan = tamu.kedatangan_set.get(out = False)
	except (KeyError, Tamu.DoesNotExist):
		#havent login
		return HttpResponseRedirect(reverse('bukutamu:out'))
	kedatangan.tanggal_keluar = timezone.now()
	kedatangan.lama_kedatangan = kedatangan.tanggal_keluar - kedatangan.tanggal_kedatangan
	kedatangan.out = True
	kedatangan.save()
	return HttpResponseRedirect(reverse('bukutamu:index'))
	return HttpResponseRedirect(reverse('bukutamu:index'))
