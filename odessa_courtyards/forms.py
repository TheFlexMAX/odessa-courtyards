from django.db import models
from django import forms

from .models import (
    MemberRequest,
    FormBefore,
    FormAfter,
    Member
)

# Первая форма (Подача заявления)
class MemberRequestForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя')
    second_name = forms.CharField(label='Фамилия')
    middle_name = forms.CharField(label='Отчество')
    phone_number = forms.CharField(label='Номер телефона', max_length=10)
    nomination = forms.ModelChoiceField(queryset=MemberRequest.objects.all(),
                                        label='Номинация',
                                        empty_label="Выберите номинацию")
    adress = forms.CharField(label='Адрес')
    additional_information = forms.Textarea()

    class Meta:
        model = MemberRequest
        fields = ['first_name', 'second_name', 'middle_name', 'phone_number', 'nomination', 'adress', 'additional_information']


# Вторая форма "До"
class FormBeforeForm(forms.ModelForm):
    #FIXME: костыль
    member = forms.ModelChoiceField(queryset=Member.objects.all(),
                                    label='Участник',
                                    empty_label="Выберите юзера")

    plan_description = forms.Textarea()
    problem_description = forms.Textarea()
    general_view = forms.ImageField()
    conceptual_design = forms.FileField()

    class Meta:
        model = FormBefore
        fields = ['member', 'plan_description', 'problem_description', 'general_view', 'conceptual_design']


# Третья форма "После"
class FormAfterForm(forms.ModelForm):
    member = forms.ModelChoiceField(queryset=Member.objects.all(),
                                    label='Участник',
                                    empty_label="Выберите юзера")
    done_work_description = forms.Textarea()
    general_view = forms.ImageField()

    class Meta:
        model = FormAfter
        fields = []