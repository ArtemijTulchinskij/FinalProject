import requests
from configuration import URL_SERVER, CREATE_ORDER, GET_ORDER_TRACK
from data import CREATE_ORDER_PAYLOAD

def create_order():
    response = requests.post(URL_SERVER + CREATE_ORDER, json=CREATE_ORDER_PAYLOAD)
    return response

def get_order_by_track(track):
    params = {"t": track}
    response = requests.get(URL_SERVER + GET_ORDER_TRACK, params=params)
    return response
