from django.conf.urls import patterns, url
from maxi import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^tutorial/(?P<id>[\w\-]+)/$', views.tutorial, name='tutorial'),	
	url(r'^experiment/(?P<id>[\w\-]+)/(?P<question_nr>[\w\-]+)/$', views.experiment, name='experiment'),
	url(r'^postexperiment/(?P<id>[\w\-]+)/$', views.postexperiment, name='postexperiment'),
	url(r'^debriefing', views.debriefing, name='debriefing'),
	url(r'^data', views.data, name='data'),
	)
	

#	url(r'^preexperiment/(?P<id>[\w\-]+)/$', views.preexperiment, name='preexperiment'),