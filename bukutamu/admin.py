from django.contrib import admin

from .models import Tamu
from .models import Kedatangan, Departemen
from pelaporan.models import Pelaporan

# Register your models here.

admin.site.register(Tamu)
admin.site.register(Kedatangan)
admin.site.register(Pelaporan)
admin.site.register(Departemen)

