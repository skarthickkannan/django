"""project URL Configuration

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
from django.contrib import admin
from django.urls import path
from main.views import home, register, profile, search, PostList, like_view, dislike_view, add_comment, PostCreate, PostUpdate, PostDetail, PostDelete, UserPostList
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', PostList.as_view(template_name='home.html'), name='home'),
    path('search/', search, name='search'),
    path('post/<int:id>/detail/comment/', add_comment, name='comment'),
    path('like/<int:pk>/', like_view, name='like_post'),
    path('dislike/<int:pk>/', dislike_view, name='dislike_post'),
    path('post/new/', PostCreate.as_view(template_name='post_form.html'), name='post_form'),
    path('post/<int:pk>/update/', PostUpdate.as_view(template_name='post_form.html'), name='post_update'),
    path('post/<int:pk>/detail/', PostDetail.as_view(template_name='post_detail.html'), name='post_detail'),
    path('post/<int:pk>/delete/', PostDelete.as_view(template_name='post_confirm_delete.html'), name='post_delete'),
    path('user/<str:username>/', UserPostList.as_view(template_name='user_posts.html'), name='user_posts'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)