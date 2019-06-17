from django.contrib import admin

from .models import Tamu
from .models import Kedatangan
from pelaporan.models import Pelaporan

# Register your models here.

admin.site.register(Tamu)
admin.site.register(Kedatangan)
admin.site.register(Pelaporan)

