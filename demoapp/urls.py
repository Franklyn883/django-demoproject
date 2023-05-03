from django.urls import path
from . import views
app_name = 'demoapp' #we do this for the sake of namespacing
urlpatterns = [
    path("", views.home),
    path("sayHello/", views.sayHello),
    path("index/", views.index),
    #path('getuser/<name>/<id>', views.pathview),
    path('getuser/', views.qryview),
    path('dishes/<str:dish>', views.menuitems),
]