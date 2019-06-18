# Generated by Django 2.2.2 on 2019-06-18 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bukutamu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelaporan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pelapor', models.CharField(max_length=100)),
                ('uid_pelapor', models.CharField(max_length=100)),
                ('tid_pelapor', models.CharField(max_length=100)),
                ('tanggal_pelanggaran', models.DateTimeField()),
                ('tanggal_pelaporan', models.DateTimeField()),
                ('tipe_aktivitas_12', models.CharField(max_length=100)),
                ('sub_kategori', models.CharField(max_length=100)),
                ('positif', models.BooleanField()),
                ('area', models.IntegerField()),
                ('action_plan1', models.CharField(max_length=100)),
                ('action_plan2', models.CharField(max_length=100)),
                ('keterangan', models.CharField(max_length=100)),
                ('departemen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bukutamu.Departemen')),
                ('pelaku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bukutamu.Tamu')),
            ],
        ),
    ]
