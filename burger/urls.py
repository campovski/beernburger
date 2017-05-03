from django.conf.urls import url
from . import views

app_name = 'burger'

urlpatterns = [
	# /burger/
	url(r'^$', views.index, name="index"),
	
	# /burger/<beer_id>/
	url(r'^review/(?P<burger_id>[0-9]+)/$', views.detail, name="detail"),

	# /burger/search=<query>/
	url(r'^search=(?P<query>[\s\S]+)/$', views.search, name="search"),
	
	# /burger/sort=<sort_by>/
	url(r'sort=(?P<sort_by>[\s\S]+)/$', views.index, name='sort'),

	# /burger/browse=maker/for=<item>/
        url(r'browse=maker/for=(?P<item>[\s\S]+)/$', views.browse_item, name='browse_item'),

	# /burger/browse=maker/
        url(r'browse=maker/$', views.browse, name='browse'),
]
