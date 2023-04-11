from django.urls import path
from .views import CreatePostView, ListPostsView, PostDetailView, PostUpdateView

urlpatterns = [
    path('posts/', CreatePostView.as_view(), name='create_post'),
    path('posts/list/', ListPostsView.as_view(), name='list_posts'),
    path('posts/<int:id>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:id>/update/', PostDetailView.as_view(), name='post_update'),
]
