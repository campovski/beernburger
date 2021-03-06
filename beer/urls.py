from django.conf.urls import url
from . import views

app_name = 'beer'

urlpatterns = [
	# /beer/
	url(r'^$', views.index, name="index"),
	
	# /beer/<beer_id>/
	url(r'^review/(?P<beer_id>[0-9]+)/$', views.detail, name="detail"),

	# /beer/search=<query>/
	url(r'^search=(?P<query>[\s\S]+)/$', views.search, name="search"),

	# /beer/sort=<sort_by>/
	url(r'sort=(?P<sort_by>[\s\S]+)/$', views.index, name='sort'),

	# /beer/browse=<query>/for=<item>/
        url(r'browse=(?P<query>[\s\S]+)/for=(?P<item>[\s\S]+)/$', views.browse_item, name='browse_item'),

	# /beer/browse=<query>/
	url(r'browse=(?P<query>[\s\S]+)/$', views.browse, name='browse'),

]
