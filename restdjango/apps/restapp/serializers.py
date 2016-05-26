from rest_framework import serializers
from restapp.models import People

class PeopleSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = People
		fields = ('id','first_name','last_name','contact','emailid','created_on','owner')
