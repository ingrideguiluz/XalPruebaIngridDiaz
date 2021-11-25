import requests

url="https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"

#1. Conectarse al enlace
def muestra_url(url):
    response = requests.get(url)
    respuesta = response.json()
    #print('INSUMO -->', respuesta)
    return respuesta #Imprime el insumo json

