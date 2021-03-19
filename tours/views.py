from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.views import View


# Create your views here.

def main_view(request):
    return render(request, 'tours/index.html')


def departure_view(request, departure):
    return render(request, 'tours/departure.html')


def tour_view(request,tour_id):
    return render(request, 'tours/tour.html')


def custom_handler404(request, exception):
    return HttpResponseNotFound('404 Страница не найдена!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')

