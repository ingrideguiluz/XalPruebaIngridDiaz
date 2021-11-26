import requests
from requests.api import request
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
        if("owner" in element and "user_id" in element["owner"] and element["owner"]["user_id"] is not None): 
            maximos = element["owner"]["user_id"]
        else:
            maximos = 0
        elementos_maximos.append(maximos) 

    print(f"Respuesta con mayor owner: {max(elementos_maximos)}") 

#4. Obtener la respuesta con menor número de 
def menor_numero_vistas():
    response = request.get(url)
    data: dict = response.json()
    menor_vista = []
    for element in data["items"]:
        menor = element["view_count"]
        menor_vista.append(menor)
    print(f"Respuesta con menor numero de vistas {min(menor_vista)}")

#5. Obtener la respuesta más vieja y más actual
def respuestas():
    response = request.get(url)
    data: dict = response.json()
    respuestas = []
    for element in data["items"]:
        valor_respuesta = element["answer_count"]
        respuestas.append(valor_respuesta)
    #Imprimir la respuesta más vieja
    print(f"Respuesta mas vieja {min(respuestas)}") 
    #Imprimir la respuesta mas reciente
    print(f"Respuesta mas reciente {max(respuestas)}")   
