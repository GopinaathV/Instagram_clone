"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from accounts.views import profile,edit_profile,profile_details,follow
from post.views import *
from .views import TestPage
urlpatterns = [

    url(r"^admin/", admin.site.urls),
    url(r"^$", TestPage.as_view(), name="test"),
    url(r'^s/$', search, name='search'),
    url(r"^accounts/", include("accounts.urls", namespace="accounts")),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^inbox/", include("chat.urls", namespace="chat")),
    url(r"^post/", include("post.urls")),
    url("tags/(?P<tag_slug>.*)/", tags, name="tags"),
    url("comments/(?P<post_id>.*)/", comments, name="comments"),
    url("follow/(?P<username>.*)/(?P<option>.*)/", follow, name="follow"),
    url("likes/(?P<post_id>.*)/", likes, name="likes"),
    url(r'^notification/$', display_notification, name='display_notification'),
    url("save_post/(?P<post_id>.*)/", save_post, name="save_post"),
    url("post_detail/(?P<post_id>.*)/", post_details, name="post_details"),
    url(r"^new_post/$", new_post, name="new_post"),
    url(r"^profile/$", profile, name="profile"),
    url(r"^profile/fav$", profile, name="profile_fav"),
    url("profile_details/(?P<username>.*)/", profile_details, name="profile_details"),
    url(r"^edit_profile/$", edit_profile, name="edit_profile"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
