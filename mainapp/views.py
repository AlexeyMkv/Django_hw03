from django.shortcuts import render
from datetime import datetime
from mainapp.models import Hobby, Study, Work


# Create your views here.
def main_page(request):
    """
    Представление главной страницы сайта
    """
    title = "Небольшая страница с информацией обо мне!"
    surname = "Маликов"
    name = "Алексей"
    patronymic = "Валерьевич"
    birthday = datetime(2021, 3, 8)
    hobby_list = Hobby.objects.all()
    context = {
        'surname': surname,
        'name': name,
        'patronymic': patronymic,
        'birthday': birthday,
        'title': title,
        'hobby_list': hobby_list,
    }
    return render(request, 'index.html', context)


def study(request):
    """
    Представление страницы с информацией о местах обучения
    """
    title = "Мои места обучения"
    school_name = "Школа №1985"
    university = "Российский Новый Университет"
    study_places_list = Study.objects.all()
    context = {
        'title': title,
        'school_name': school_name,
        'university': university,
        'study_places_list': study_places_list,
    }
    return render(request, 'study.html', context)


def work(request):
    places_of_work_list = Work.objects.all()
    title = 'Мои места работы'
    context = {
        'title': title,
        'work_list': places_of_work_list,
    }
    return render(request, 'work.html', context)
