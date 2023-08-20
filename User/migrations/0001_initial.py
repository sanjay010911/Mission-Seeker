# Generated by Django 4.1.5 on 2023-01-27 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0004_agency'),
        ('Admin', '0004_district_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_details', models.CharField(max_length=50)),
                ('request_date', models.CharField(max_length=50)),
                ('request_status', models.IntegerField(default=0)),
                ('payment_status', models.IntegerField(default=0)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.agency')),
                ('casetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.casetype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.user')),
            ],
        ),
    ]
