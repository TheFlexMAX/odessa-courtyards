from rest_framework import serializers
from .models import MemberRequest, FormBefore, FormAfter


class MemberRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberRequest
        fields = ('NOMINATIONS', 'first_name', 'last_name', 'middle_name',
                  'phone_number', 'nomination', 'adress', 'additional_information')


class FormBeforeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormBefore
        fields = ('plan_description', 'problem_description', 'general_view', 'conceptual_design')


class FormAfterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormAfter
        fields = ('member', 'done_work_description', 'general_view')
