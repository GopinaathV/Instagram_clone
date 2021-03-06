# Generated by Django 3.0.7 on 2020-10-09 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201008_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'male'), ('F', 'female'), ('S', 'shemale')], default='M', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
