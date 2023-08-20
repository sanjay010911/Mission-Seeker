# Generated by Django 4.1.5 on 2023-02-03 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_district_place'),
        ('Guest', '0005_delete_agency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_name', models.CharField(max_length=50)),
                ('agency_address', models.CharField(max_length=200)),
                ('agency_mail', models.CharField(max_length=100)),
                ('agency_pass', models.CharField(max_length=50)),
                ('agency_proof', models.FileField(upload_to='AgencyDocs/')),
                ('agency_photo', models.FileField(upload_to='AgencyDocs/')),
                ('agency_contact', models.CharField(max_length=50)),
                ('agency_vstatus', models.IntegerField(default=0)),
                ('casetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.casetype')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.place')),
            ],
        ),
    ]
