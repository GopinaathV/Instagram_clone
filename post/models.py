from django.db import models
from django.db.models.signals import post_save, post_delete
from django.utils.text import slugify
import uuid
from django.urls import reverse
from django.contrib.auth.models import User
from accounts.models import *
from datetime import datetime, timedelta
import os
from django.conf import settings
# Create your models here.


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)
    return post_pic_name

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug= models.SlugField(max_length=50)
    
    
    def get_absolute_url(self):
       return reverse('tags',args=[self.slug])

    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        if not self.slug:
          self.slug=slugify(self.title)
        return super().save(*args,**kwargs)
        
    


class Post(models.Model):
    id= models.UUIDField(default=uuid.uuid4, editable=False,primary_key=True)
    tag = models.ManyToManyField(Tag)
    caption= models.TextField(max_length=50,null=True)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=user_directory_path,null=False,blank=False)
    posted = models.DateField(auto_now=True)



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def user_likes(sender,instance,*args,**kwargs):
        like=instance
        post=like.post
        senders=like.user
        notify=Notification(post=post,user=post.user,notification_type=1,sender=senders,text_preview='your post was liked by '+str(senders)+'!!!')
        notify.save()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=50)

    def user_comments(sender,instance,*args,**kwargs):
        comment=instance
        post=comment.post
        senders=comment.user
        notify=Notification(post=post,user=post.user,notification_type=2,sender=senders,text_preview=str(senders)+' commented on our post')
        notify.save()

class Follow(models.Model):
    followers= models.ForeignKey(User,on_delete=models.CASCADE,related_name='followers')
    following = models.ForeignKey(User,on_delete=models.CASCADE, related_name='following')

    def user_follows(sender, instance, *args, **kwargs):
        follow = instance
        senders = follow.followers
        notify = Notification( user=follow.following, notification_type=2, sender=senders,
                              text_preview=str(senders) + '  started following you')
        notify.save()




class Notification(models.Model):
    NOTIFICATION_TYPES = ((1, 'Like'), (2, 'Comment'), (3, 'Follow'))
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="noti_from_user")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="noti_to_user")
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)
    text_preview = models.CharField(max_length=90, blank=True)
    sender_pic = models.ImageField(null=True)
    is_seen = models.BooleanField(default=False)
    mydate = models.DateTimeField(default=datetime.now())


class Stream(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    following=models.ForeignKey(User,on_delete=models.CASCADE,related_name='stream_following')
    posted_date = models.DateTimeField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def addpost(sender,instance,*args,**kwargs):
        post =instance
        user=post.user
        followers=Follow.objects.all().filter(following=user)
        for follower in followers:
            stream=Stream(post=post,following=user,user=follower.followers,posted_date=post.posted)
            stream.save()

post_save.connect(Stream.addpost,sender=Post)

post_save.connect(Like.user_likes,sender=Like)

post_save.connect(Comment.user_comments,sender=Comment)

post_save.connect(Follow.user_follows,sender=Follow)










           
    
    
    
