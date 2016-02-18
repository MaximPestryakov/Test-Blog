from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^login/', views.user_login),
  url(r'^logout/', views.user_logout),
  url(r'^new-post/', views.new_post),
  url(r'^get-post/', views.get_post),
  url(r'^$', views.posts),
]