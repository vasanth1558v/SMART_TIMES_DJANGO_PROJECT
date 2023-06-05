# Generated by Django 4.2 on 2023-05-13 11:32

import My_application.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_application', '0003_remove_done_mail'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('vender', models.CharField(max_length=500)),
                ('product_img', models.ImageField(blank=True, null=True, upload_to=My_application.models.getfilename)),
                ('quantity', models.IntegerField()),
                ('original_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('discription', models.CharField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0-show,1-Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0-defalt,1-trending')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='done',
        ),
    ]
