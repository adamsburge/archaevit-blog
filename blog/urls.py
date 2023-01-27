from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('filter_interesting/', views.PostListInteresting.as_view(), name='filter_interesting'),
    path('filter_important/', views.PostListImportant.as_view(), name='filter_important'),
    path('filter_underrated/', views.PostListUnderrated.as_view(), name='filter_underrated'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('update_post/<slug:slug>', views.update_post, name='update-post'),
    path('add_post/', views.add_post, name='add-post'),
    path('delete/<slug:slug>', views.delete_post, name='delete-post'),
]
