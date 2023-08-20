# Generated by Django 4.1.5 on 2023-02-11 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0006_agency'),
        ('Admin', '0004_district_place'),
        ('User', '0017_remove_feedback_user_remove_req_agency_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Req',
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
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_details', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.user')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_title', models.CharField(max_length=50)),
                ('complaint_details', models.CharField(max_length=100)),
                ('complaint_status', models.IntegerField(default=0)),
                ('complaint_reply', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.user')),
            ],
        ),
    ]
