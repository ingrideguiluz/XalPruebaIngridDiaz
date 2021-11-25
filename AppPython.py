import requests
from requests.models import Response
from requests.sessions import _Data

url="https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"

#1. Conectarse al enlace
def muestra_url(url):
    response = requests.get(url)
    respuesta = response.json()
    #print('INSUMO -->', respuesta)
    return respuesta #Imprime el insumo json

#2. Obtener el número de respuestas contestadas y no contestadas
def valor_de_respuestas():
    response = requests.get(url)
    data: dict = response.json()

    contador_true: int = 0
    contador_false: int = 0
    for element in data["items"]:
        respuestas = element["is_answered"]
        if respuestas == True:
            contador_true = contador_true + 1
        elif respuestas == False:
            contador_false = contador_false + 1
    print(f"numero de respuestas contestadas: {contador_true}")
    print|(f"numero de respuestas no contestadas: {contador_false}")   

#3. Obtener la respuesta con mayor owners
def mayor_owners():
    response = requests.get(url)
    data: dict = response.json()
    elementos_maximos = []
    for element in data["items"]:
        maximos = element["owner"]["reputation"]
        elementos_maximos.append(maximos) 

    print(f"Respuesta con mayor owner: {max(elementos_maximos)}")     