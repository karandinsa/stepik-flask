from helpers import render_index_html,render_departure_html,render_tour_html
from helpers import render_data_html, render_data_departures_html, render_data_tours
from data import departures, tours


def check_departure(departure):
    if departure not in departures.keys():
        ret = "<h1>Неверный пункт отправления</h1>" \
              "<p>Верные пункты: " + ",".join(departures.keys()) + "</p>"
        return ret, 404
    else:
        return "OK", 200


def check_tour(id):
    ret = "<h1>Такого тура не существует</h1>"
    try:
        if int(id) not in tours.keys():
            return ret, 404
        else:
            return "OK", 200
    except Exception as e:
        return ret, 404

def index_html():
    return render_index_html.index_html()


def departure_html(departure):
    ret,status = check_departure(departure)
    if status == 200:
        return render_departure_html.departure_html(departure)
    else:
        return ret


def tour_html(id):
    ret, status = check_tour(id)
    if status == 200:
        return render_tour_html.tour_html(id)
    else:
        return ret


def data_html():
    return render_data_html.data_html()


def data_departures_html(departure):
    ret, status = check_departure(departure)
    if status == 200:
        return render_data_departures_html.data_departures_html(departure)
    else:
        return ret


def data_tours_html(id):
    ret, status = check_tour(id)
    if status == 200:
        return render_data_tours.data_tours(int(id))
    else:
        return ret
