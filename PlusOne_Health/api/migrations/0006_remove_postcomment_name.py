# Generated by Django 4.2.11 on 2024-06-19 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_postcomment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcomment',
            name='name',
        ),
    ]