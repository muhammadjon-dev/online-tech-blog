from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('category-list/<int:pk>/', PostsByCategory.as_view(), name='category'),
    path('post-detail/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('post/add/', AddPostView.as_view(), name='add_post'),
    path('comment/<int:pk>/add/', AddCommentView.as_view(), name='add_comment'),
    path('like/post/<int:pk>/', LikeView.as_view(), name='like'),
    path('search/', SearchView.as_view(), name='search'),
]