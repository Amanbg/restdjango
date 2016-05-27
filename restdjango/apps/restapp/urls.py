from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from restapp import views

urlpatterns = [
	url(r'^$',views.api_root),
	url(r'^people/(?P<pk>[0-9]+)/highlight/$',views.PeopleHighlight.as_view(), name='people-highlight'),
	url(r'^users/$',views.UserList.as_view(), name='user-list'),
	url(r'^users/(?P<pk>[0-9]+)/$',views.UserDetail.as_view(), name='user-detail'),
	url(r'^people/$',views.PeopleList.as_view(), name='people-list'),
	url(r'^people/(?P<pk>[0-9]+)/$',views.PeopleDetail.as_view(), name='people-detail'),

]
urlpatterns = format_suffix_patterns(urlpatterns)
# urlpatterns += [
# 	url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
# ]