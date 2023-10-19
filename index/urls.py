from django.urls import path
from . import views

app_name = 'index1'

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup')
]
