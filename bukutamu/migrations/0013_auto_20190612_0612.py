# Generated by Django 2.2 on 2019-06-12 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bukutamu', '0012_auto_20190612_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tamu',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
