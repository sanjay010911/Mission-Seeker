# Generated by Django 4.1.5 on 2023-01-27 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_district_place'),
        ('Guest', '0004_agency'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Request',
            new_name='Req',
        ),
    ]