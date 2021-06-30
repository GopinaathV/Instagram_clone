from django.contrib import auth
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from post.models import Post
import os
from django.conf import settings
GENDER_CHOICES = (
    ("M", "male"),
    ("F", "female"),
    ("S", "shemale")
)
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    profile_pic_name = 'user_{0}/profile.jpg'.format(instance.user.id)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

    if os.path.exists(full_path):
    	os.remove(full_path)

    return profile_pic_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=50)
    location=models.CharField(max_length=50, null=True, blank=True)
    profile_info = models.TextField(max_length=150, null=True, blank=True)
    picture = models.ImageField(upload_to=user_directory_path,blank=True, null=True, verbose_name='Picture')
    phone_no =models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField()
    gender= models.CharField(choices=GENDER_CHOICES,max_length=10,default='M')
    favorites = models.ManyToManyField(Post)


    def __str__(self):
        return self.user.username



def createprofile(sender,created,instance,**kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(createprofile,sender=User)








