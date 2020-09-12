from flask import Flask, render_template
import data as tours_data

app = Flask(__name__)


@app.route('/')
def main():
    template = render_template('index.html')
    return template

@app.route('/departures/<departure>/')
def departures(departure):
    template = render_template('departure.html')
    return template

@app.route('/tours/<id>/')
def tours(id):
    template = render_template('tour.html')
    return template

@app.route('/data/')
def data():
    ret = "<h1>Все туры:</h1>"+"\n"
    for i in tours_data.tours.keys():
        ret = ret + "<p>"+\
              tours_data.tours[i]["country"]+\
              ': <a href="/data/tours/'+str(i)+'/">'+\
              tours_data.tours[i]["title"]+\
              "</a></p>"
    return ret

@app.route('/data/departures/<departure>/')
def data_departures(departure):
    departure_place="Неверный пункт отправления"
    ret_departure = ""
    for i in tours_data.tours.keys():
        if tours_data.tours[i]["departure"] == departure:
            ret_departure = ret_departure + \
                            "<p>"+tours_data.tours[i]["country"]+':<a href="/tours/'+str(i)+'/">'+ \
                            tours_data.tours[i]["title"]+"</a></p>\n"
            departure_place = tours_data.departures[departure]

    ret = "<h1>Туры по направлению "+departure_place+": </h1>\n"+ret_departure


    return ret

@app.route('/data/tours/<int:tour>/')
def data_tours(tour):
    td = tours_data.tours[tour]
    ret_tour = "<h1>"+td["country"]+": "+td["title"]+":</h1>\n"+\
               "<p>"+str(td["nights"])+" ночей</p>\n"+\
               "<p>Стоимость: "+str(td["price"])+" Р</p>\n"+\
               "<p>"+td["description"]+"</p>"

    return ret_tour

if __name__ == '__main__':
    app.run()
