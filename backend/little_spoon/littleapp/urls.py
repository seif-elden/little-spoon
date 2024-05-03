from django.urls import path

from . import views

urlpatterns = [
    path("", views.mybookmarks, name="home"),
    path("explore/", views.explore, name="explore"),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('myprofile/', views.myprofile, name='myprofile'),
]