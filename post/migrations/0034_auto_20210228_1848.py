# Generated by Django 2.2 on 2021-02-28 13:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0033_auto_20210228_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 28, 18, 48, 52, 312184)),
        ),
    ]
