import data as tours_data


def data_html():
    ret = "<h1>Все туры:</h1>"+"\n"
    for i in tours_data.tours.keys():
        ret = ret + "<p>"+\
              tours_data.tours[i]["country"]+\
              ': <a href="/data/tours/'+str(i)+'/">'+\
              tours_data.tours[i]["title"]+\
              "</a></p>"
    return ret
