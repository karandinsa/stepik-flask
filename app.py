from flask import Flask
from controllers import chapter1


app = Flask(__name__)


@app.route('/')
def main():
    return chapter1.index_html()


@app.route('/departures/<departure>/')
def departures(departure):
    return chapter1.departure_html(departure)


@app.route('/tours/<id>/')
def tours(id):
    return chapter1.tour_html(id)


@app.route('/data/')
def data():
    return chapter1.data_html()


@app.route('/data/departures/<departure>/')
def data_departures(departure):
    return chapter1.data_departures_html(departure)


@app.route('/data/tours/<id>/')
def data_tours(id):
    return chapter1.data_tours_html(id)


if __name__ == '__main__':
    app.run()
