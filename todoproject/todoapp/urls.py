from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home-page'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('delete-task/<str:name>/', views.delete_task, name='delete'),
    path('update-task/<str:name>/', views.update, name='update')

]