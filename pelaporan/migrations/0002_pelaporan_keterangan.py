# Generated by Django 2.2 on 2019-06-14 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelaporan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelaporan',
            name='keterangan',
            field=models.CharField(default='ooo', max_length=100),
            preserve_default=False,
        ),
    ]
