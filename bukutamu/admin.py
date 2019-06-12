from django.contrib import admin

from .models import Tamu
from .models import Kedatangan


# Register your models here.


class kedatangan(admin.StackedInline):
    model = Kedatangan
    extra = 1

class TamuAdmin(admin.ModelAdmin):
    inlines = [kedatangan]

admin.site.register(TamuAdmin)