from django.urls import path
from . import views 

urlpatterns = [
    path('',  views.landing_page, name= 'landing_page'),
    path('posts', views.postsList,  name='postsList'),
    path('posts/<slug:slug>', views.onePost,name='onePost'), # Corrected
]