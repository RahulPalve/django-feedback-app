from app import views
from django.conf.urls import url

urlpatterns=[ url(r'^post/(?P<pk>\d+)/$',	views.post_detail,	name='post_detail'),
                url(r'^$', views.index, name='index'),
           
            ]
