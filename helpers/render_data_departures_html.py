import data as tours_data


def data_departures_html(departure):
    departure_place="Неверный пункт отправления"
    ret_departure = ""
    for i in tours_data.tours.keys():
        if tours_data.tours[i]["departure"] == departure:
            ret_departure = ret_departure + \
                            "<p>"+tours_data.tours[i]["country"]+':<a href="/tours/'+str(i)+'/">'+ \
                            tours_data.tours[i]["title"]+"</a></p>\n"
            departure_place = tours_data.departures[departure]

    return "<h1>Туры по направлению "+departure_place+": </h1>\n"+ret_departure

