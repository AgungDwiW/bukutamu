from django.contrib import admin

from .models import Tamu
from .models import Kedatangan


# Register your models here.

"""
class kedatangans(admin.StackedInline):
    model = Kedatangan
    extra = 3

class TamuAdmin(admin.ModelAdmin):
    inlines = [kedatangans]

admin.site.register(TamuAdmin)
"""
admin.site.register(Tamu)
admin.site.register(Kedatangan)
