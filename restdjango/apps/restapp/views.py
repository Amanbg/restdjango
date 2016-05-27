from rest_framework.decorators import api_view
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import renderers
from restapp.models import People
from rest_framework import generics
from restapp.serializers import PeopleSerializer
from restapp.serializers import UserSerializer
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework import viewsets


@api_view(['GET','POST'])
def api_root(request, format=None):
	return Response({
		'users':reverse('user-list',request=request , format=format),
		'people':reverse('people-list',request=request, format=format)
		})
class UserViewSet(viewsets.ReadOnlyModelViewSet):

	queryset = User.objects.all()
	serializer_class = UserSerializer

class PeopleViewSet(viewsets.ModelViewSet):
	
	queryset = People.objects.all()
	serializer_class = PeopleSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs):
		people= self.get_object()
		return Response(people.highlighted)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)