# Generated by Django 3.0.7 on 2020-10-21 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_profile_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='userspic/%Y/%m/%d/', verbose_name='Picture'),
        ),
    ]