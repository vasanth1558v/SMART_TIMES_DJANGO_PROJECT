# Generated by Django 4.2 on 2023-05-08 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('My_application', '0002_alter_done_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='done',
            name='Mail',
        ),
    ]
