from django.urls import path
from blog.views import (
    IndexView,
    PostDetailView,
    CategoryListView,
    TagListView,
    CategoryPostView,
    TagPostView,
    SearchPostView,
    AboutView,
)

app_name = 'blog'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/<str:category_slug>/', CategoryPostView.as_view(), name='category_post'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('tag/<str:tag_slug>/', TagPostView.as_view(), name='tag_post'),
    path('search/', SearchPostView.as_view(), name='search_post'),
    path('about/', AboutView.as_view(), name='about'),
]

