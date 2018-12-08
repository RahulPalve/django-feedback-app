from app import views
from django.conf.urls import url

urlpatterns=[url('', views.index, name='index'),
            url(r'^post/(?P<pk>\d+)/$',	views.post_detail,	name='post_detail'),
            ]
