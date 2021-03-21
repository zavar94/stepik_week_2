from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
from tours.data import tours, departures
from tours.templatetags import function


# Create your views here.
def main_view(request):
    return render(request, 'tours/index.html', context={'tours': function.random_6_tour(),
                                                        })


def departure_view(request, departure):
    tours_departure = function.departure_ture(departure)
    return render(request, 'tours/departure.html', context={'tours': tours_departure,
                                                            'direction': departures[departure],
                                                            'tour_search': function.tour_search(tours_departure),
                                                            })


def tour_view(request, tour_id):
    tour = tours[tour_id]
    return render(request, 'tours/tour.html', context={'tours': tour,
                                                       'departures': departures[tour['departure']],
                                                       'stars': '★' * int(tour['stars']),
                                                       })


def custom_handler404(request, exception):
    return HttpResponseNotFound('404 Страница не найдена!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
