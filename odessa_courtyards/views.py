from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View

from .forms import (MemberRequestForm,
                    FormBeforeForm,
                    FormAfterForm)

from .models import (MemberRequest,
                     FormBefore,
                     ProblemArea)
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


'''
    Классы обработки запросов без view
'''

# Логика обработки формы создания нового студента из формы
class MemberRequestCreate(View):
    def get(self, request):
        form = MemberRequestForm()
        return render(request, 'form.html', context={'form': form})

    def post(self, request):
        bound_form = MemberRequestForm(request.POST)
        if bound_form.is_valid():
            new_member_request = bound_form.save()
            return redirect('../')
        return render(request, 'form.html', context={'form': bound_form})


# Логика обработки формы "До"
class FormBeforeCreate(View):
    def get(self, request):
        form = FormBeforeForm()
        return render(request, 'form.html', context={'form': form})

    def post(self, request):
        bound_form = FormBeforeForm(request.POST)
        if bound_form.is_valid():
            new_member_request = bound_form.save()
            return redirect('../')
        return render(request, 'form.html', context={'form': bound_form})


# Логика обработки формы "После"
class FormAfterCreate(View):
    def get(self, request):
        form = FormAfterForm()
        return render(request, 'form.html', context={'form': form})

    def post(self, request):
        bound_form = FormAfterForm(request.POST)
        if bound_form.is_valid():
            new_member_request = bound_form.save()
            return redirect('../')
        return render(request, 'form.html', context={'form': bound_form})
