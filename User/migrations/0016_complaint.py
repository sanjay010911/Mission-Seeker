# Generated by Django 4.1.5 on 2023-02-04 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0006_agency'),
        ('User', '0015_delete_complaint'),
    ]

    operations = [
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
