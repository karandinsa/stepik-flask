import data as tours_data


def data_tours(id):
    td = tours_data.tours[id]
    ret_tour = "<h1>" + td["country"] + ": " + td["title"] + ":</h1>\n" + \
               "<p>" + str(td["nights"]) + " ночей</p>\n" + \
               "<p>Стоимость: " + str(td["price"]) + " Р</p>\n" + \
               "<p>" + td["description"] + "</p>"

    return ret_tour
