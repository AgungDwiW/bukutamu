from django.shortcuts import render
from bukutamu.models import Kedatangan, Tamu

def index(request):
    kedatangans = Kedatangan.objects.all()
    content = []
    counter = 1
    for kedatangan in kedatangans:
        tamu = Tamu.objects.get(id = kedatangan.tamu_id)
        temp = {}
        temp['no'] = counter
        counter += 1
        temp['kedatagan'] = kedatangan
        temp['tamu'] = tamu
        content.append(temp)
    contents = {}
    contents['items'] = content
    return render(request, 'pelaporan/test.html',contents)

# Create your views here.
