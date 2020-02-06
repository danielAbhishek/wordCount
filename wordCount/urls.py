from django.conf.urls import url

from . import views

urlpatterns = [
    url('homepage', views.homepage, name = 'homepage'),
    url('count/', views.count, name = 'count'),
    url('about/', views.about, name = 'about')
    
]
