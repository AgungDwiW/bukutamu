# Generated by Django 2.2 on 2019-04-14 09:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bukutamu', '0004_auto_20190414_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='tamu',
            name='terakhir_datang',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 14, 9, 39, 36, 216873, tzinfo=utc), verbose_name='terakhir_datang'),
            preserve_default=False,
        ),
    ]
