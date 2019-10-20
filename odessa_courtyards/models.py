from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone


# участник
class Member(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    middle_name = models.CharField(max_length=30, null=False)
    phone_number = models.CharField(max_length=10, null=False)
    email = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=30)
    registration_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.middle_name

    def get_short_name(self):
        return self.first_name + ' ' + self.last_name


# жюри
class Jury(models.Model):
    username = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    middle_name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.middle_name

    def get_short_name(self):
        return self.first_name + ' ' + self.last_name


# Заявка участника
class MemberRequest(models.Model):
    NOMINATIONS = (
        ('Старый город', 'Старый город'),
        ('Многоэтажки', 'Многоэтажки'),
        ('Самый зеленый двор', 'Самый зеленый двор'),
        ('Самый спортивный', 'Самый спортивный'),
        ('Лучший двор для детей', 'Лучший двор для детей'),
        ('Лучший стрит-арт', 'Лучший стрит-арт'),
        ('Лучший подъезд', 'Лучший подъезд')
    )
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    middle_name = models.CharField(max_length=30, null=False)
    phone_number = models.CharField(max_length=10, null=False)
    nomination = models.CharField(max_length=30,
                                  choices=NOMINATIONS,
                                  default='Старый город',
                                  null=False)
    adress = models.CharField(max_length=100, null=False)
    additional_information = models.TextField(max_length=300, null=True)

    def __str__(self):
        return self.adress + ' ' + self.nomination


# Модели формы которую заполняет пользователь "До"
class FormBefore(models.Model):
    # Привязка к юзеру
    member = models.ForeignKey(Member,
                               on_delete=models.CASCADE,
                               null=True)
    # Описание планов
    plan_description = models.TextField(max_length=2000)
    # Описание проблем
    problem_description = models.TextField(max_length=500)
    # Общая фотка
    general_view = models.ImageField()
    # Файл эскизного проекта
    conceptual_design = models.FileField()
    # одобренная не одобренная форма

    def __str__(self):
        return self.adress + ' ' + self.nomination


# Модель формы "До" которая хранит фотки проблемных участков
class ProblemArea(models.Model):
    # (Связь) ссылка на то, к какой формы привязана фотка проблемного участка
    form_before = models.ForeignKey(FormBefore,
                                    null=False,
                                    related_name='problem_photos',
                                    on_delete=models.CASCADE)
    # сама фотография проблемного участка
    photo = models.ImageField()

    def __str__(self):
        return self.form_before


# Модели формы которую заполняет пользователь "После"
class FormAfter(models.Model):
    # Связь с участником
    member = models.ForeignKey(Member,
                               null=True,
                               on_delete=models.CASCADE,)
    # Описание продленных работ
    done_work_description = models.TextField(max_length=2000, null=True)
    # Общая фотка
    general_view = models.ImageField(null=True)

    def __str__(self):
        return self.member


# Модель формы "После" которая хранит фотки решенных участков
class ReformedAreas(models.Model):
    # (Связь) ссылка на то, к какой формы привязана фотка решенного участка
    form_after = models.ForeignKey(FormAfter,
                                   null=True,
                                   related_name='reformed_photos',
                                   on_delete=models.CASCADE)
    # Сама фотография исправленного участка
    photo = models.ImageField()

    def __str__(self):
        return self.form_after


# Оставленные оценки
class Mark(models.Model):
    # Генерирует возможные оценки для выбора
    MARKS_LIST = (
        tuple([mark for mark in range(100)])
    )
    # Ссылка на форму "После"
    form_after = models.ForeignKey(FormAfter,
                                   related_name='appraised_yards',
                                   on_delete=models.CASCADE)
    # Ссылка на того, кто оставил
    jury = models.ForeignKey(Jury,
                             on_delete=models.CASCADE)
    # зафиксированная оценка
    value = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.jury
