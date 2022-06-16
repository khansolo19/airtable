from settings import settings
import requests



def list_records():
    """ Метод для получения всех объектов """
    URL = '?maxRecords=3&view=Grid%20view'
    req = requests.get(
        url=settings.get_url()+URL,
        headers={'Authorization': settings.TOKEN}
        )
    return req.text

def retrieve_record(id_):
    """ Метод для получения одного объекта """
    req = requests.get(
        settings.get_url()+id_, 
        headers={'Authorization': settings.TOKEN}
        )
    return req.text

# print(list_records())
print(retrieve_record('rec7DxpWyh31c7j5J'))