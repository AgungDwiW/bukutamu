# Generated by Django 2.2.2 on 2019-06-21 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bukutamu', '0002_auto_20190621_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
            ],
        ),
    ]
