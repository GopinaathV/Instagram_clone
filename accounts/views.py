from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, HttpResponseRedirect,get_object_or_404,redirect
from . import forms
from accounts.models import *
from post.models import *
from django.db import transaction
from django.contrib.auth.models import User
from post.views import *
from django.core.files.storage import FileSystemStorage
from django.urls import resolve



class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = "signup.html"

def profile(request):
    user = request.user
    profile=Profile.objects.get(user=user)
    url_name=resolve(request.path).url_name
    print(url_name)
    if url_name=='profile':
        user_posts = Post.objects.filter(user=user)
    else:
        user_posts = profile.favorites.all()

    user_post_count = user_posts.count()
    following=Follow.objects.filter(following=user).all().count()
    follower=Follow.objects.filter(followers=user).all().count()
    context={
     'user':user,
     'profile':profile,
     'posts': user_posts,
      'user_post_count':user_post_count,
       'following':following,
        'follower':follower,
        'url_name':url_name,
    }
    template='profile.html'
    return render(request, template, context)

def profile_details(request,username):
    user=Profile.objects.get(username=username)
    post=Post.objects.filter(user=user.user)
    post_count=post.count()
    follow = Follow.objects.filter(following=user.user, followers=request.user).exists()
    following = Follow.objects.filter(following=user.user).all().count()
    follower = Follow.objects.filter(followers=user.user).all().count()
    context={
        'post_count':post_count,
        'profile':user,
        'follow':follow,
        'following':following,
        'follower':follower
    }
    template = 'profile_details.html'
    return render(request, template, context)


def edit_profile(request):
    profile=Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form =forms.EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
              username=form.cleaned_data.get('username')
              location=form.cleaned_data.get('location')
              profile_info=form.cleaned_data.get('profile_info')
              picture= form.cleaned_data.get('picture')
              phone_no=form.cleaned_data.get('phone_no')
              email=form.cleaned_data.get('email')
              gender = form.cleaned_data.get('gender')
              profile = Profile.objects.get(user=request.user)
              profile.username=username
              profile.location=location
              profile.profile_info=profile_info
              profile.picture=picture
              profile.phone_no=phone_no
              profile.email=email
              profile.gender=gender
              profile.save()
    else:
            form=forms.EditProfileForm()
    template='edit-profile.html'
    context={
        'profile':profile,
        'form':form,
    }
    return render(request, template, context)


def follow(request,username,option):
    following=get_object_or_404(User,username=username)
    f,created=Follow.objects.get_or_create(followers=request.user,following=following)
    if int(option)==0:
        f.delete()
        Stream.objects.filter(following=following,user=request.user).all().delete()
    else:
        posts=Post.objects.all().filter(user=following)
        with transaction.atomic():
            for post in posts:
             stream=Stream(post=post,user=request.user,posted_date=post.posted,following=following)
             stream.save()
    return redirect('profile_details',username)








