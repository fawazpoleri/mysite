from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index, name="index"),
    
    path('contact/',views.contact, name="contact"),
    path('promotion/',views.promotion, name="promotion"),
    path('about/',views.about, name="about"),
    path('gallery/',views.gallery, name="gallery"),

    path('career/',views.career, name="career"),
    path('blog/',views.blog, name="blog"),
    path('career/', views.send_mail_page)



    

    
   
]
