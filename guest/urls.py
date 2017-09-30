#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

from sign import views  #导入sign应用views文件

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'guest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index1/$', views.index1), #添加index/路径配置
    url(r'^index2/$', views.index2),
    url(r'^index/$', views.index),
    url(r'^login_action/$', views.login_action),
    url(r'^event_manage/$', views.event_manage),
    url(r'^accounts/login/$', views.index),
    url(r'^$', views.index),
    url(r'^search_name/$', views.search_name),
    url(r'^guest_manage/$', views.guest_manage),
    url(r'^guest_search/$', views.guest_search),
    url(r'^logout/$', views.logout),
    url(r'^sign_index/(?P<eid>[0-9]+)/$', views.sign_index),
    url(r'^sign_index_action/(?P<eid>[0-9]+)/$', views.sign_index_action),
    url(r'^api/', include('sign.urls', namespace='sign')),
)
