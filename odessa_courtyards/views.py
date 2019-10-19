from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View

from .forms import (
    MemberRequestForm
)

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

        print(f"bound_form.is_valid(): {bound_form.is_valid()}")
        print(f"bound_form: {bound_form}")
        if bound_form.is_valid():
            new_member_request = bound_form.save()
            return redirect('../')
        return render(request, 'form.html', context={'form': bound_form})

