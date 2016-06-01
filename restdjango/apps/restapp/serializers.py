from rest_framework import serializers
from restapp.models import Recruiter, Candidate, Jobs


class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruiter
        fields = ('url', 'username', 'first_name', 'last_name', 'gender', 'contact', 'email_id', 'date_joined')


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ('url', 'recruiter', 'jobtitle', 'created_on', 'is_active', 'exp_required', 'salary')

        def create(self, validated_data):
            jobs = Jobs.objects.create(validated_data['recruiter'])
            jobs.save()
            return jobs


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('url', 'username', 'first_name', 'last_name', 'apply_to', 'apply_on', 'email_id', 'contact')

        def create(self, validated_data):
            candidate = Candidate.objects.create(validated_data['apply_to'])
            candidate.save()
            return candidate
