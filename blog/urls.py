
from django.urls import path
from .import views

urlpatterns = [
    path("", views.starting_page, name='starting_page'),
    path("posts/", views.posts, name='posts'),
    path("posts/<slug:slug>", views.detail_post, name='detail_post')
]
