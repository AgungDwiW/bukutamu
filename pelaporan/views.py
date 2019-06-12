from django.shortcuts import render
from bukutamu.models import Kedatangan, Tamu

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
        temp['nama'] = tamu.nama_tamu
        temp['tanggal'] = kedatangan.tanggal_keluar
        temp['alasan'] = kedatangan.alasan_kedatangan
        temp['bertemu'] = kedatangan.bertemu_dengan
        temp['keperluan'] = kedatangan.alasan_kedatangan
        if (tamu.signed_in):
            temp['status'] = "Masuk"
        else:
            temp['status'] = "Keluar"
        content.append(temp)
    contents = {}
    contents['items'] = content
    #return HttpResponse(contets)
    return render(request, 'pelaporan/bukutamu.html',contents)

def index(request):
    pass
# Create your views here.
