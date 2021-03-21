from tours.data import departures


def navigation(request):
    depart = {'departures_context': departures}
    return depart
