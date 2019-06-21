from django.contrib import admin

from .models import Tamu
from .models import Kedatangan, Departemen
from pelaporan.models import Pelaporan

# Register your models here.

# admin.site.register(Tamu)
# admin.site.register(Kedatangan)
# admin.site.register(Pelaporan)
# admin.site.register(Departemen)

@admin.register(Tamu)
class TamuAdmin(admin.ModelAdmin):
	list_display = ('uid', 'tipeid', 'nama_tamu', 'no_hp_tamu', 'signed_in', 'perusahaan',
		'terakhir_datang', 'saved')


@admin.register(Kedatangan)
class KedatanganAdmin(admin.ModelAdmin):
	list_display = ('tamu', 'tanggal_kedatangan', 'bertemu_dengan','suhu_badan', 
		'terdapat_luka_terbuka', 'sakit', 'departemen',
		'alasan_kedatangan', 'tanggal_keluar', 'lama_kedatangan', )

    

@admin.register(Pelaporan)

class PelaporanAdmin(admin.ModelAdmin):
	list_display = ('nama_pelapor', 'uid_pelapor', 'tid_pelapor', 'tanggal_pelanggaran', 'tanggal_pelaporan',
		'pelaku', 'tipe_aktivitas_12', 'sub_kategori', 'positif', 'area', 'departemen', 'action_plan1',
		'action_plan2', 'keterangan')


@admin.register(Departemen)
class DepartemenAdmin(admin.ModelAdmin):
    list_display = ('nama_departemen', 'penanggungjawab', 'email')
