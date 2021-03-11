from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError


# Create your views here.

def MainView(request):
    return render(request, 'tours/index.html')


def DepartureView(request):
    return render(request, 'tours/departure.html')


def TourView(request):
    return render(request, 'tours/tour.html')


def custom_handler404(request, exception):
    return HttpResponseNotFound('404 Страница не найдена!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
