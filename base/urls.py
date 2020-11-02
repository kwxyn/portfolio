from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('posts/', views.posts, name="posts"),
	path('post/<slug:slug>/', views.post, name="post"),
	path('send_email/', views.sendEmail, name="send_email"),
]