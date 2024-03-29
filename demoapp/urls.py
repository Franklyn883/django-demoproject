from django.urls import path
from . import views
app_name = 'demoapp' #we do this for the sake of namespacing
urlpatterns = [
    path("", views.home, name='home'),
    path("sayHello/", views.sayHello),
    path("index/", views.index),
    #path('getuser/<name>/<id>', views.pathview),
    path('getuser/', views.qryview),
    path('dishes/<str:dish>', views.menuitems),
    path('form/', views.form_view),
    path('about/', views.about, name='about'),
    path('checkname/<str:name>',views.checkname, name='checkname'),
    path('menu/', views.menu_id),
    path('register/', views.register, name="register"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
]