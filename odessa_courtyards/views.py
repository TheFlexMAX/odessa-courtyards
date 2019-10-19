from django.shortcuts import render
from rest_framework import viewsets

from .models import MemberRequest, FormBefore, ProblemArea
                    #FormAfter, ReformedAreas
from .serializers import MemberRequestSerializer, FormBeforeSerializer, ProblemAreaSerializer


class MemberRequestViewSet(viewsets.ModelViewSet):
    serializer_class = MemberRequestSerializer
    queryset = MemberRequest.objects.all()

class FormBeforeViewSet(viewsets.ModelViewSet):
    serializer_class = FormBeforeSerializer
    queryset = FormBefore.objects.all()

class ProblemAreaViewSet(viewsets.ModelViewSet):
    serializer_class = ProblemAreaSerializer
    queryset = ProblemArea.objects.all()