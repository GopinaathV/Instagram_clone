# Generated by Django 2.2 on 2021-02-26 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0024_auto_20210226_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='sender_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
