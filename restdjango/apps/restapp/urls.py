from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from restapp import views


urlpatterns = [
    url(r'^users/$', views.UserList.as_view(), name='user_list'),
    url(r'^users/$', views.UserDetail.as_view(), name='user_detail'),
    url(r'^recruiters/$', views.RecruiterList.as_view(), name='recruiter-list'),
    url(r'^recruiters/(?P<pk>[0-9]+)/$', views.RecruiterDetail.as_view(), name='recruiter-detail'),
    url(r'^jobs/$', views.JobsList.as_view(), name='jobs-list'),
    url(r'^jobs/(?P<pk>[0-9]+)/$', views.JobsDetail.as_view(), name='jobs-detail'),
    url(r'^candidates/$', views.CandidateList.as_view(), name='candidate-list'),
    url(r'^candidates/(?P<pk>[0-9]+)/$', views.CandidateDetail.as_view(), name='candidate-detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
