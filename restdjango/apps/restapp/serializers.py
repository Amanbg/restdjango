from django.contrib.auth.models import User
from rest_framework import serializers
from restapp.models import People

class PeopleSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	highlight = serializers.HyperlinkedIdentityField(view_name='people-highlight', format='html')

	class Meta:
		model = People
		fields = ('url','highlight','owner',
					'first_name','last_name','contact','emailid','created_on')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	# peoples = serializers.HyperlinkedRelatedField(many=True, view_name='people-detail',read_only=True)

	class Meta:
		model = User
		fields = ('url','username','email','is_staff')