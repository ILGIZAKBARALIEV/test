from django.urls import path
from . import views
from .views import books_list

urlpatterns = [
    path('',books_list,name='books_list'),
    path('books_detail/<int:id>/',views.books_detail,name='books_detail'),
    path('emoji/', views.emodji, name='emoji'),
    path('text/', views.text, name='text'),
    path('image/', views.image, name='image'),
    path ('about_me/',views.about_me,name='about_me'),
    path('text_and_photo/',views.text_and_photo,name='text_and_photo'),
    path('system_time/',views.system_time,name='system_time')
]