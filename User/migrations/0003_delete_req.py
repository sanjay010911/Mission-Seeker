# Generated by Django 4.1.5 on 2023-01-28 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_rename_request_req'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Req',
        ),
    ]