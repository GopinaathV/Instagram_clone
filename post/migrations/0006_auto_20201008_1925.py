# Generated by Django 3.0.7 on 2020-10-08 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20201008_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='posted_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]