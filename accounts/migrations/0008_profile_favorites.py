# Generated by Django 3.0.7 on 2020-10-12 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_comment'),
        ('accounts', '0007_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(to='post.Post'),
        ),
    ]
