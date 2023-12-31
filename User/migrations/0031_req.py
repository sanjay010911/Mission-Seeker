# Generated by Django 4.1.5 on 2023-04-18 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_delete_admin'),
        ('Guest', '0015_user_agency'),
        ('User', '0030_delete_req'),
    ]

    operations = [
        migrations.CreateModel(
            name='Req',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_details', models.CharField(max_length=50)),
                ('request_date', models.CharField(max_length=50)),
                ('request_status', models.IntegerField(default=0)),
                ('report', models.FileField(default=0, upload_to='AgencyDocs/')),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.agency')),
                ('casetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.casetype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.user')),
            ],
        ),
    ]
