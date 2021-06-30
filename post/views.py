from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from accounts.forms import NewPostForm
from accounts.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.functions import Cast, Coalesce
# Create your views here.


def search(request):

    try:
        q = request.GET.get('q')
    except:
        q = None

    if q:
        profiles= Profile.objects.filter(username__icontains=q).exclude(username__icontains=request.user.username)
        followers=Follow.objects.filter(followers=request.user).all()
        follow=[]
        for follower in followers:
            follow.append(follower.following.username)
        context = {'query': q, 'profiles': profiles,'follow':follow,}
        template = 'results.html'
    else:
        template = 'feed.html'
        context = {

        }
    return render(request, template, context)





def new_post(request):
    user=request.user
    tagsobj=[]
    if user.is_authenticated:
        if request.method=='POST':
            form = NewPostForm(request.POST, request.FILES)
            if form.is_valid():
                picture = form.cleaned_data.get('picture')
                caption = form.cleaned_data.get('caption')
                tags_form = form.cleaned_data.get('tags')

                tags_list = list(tags_form.split(','))

                for tag in tags_list:
                    t,created=Tag.objects.get_or_create(title=tag)
                    tagsobj.append(t)
                post=Post.objects.create(user=user,picture=picture,caption=caption)
                post.tag.set(tagsobj)
                post.save()
                return redirect('/profile')
        else:
            form = NewPostForm()

        context = {
            'form': form,
        }
        template='new_post.html'
        return render(request,template,context)

def index(request):
    count = count_notification(request)
    counts=True
    user=request.user
    posts=Stream.objects.filter(user=user)
    likes=Like.objects.filter(user=user)
    saves=Profile.objects.get(user=user)
    liked =[]
    saved=[]
    for like in likes:
        liked.append(like.post)


    group=[]
    for post in posts:
        group.append(post.post_id)
    postitems=Post.objects.filter(id__in=group).all()

    for postitem in postitems:
        post=Post.objects.get(id=postitem.id)
        if saves.favorites.filter(id=postitem.id).exists():
            saved.append(postitem)


        post.save()

    if count==0:
        counts=False

    context={
      'liked':liked,
       'saved':saved,
    'postitems':postitems,
    'count': count,
    'counts':counts,
    }
    template="feed.html"
    return render(request,template,context)

def post_details(request,post_id):

    post = Post.objects.get(id=post_id)
    comments=Comment.objects.filter(post=post)
    context={
        'post':post,
        'comments':comments,
    }
    template="image-detail.html"
    return render(request,template,context)






def tags(request,tag_slug):
    tags=get_object_or_404(Tag,slug=tag_slug)
    posts=Post.objects.filter(tag=tags).order_by('-posted')


    context={
       'tags':tags,
      "posts":posts
    }
    template='tags.html'
    return render(request,template,context)


def likes(request,post_id):
    user=request.user
    post = Post.objects.get(id=post_id)
    current_likes=post.likes
    liked=Like.objects.filter(user=user,post=post)
    if not liked:
        Like.objects.create(user=user,post=post)
        current_likes=current_likes+1
    else:
        Like.objects.filter(user=user, post=post).delete()
        current_likes=current_likes-1
    post.likes=current_likes
    post.save()

    return redirect('/post')

def comments(request,post_id):
    user=request.user
    post=Post.objects.get(id=post_id)
    commented=Comment.objects.filter(user=user,post=post)
    if not commented:
       if request.method=='POST':
           indiv_comment=Comment(user=user,post=post,)
           indiv_comment.comment=request.POST.get('comment')
           indiv_comment.save()
    return redirect('post_details',post_id)


def display_notification(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-mydate')
    Notification.objects.filter(user=user, is_seen=False).update(is_seen=True)
    counts=True
    count =notifications.count()
    if count==0:
        counts=False

    context = {
        'counts':count,
        'notifications':notifications,
    }
    template = 'explore.html'
    return render(request, template, context)

def count_notification(request):
    count = Notification.objects.filter(user=request.user).all().count()

    return count







def save_post(request,post_id):
    user=request.user
    post=Post.objects.get(id=post_id)
    profile_save=Profile.objects.get(user=user)

    if profile_save.favorites.filter(id=post_id).exists():
        profile_save.favorites.remove(post)
    else:
        profile_save.favorites.add(post)

    return redirect('/post')
















