import math

# Función para calcular la distancia entre dos puntos en la superficie terrestre
def calcular_distancia(lat1, lon1, lat2, lon2):
    R = 6371  # Radio de la Tierra en kilómetros
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distancia_km = R * c
    distancia_millas = distancia_km * 0.621371
    return distancia_km, distancia_millas

# Función para calcular la duración del viaje
def calcular_duracion(distancia_km, velocidad_km_h):
    duracion_horas = distancia_km / velocidad_km_h
    return duracion_horas

# Función para mostrar la narrativa del viaje
def mostrar_narrativa(ciudad_origen, ciudad_destino, distancia_km, duracion_horas, medio_transporte):
    print(f"Usted va a viajar desde {ciudad_origen} hasta {ciudad_destino}.")
    print(f"La distancia entre ambas ciudades es de {distancia_km:.2f} kilómetros.")
    print(f"El viaje durará aproximadamente {duracion_horas:.2f} horas en {medio_transporte}.")

# Ciudades y sus coordenadas geográficas
ciudades = {
    "Santiago de Chile": (-33.45, -70.67),
    "Buenos Aires": (-34.60, -58.38),
    "Mendoza": (-32.89, -68.84),
    "Córdoba": (-31.42, -64.18),
    # Agregar más ciudades aquí
}

# Programa principal
while True:
    print("Seleccione la ciudad de origen:")
    for i, ciudad in enumerate(ciudades.keys()):
        print(f"{i+1}. {ciudad}")
    origen = input("Ingrese el número de la ciudad de origen: ")
    ciudad_origen = list(ciudades.keys())[int(origen) - 1]

    print("Seleccione la ciudad de destino:")
    for i, ciudad in enumerate(ciudades.keys()):
        print(f"{i+1}. {ciudad}")
    destino = input("Ingrese el número de la ciudad de destino: ")
    ciudad_destino = list(ciudades.keys())[int(destino) - 1]

    lat1, lon1 = ciudades[ciudad_origen]
    lat2, lon2 = ciudades[ciudad_destino]

    distancia_km, distancia_millas = calcular_distancia(lat1, lon1, lat2, lon2)

    print("Seleccione el medio de transporte:")
    print("1. Avión")
    print("2. Automóvil")
    print("3. Autobús")
    medio_transporte = input("Ingrese el número del medio de transporte: ")

    if medio_transporte == "1":
        velocidad_km_h = 800  # Velocidad promedio de un avión
    elif medio_transporte == "2":
        velocidad_km_h = 100  # Velocidad promedio de un automóvil
    elif medio_transporte == "3":
        velocidad_km_h = 60  # Velocidad promedio de un autobús
    else:
        print("Opción inválida. Saliendo...")
        break

    duracion_horas = calcular_duracion(distancia_km, velocidad_km_h)

    mostrar_narrativa(ciudad_origen, ciudad_destino, distancia_km, duracion_horas, medio_transporte)

    salir = input("¿Desea salir? (s/n): ")
    if salir.lower() == "s":
        break