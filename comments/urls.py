from django.conf.urls import url
from . import views
app_name='comments'
urlpatterns=[
    url(r'^detail/(?P<post_pk>[0-9]+)/$',views.post_comment,name='detail_comments'),
]