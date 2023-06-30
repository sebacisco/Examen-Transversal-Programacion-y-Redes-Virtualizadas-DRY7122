import requests
import urllib.parse
def obtener_distancia(ciudad_origen, ciudad_destino):
    api_key = "FX7ovwFThdMnD2jLURQM43dLRGGSmVp5" 
    url = f"http://www.mapquestapi.com/directions/v2/route?key={api_key}&from={ciudad_origen}&to={ciudad_destino}"
    response = requests.get(url)
    data = response.json()
    distancia = data["route"]["distance"]
    return round(distancia, 3)

def calcular_duracion(distancia, velocidad_promedio=80):
    tiempo_en_horas = distancia / velocidad_promedio
    minutos_totales = tiempo_en_horas * 60
    horas = int(minutos_totales // 60)
    minutos = int(minutos_totales % 60)
    segundos = int((minutos_totales % 1) * 60)
    return horas, minutos, segundos

def calcular_combustible(distancia, rendimiento_vehiculo=12):
    combustible_requerido = distancia / rendimiento_vehiculo
    return round(combustible_requerido, 3)

def obtener_narrativa(ciudad_origen, ciudad_destino, distancia, duracion, combustible):
    return f"Viaje desde {ciudad_origen} hasta {ciudad_destino}:\n" \
           f"- Distancia: {distancia} km\n" \
           f"- Duración estimada del viaje: {duracion[0]:02d} horas, {duracion[1]:02d} minutos, {duracion[2]:02d} segundos\n" \
           f"- Combustible requerido: {combustible} lts\n" \
           f"¡Buen viaje!"

ciudad_origen = input("Ciudad de Origen: ")
ciudad_destino = input("Ciudad de Destino: ")

distancia = obtener_distancia(ciudad_origen, ciudad_destino)

duracion = calcular_duracion(distancia)
combustible = calcular_combustible(distancia)

narrativa = obtener_narrativa(ciudad_origen, ciudad_destino, distancia, duracion, combustible)

print(narrativa)

letra_salida = 'Q'

while True:
    entrada = input("Ingresa una letra (Q para salir): ")
    
    if entrada.upper() == letra_salida:
        print("Programa finalizado.")
        break
    else:
        print("Has ingresado la letra:", entrada)es_grupo:
    print(integrante)
