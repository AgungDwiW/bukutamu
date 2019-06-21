import datetime
import os
from django.db import models
from django.utils import timezone


class Tamu(models.Model):
    uid = models.CharField(max_length = 12)
    tipeid = models.CharField(max_length = 20)
    nama_tamu = models.CharField(max_length = 100,null = True)
    no_hp_tamu = models.CharField(max_length = 30,null = True)
    jenis_kelamin = models.CharField(max_length = 20,null = True)
    signed_in = models.BooleanField(null = True)
    perusahaan = models.CharField(max_length = 100,null = True)
    terakhir_datang = models.DateTimeField('terakhir_datang',null = True)
    image = models.ImageField(upload_to= "camera/",null = True)
    uid.default = '000000000000'
    saved = models.BooleanField()
    saved.default = True
    def delete_image(self):
        path = os.path.join(os.path.join(os.getcwd(), "media"), self.image.name)
        try:
            os.remove(path)
        except:
            pass
    def checkme(self):
        returned = [self.nama_tamu, self.terakhir_datang]
        return returned
    def last(self):
        #bool terakhir datang 30 hari terakhir
        return self.terakhir_datang >= timezone.now() - datetime.timedelta(days=30)
    def dest(self):

        return True

    def __str__(self):
        if(self.nama_tamu != None):
            return self.nama_tamu
        else:
            return "-"

class Departemen(models.Model):
    nama_departemen = models.CharField(max_length = (50))
    penanggungjawab = models.CharField(max_length = (50))
    email = models.CharField(max_length = (50))

class Kedatangan(models.Model):
    tamu = models.ForeignKey(Tamu, on_delete= models.CASCADE)
    tanggal_kedatangan = models.DateTimeField("datang")
    bertemu_dengan = models.CharField(max_length=(100))
    departemen = models.ForeignKey(Departemen,models.SET_NULL,blank=True,null=True,)
    alasan_kedatangan = models.CharField(max_length = 300)
    tanggal_keluar = models.DateTimeField("keluar")
    lama_kedatangan = models.DurationField("lama")
    suhu_badan = models.DecimalField(max_digits=5, decimal_places=2)
    terdapat_luka_terbuka = models.BooleanField()
    sakit =models.CharField(max_length=(100), null = True)
    out = models.BooleanField()
    def signout (self):
        self.tanggal_keluar = timezone.now()
        self.lama_kedatangan = self.tanggal_keluar - self.tanggal_kedatangan
        self.out = True

    def checkme(self):
        returned = [self.tamu, self.alasan_kedatangan, self.tanggal_kedatangan]
        return returned