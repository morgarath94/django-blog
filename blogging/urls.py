from django.urls import path
from blogging.views import stub_view, PostListView, PostDetailView

urlpatterns = [
    path("", PostListView.as_view(), name="blog_index"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="blog_detail"),
]
