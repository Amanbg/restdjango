"""restdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
from restapp.views import UserViewSet, RecruiterViewSet, JobsViewSet, CandidateViewSet
from rest_framework.routers import DefaultRouter
from restapp import views


user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
    })

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
    })

recruiter_list = RecruiterViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
recruiter_detail = RecruiterViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


jobs_list = JobsViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
jobs_detail = JobsViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

candidate_list = CandidateViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
candidate_detail = CandidateViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'recruiters', views.RecruiterViewSet)
router.register(r'jobs', views.JobsViewSet)
router.register(r'candidates', views.CandidateViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

] + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
