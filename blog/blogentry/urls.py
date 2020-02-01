from django.urls import path

from . import views

handler404 = views.handler404
handler500 = views.handler500

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:the_slug>/', views.detail, name='BlogItem'),
] 
