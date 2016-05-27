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
from restapp import views
from rest_framework.routers import DefaultRouter
from rest_framework import routers, serializers, viewsets
from restapp.views import UserViewSet, PeopleViewSet,api_root
from rest_framework import renderers


people_list = PeopleViewSet.as_view({
        'get':'list',
        'post':'create'
    })
people_detail = PeopleViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy'
    })

people_highlight = PeopleViewSet.as_view({
    'get':'highlight',
    }, renderer_classes = [renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get':'list'
    })
user_detail = UserViewSet.as_view({
    'get':'retrieve'
    })


# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'peoples', views.PeopleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

] + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
