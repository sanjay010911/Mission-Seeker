# Generated by Django 4.1.5 on 2023-02-11 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0019_remove_feedback_user_remove_req_agency_and_more'),
        ('Guest', '0006_agency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='place',
        ),
        migrations.DeleteModel(
            name='Agency',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]