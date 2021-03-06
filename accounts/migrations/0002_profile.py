# Generated by Django 3.0.7 on 2020-10-08 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_info', models.TextField(blank=True, max_length=150, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Picture')),
            ],
        ),
    ]
