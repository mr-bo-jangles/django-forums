from django.conf.urls import patterns, url

from views import CategoryListView, ForumDetailView, TopicDetailView, TopicCreateView


urlpatterns = patterns('',
    url(r'^$', CategoryListView.as_view(), name='overview'),
    url(r'^(?P<pk>\d+)/$', ForumDetailView.as_view(), name='forum'),
    url(r'^(?P<forum_id>\d+)/create/$', TopicCreateView.as_view(), name='topic_create'),
    url(r'^topic/(?P<pk>\d+)/$', TopicDetailView.as_view(), name='topic'),
)
