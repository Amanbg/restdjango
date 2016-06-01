from rest_framework import serializers
from restapp.models import Recruiter, Candidate, Jobs
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = ('url', 'username', 'first_name', 'last_name', 'gender', 'contact', 'email_id', 'date_joined')


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ('url', 'company', 'jobtitle', 'created_on', 'is_active', 'exp_required', 'salary')

        def create(self, validated_data):
            jobs = Jobs.objects.create(validated_data['company'])
            jobs.save()
            return jobs


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('url', 'username', 'first_name', 'last_name', 'apply_for', 'apply_on', 'recruiter', 'email_id', 'contact')

        def create(self, validated_data):
            candidate = Candidate.objects.create(validated_data['apply_for'], validated_data['recruiter'])
            candidate.save()
            return candidate
