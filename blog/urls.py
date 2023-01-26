from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('update_post/<slug:slug>', views.update_post, name='update-post'),
    path('add_post/', views.add_post, name='add-post'),
]
