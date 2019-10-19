from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager
from django.contrib.auth.base_user import AbstractBaseUser

# участник


# жюри


# модератор


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


# Модели формы которую заполняет пользователь "До"
class FormBefore(models.Model):
    # Описание планов
    plan_description = models.TextField(max_length=2000)
    # Описание проблем
    problem_description = models.TextField(max_length=500)
    # Общая фотка
    general_view = models.ImageField()
    # Файл эскизного проекта
    conceptual_design = models.FileField()
    # одобренная не одобренная форма



# Модель формы "До" которая хранит фотки проблемных участков
class ProblemArea(models.Model):
    # (Связь) ссылка на то, к какой формы привязана фотка проблемного участка
    form_before = models.ForeignKey(FormBefore,
                                    null=False,
                                    related_name='problem_photos',
                                    on_delete=models.CASCADE)
    # сама фотография проблемного участка
    photo = models.ImageField()



class FormAfter(models.Model):
    # Связь с участником
    member = models.ForeignKey(Member,
                               null=False,
                               on_delete=models.CASCADE)
    # Общая фотка
    general_view = models.ImageField()


# Модель формы "После" которая хранит фотки решенных участков
class ReformedAreas(models.Model):
    # (Связь) ссылка на то, к какой формы привязана фотка решенного участка
    form_after = models.ForeignKey(FormAfter,
                                   null=True,
                                   related_name='reformed_photos',
                                   on_delete=models.CASCADE)
    # Сама фотография исправленного участка
    photo = models.ImageField()