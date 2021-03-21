import random
from django import template
from tours.data import tours

register = template.Library()


@register.filter()
def random_6_tour():
    kol = 1
    tours_dict = {}
    while kol <= 6:
        random_num = random.randint(1, 16)
        if random_num not in tours_dict:
            tours_dict[random_num] = tours[random_num]
            kol += 1
    return tours_dict


@register.filter()
def departure_ture(departure):
    tours_dict = {}
    for tour_id, tour_value in tours.items():
        if tour_value['departure'] == departure:
            tours_dict[tour_id] = tour_value
    return tours_dict


@register.filter()
def tour_search(dict_tour):
    tours_search = {'min_price': 999999, 'max_price': 0, 'max_nights': 1, 'min_nights': 999999,
                    'kol_tour': len(dict_tour)}
    for key, value in dict_tour.items():
        if value['price'] < tours_search['min_price']:
            tours_search['min_price'] = value['price']
        if value['price'] > tours_search['max_price']:
            tours_search['max_price'] = value['price']
        if value['nights'] > tours_search['max_nights']:
            tours_search['max_nights'] = value['nights']
        if value['nights'] < tours_search['min_nights']:
            tours_search['min_nights'] = value['nights']
    return tours_search
