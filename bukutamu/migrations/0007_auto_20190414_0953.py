# Generated by Django 2.2 on 2019-04-14 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bukutamu', '0006_kedatangan_signedout'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kedatangan',
            old_name='signedout',
            new_name='out',
        ),
    ]
