#Encuentro de vuelos baratos a partir de una base de datos (se creará una base de datos
#ficticia usando un archivo de texto o directamente una estructura que la simule dentro
#del mismo programa que desarrollará)
"""
encuentro_vuelos.py
Ejemplo: búsqueda de vuelos baratos usando Dijkstra
Requisitos: pip install networkx
"""

import networkx as nx

# Simulación de la base de datos de vuelos (puedes reemplazar por lectura de archivo)
# Formato: (origen, destino, precio, duracion_minutos)
vuelos = [
    ("Quito", "Guayaquil", 80, 55),
    ("Quito", "Cuenca", 60, 40),
    ("Cuenca", "Guayaquil", 50, 45),
    ("Quito", "Loja", 120, 120),
    ("Loja", "Guayaquil", 70, 60),
    ("Cuenca", "Loja", 90, 80),
]

# Construcción del grafo dirigido
G = nx.DiGraph()
for origen, destino, precio, duracion in vuelos:
    G.add_edge(origen, destino, price=precio, time=duracion)

def encontrar_vuelo_mas_barato(G, origen, destino):
    try:
        # Usamos Dijkstra con el peso = precio
        ruta = nx.dijkstra_path(G, origen, destino, weight="price")
        costo = nx.dijkstra_path_length(G, origen, destino, weight="price")

        # Calcular duración total
        duracion_total = 0
        for i in range(len(ruta) - 1):
            datos = G[ruta[i]][ruta[i+1]]
            duracion_total += datos["time"]

        return ruta, costo, duracion_total
    except nx.NetworkXNoPath:
        return None, float("inf"), None

# Ejemplo de búsqueda
origen = "Quito"
destino = "Guayaquil"

ruta, costo, duracion = encontrar_vuelo_mas_barato(G, origen, destino)

if ruta:
    print(f"Ruta más barata de {origen} a {destino}: {' -> '.join(ruta)}")
    print(f"Costo total: ${costo}")
    print(f"Duración total: {duracion} minutos")
else:
    print(f"No existe una ruta entre {origen} y {destino}")
