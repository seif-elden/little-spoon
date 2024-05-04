from django.urls import path

from . import views

urlpatterns = [
    path("", views.mybookmarks, name="home"),
    path("explore/", views.explore, name="explore"),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),

    path('myprofile/', views.myprofile, name='myprofile'),
    path('editprofile/<pk>/', views.editprofile, name='editprofile'),

    path('addrecipe/', views.addrecipe, name='addrecipe'),
    path('viewrecipe/<pk>/', views.viewrecipe, name='viewrecipe'),
    path('deleterecipe/<pk>/', views.deleterecipe, name='deleterecipe'),
    path('addbockmark/<pk>/', views.addbockmark, name='addbockmark'),
    path('removebockmark/<pk>/', views.removebockmark, name='removebockmark'),
    path('likerecipe/<pk>/', views.likerecipe, name='likerecipe'),
    path('unlikerecipe/<pk>/', views.unlikerecipe, name='unlikerecipe'),

    path('updaterecipe/<pk>/', views.updaterecipe, name='updaterecipe'),


]