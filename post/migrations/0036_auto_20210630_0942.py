# Generated by Django 3.1.2 on 2021-06-30 04:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0035_auto_20210630_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='notification',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 30, 9, 42, 30, 530372)),
        ),
    ]
