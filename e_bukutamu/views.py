from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import get_object_or_404, render

# Create your views here.

def home(request):
    return render(request, 'index.html')