from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailsView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.PostNewView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.PostEditView.as_view(), name='post_edit'),
]
