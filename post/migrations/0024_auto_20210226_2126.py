# Generated by Django 2.2 on 2021-02-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0023_auto_20210226_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='sender_pic',
            field=models.URLField(blank=True, null=True),
        ),
    ]
