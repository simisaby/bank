from . import views
from django.urls import path

app_name = 'bankapp'    #namespace

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('user/',views.user,name='user'),
    path('form/',views.form,name="form"),
]