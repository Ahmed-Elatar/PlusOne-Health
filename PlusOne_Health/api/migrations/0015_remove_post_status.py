# Generated by Django 4.2.11 on 2024-06-21 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_userprofile_bio_alter_userprofile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
    ]
