from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='index'),
    path('upload', views.upload, name='upload'),
    path('download', views.download, name='download')

]