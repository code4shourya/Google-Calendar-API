import requests 

endpoint1 = "http://127.0.0.1:8000/rest/v1/calendar/init"
endpoint2 = "http://127.0.0.1:8000/rest/v1/calendar/redirect"


get_responce = requests.get(endpoint1)
print(get_responce.json())
print(get_responce.status_code)


get_responce = requests.get(endpoint2)
print(get_responce.json())
print(get_responce.status_code)
