from restapp.models import Recruiter, Candidate, Jobs
from restapp.serializers import RecruiterSerializer, JobsSerializer, CandidateSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets


class RecruiterViewSet(viewsets.ModelViewSet):

    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class JobsViewSet(viewsets.ModelViewSet):

    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CandidateViewSet(viewsets.ModelViewSet):

    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# class RecruiterList(generics.ListCreateAPIView):
#     queryset = Recruiter.objects.all()
#     serializer_class = RecruiterSerializer


# class RecruiterDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Recruiter.objects.all()
#     serializer_class = RecruiterSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadonly,)


# class JobsList(generics.ListCreateAPIView):
#     queryset = Jobs.objects.all()
#     serializer_class = JobsSerializer


# class JobsDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Jobs.objects.all()
#     serializer_class = JobsSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadonly,)


# class CandidateList(generics.ListCreateAPIView):
#     queryset = Candidate.objects.all()
#     serializer_class = CandidateSerializer


# class CandidateDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Candidate.objects.all()
#     serializer_class = CandidateSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadonly,)
