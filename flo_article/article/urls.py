from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('', views.articlespage,name='article-base'),
    path('',views.posts,name='posts'),
    path('blogpost/<int:id>',views.blogpost,name='blogposts'),
    path('newposts/',views.newposts,name='newposts'),
    path('newerposts/',views.newerposts,name='newerposts'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
