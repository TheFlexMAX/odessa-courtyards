from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .forms import (MemberRequestForm,
                    FormBeforeForm,
                    FormAfterForm)
from .models import (MemberRequest,
                     FormBefore,
                     FormAfter)
from .serializers import (MemberRequestSerializer,
                          FormBeforeSerializer,
                          FormAfterSerializer)


class MemberRequestViewSet(viewsets.ModelViewSet):
    serializer_class = MemberRequestSerializer
    queryset = MemberRequest.objects.all()


class FormBeforeViewSet(viewsets.ModelViewSet):
    serializer_class = FormBeforeSerializer
    queryset = FormBefore.objects.all()


class FormAfterViewSet(viewsets.ModelViewSet):
    serializer_class = FormAfterSerializer
    queryset = FormAfter.objects.all()

'''
    Классы обработки запросов без view
'''

# Логика обработки формы создания нового студента из формы
class MemberRequestCreate(APIView):
    def post(self, request):
        serializer_class = MemberRequestSerializer(data=request.data)
        print(f"serializer_class.is_valid(): {serializer_class.is_valid()}")
        print(f"request.data: {request.data}")
        print(f"serializer_class.errors: {serializer_class.errors}")
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


# Логика обработки второй формы
class FormBeforeCreate(APIView):
    def post(self, request):
        serializer_class = FormBeforeSerializer(data=request.data)
        print(f"serializer_class.is_valid(): {serializer_class.is_valid()}")
        print(f"request.data: {request.data}")
        print(f"serializer_class.errors: {serializer_class.errors}")
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


# Логика обработки формы "После"
class FormAfterCreate(APIView):
    def post(self, request):
        serializer_class = FormAfterSerializer(data=request.data)
        print(f"serializer_class.is_valid(): {serializer_class.is_valid()}")
        print(f"request.data: {request.data}")
        print(f"serializer_class.errors: {serializer_class.errors}")
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
