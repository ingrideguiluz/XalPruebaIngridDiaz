import requests
from requests.models import Response

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

    print(f"Número de respuestas contestadas: {contador_true}")
    print(f"Número de respuestas no contestadas: {contador_false}")   

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
    response = requests.get(url)
    data: dict = response.json()
    menor_vista = []
    for element in data["items"]:
        menor = element["view_count"]
        menor_vista.append(menor)

    print(f"Respuesta con menor número de vistas: {min(menor_vista)}")

#5. Obtener la respuesta más vieja y más actual
def respuestas():
    response = requests.get(url)
    data: dict = response.json()
    respuestas = []
    for element in data["items"]:
        valor_respuesta = element["creation_date"]
        respuestas.append(valor_respuesta)

    #Imprimir la respuesta más vieja
    print(f"La fecha de la respuesta más vieja es: {max(respuestas)}") 
    #Imprimir la respuesta mas reciente
    print(f"La fecha de la respuesta más reciente es: {min(respuestas)}")   

def run():
    muestra_url(url)
    valor_de_respuestas()
    mayor_owners()
    menor_numero_vistas()
    respuestas()

        
if __name__ == '__main__':
    run()




    