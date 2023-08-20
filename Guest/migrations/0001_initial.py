# Generated by Django 4.1.5 on 2023-01-20 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0004_district_place'),
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
                ('place_name', models.CharField(max_length=50)),
                ('user_pass', models.CharField(max_length=50)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.district')),
            ],
        ),
    ]
