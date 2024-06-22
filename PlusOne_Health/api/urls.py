from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import *

urlpatterns = [
    
    path('', index ,name="index"),
    path('login/',user_login,name="login"),
    path('logout/',user_logout,name="logout"),
    path('signup/',user_signup,name="signup"),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('profile/<int:id>/', profile, name='profile'),
    path('add-post/',add_post,name="add_post"),
    path('post-delete/<int:id>',post_delete,name="post_delete"),
    path('comment-delete/<int:id>',comment_delete,name="comment_delete"),


]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)