from django.db import models
from bukutamu.models import Tamu


# Create your models here.

class Pelaporan (models.Model):
	nama_pelapor = models.CharField(max_length=(100))
	uid_pelapor = models.CharField(max_length=(100))
	tid_pelapor = models.CharField(max_length=(100))
	tanggal_pelanggaran = models.DateTimeField()
	tanggal_pelaporan = models.DateTimeField()
	pelaku = models.ForeignKey(Tamu, on_delete = models.CASCADE)
	tipe_aktivitas_12 = models.CharField(max_length=(100))
	sub_kategori =  models.CharField(max_length=(100))
	positif = models.BooleanField()
	action_plan1 = models.CharField(max_length=(100))
	action_plan2 = models.CharField(max_length=(100))
	keterangan = models.CharField(max_length=(100))