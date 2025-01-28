from django.urls import path
from . import views 

urlpatterns = [
            path('',  views.landing_page, name= 'landingPage'),
            path('post/<>', views.all_posts, name='postsLists '),
            path('slug/<slug>', views.fullpost,name='onePost'),
]
