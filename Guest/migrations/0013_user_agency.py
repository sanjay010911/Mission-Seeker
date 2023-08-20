# Generated by Django 4.1.5 on 2023-03-01 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_delete_admin'),
        ('Guest', '0012_remove_user_place_delete_agency_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_address', models.CharField(max_length=100)),
                ('user_mail', models.CharField(max_length=50)),
                ('user_contact', models.CharField(max_length=50)),
                ('user_photo', models.FileField(upload_to='UserDocs/')),
                ('user_pass', models.CharField(max_length=50)),
                ('key', models.BinaryField(max_length=1000, null=True)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.place')),
            ],
        ),
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
                ('key', models.BinaryField(max_length=1000, null=True)),
                ('casetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.casetype')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.place')),
            ],
        ),
    ]
