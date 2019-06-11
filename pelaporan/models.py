from django.db import models
import bukutamu.models as bukutamu


# Create your models here.

class pelaporan (models.Model):
	tamu = models.ForeignKey(bukutamu.Tamu, on_delete= models.CASCADE)
	pelanggaran = models.CharField(max_length=(100))
	tempat = models.CharField(max_length=(100))
	tanggal = models.DateTimeField()