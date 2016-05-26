# from django.shortcuts import render
# from django.http import HttpResponse
# from django.http import Http404
# from rest_framework.views import APIView
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from restapp.models import People
from rest_framework import generics
from restapp.serializers import PeopleSerializer
from rest_framework import permissions


# Create your views here.

# class JSONResponse(HttpResponse):
# 	"""
# 	An HttpResponse that renders its content into JSON.
# 	"""

# 	def __init__(self,data, **kwargs):
# 		content = JSONRenderer().render(data)
# 		kwargs['content_type']='application/json'
# 		super(JSONResponse, self).__init__(content, **kwargs)

# @api_view(['GET','POST'])
class PeopleList(generics.ListCreateAPIView): 
	"""
	List all peoples , or create a new user.
	"""
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset = People.objects.all()
	serializer_class = PeopleSerializer
	
	def perform_create(self, serializer):
	    serializer.save(owner=self.request.user)
	# def get(self, request,format=None):
	# 	people = People.objects.all()
	# 	serializer = PeopleSerializer(people)
	# 	return Response(serializer.data)

	# def post(self, request,format=None):
	# 	serializer = PeopleSerializer(data=request.data)
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return Response(serializer.data, status=status.HTTP_201_CREATED)
	# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','POST'])
class PeopleDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve , update or delete an individual. 
	"""
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	queryset = People.objects.all()
	serializer_class = PeopleSerializer
	# def get_object(self, pk):
	# 	try:
	# 		# people = People.objects.get(pk=pk)
	# 		return People.objects.get(pk=pk)
	# 	except People.DoesNotExist:
	# 		return Http404
	# 		# return HttpResponse(status=404)
	# def get(self, request,pk,format=None):
	# 	people = self.get_object(pk)
	# 	serializer = PeopleSerializer(people)
	# 	return Response(serializer.data)

	# def put(self, request,pk,format=None):
	# 	people = self.get_object(pk)
	# 	serializer=PeopleSerializer(people, data=request.data)
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return Response(serializer.data)
	# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	# def delete(self, request,pk,format=None):
	# 	people = self.get_object(pk)
	# 	people.delete()
	# 	return Response(status=status.HTTP_204_NO_CONTENT) 