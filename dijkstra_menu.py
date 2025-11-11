# ---------------------------------------------
# PROGRAMA: Algoritmo de Dijkstra (Ejemplo del grafo de la imagen)
# Autor: Nicolás
# Materia: Programación III
# Descripción:
# Este programa implementa el algoritmo de Dijkstra
# para encontrar el camino más corto entre nodos numerados (1 a 6)
# tal como el grafo mostrado en la imagen del ejemplo.
# ---------------------------------------------

import heapq  # Librería para usar colas de prioridad (elige el menor camino automáticamente)

# Clase Grafo: representa el conjunto de nodos y conexiones (aristas)
class Grafo:
    def __init__(self):
        # Diccionario: cada nodo guarda una lista de vecinos con el peso (distancia)
        self.nodos = {}

    def agregar_nodo(self, nodo):
        if nodo not in self.nodos:
            self.nodos[nodo] = []

    def agregar_arista(self, origen, destino, peso):
        self.agregar_nodo(origen)
        self.agregar_nodo(destino)
        # Se agrega conexión ida y vuelta
        self.nodos[origen].append((destino, peso))
        self.nodos[destino].append((origen, peso))

    # Algoritmo de Dijkstra
    def dijkstra(self, inicio):
        # Distancias iniciales: todas son infinitas excepto el nodo de inicio (0)
        distancias = {nodo: float('inf') for nodo in self.nodos}
        distancias[inicio] = 0

        # Cola de prioridad con (distancia, nodo)
        cola = [(0, inicio)]

        while cola:
            distancia_actual, nodo_actual = heapq.heappop(cola)

            # Si ya hay una mejor distancia guardada, se ignora
            if distancia_actual > distancias[nodo_actual]:
                continue

            # Recorre los vecinos del nodo actual
            for vecino, peso in self.nodos[nodo_actual]:
                nueva_distancia = distancia_actual + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    heapq.heappush(cola, (nueva_distancia, vecino))

        return distancias



# FUNCIÓN PRINCIPAL
def main():
    grafo = Grafo()
    # 1 → 2 (2)
    grafo.agregar_arista(1, 2, 2)
    # 1 → 3 (1)
    grafo.agregar_arista(1, 3, 1)
    # 2 → 4 (1)
    grafo.agregar_arista(2, 4, 1)
    # 4 → 6 (2)
    grafo.agregar_arista(4, 6, 2)
    # 4 → 3 (3)
    grafo.agregar_arista(4, 3, 3)
    # 3 → 5 (4)
    grafo.agregar_arista(3, 5, 4)
    # 5 → 6 (2)
    grafo.agregar_arista(5, 6, 2)

    print("===== ALGORITMO DE DIJKSTRA =====")
    print("Grafo cargado con los nodos (1 al 6) del ejemplo.\n")

# Bucle principal del programa que muestra el menú continuamente
while True:
    print("\n--- MENÚ ---")
    print("1. Mostrar todas las conexiones del grafo")
    print("2. Calcular el camino más corto desde un nodo")
    print("3. Salir")

    # El usuario elige una opción del menú
    opcion = input("Seleccione una opción: ")

    # Opción 1: Mostrar las conexiones del grafo (todos los nodos y sus vecinos)
    if opcion == "1":
        print("\nConexiones del grafo:")
        for nodo, vecinos in grafo.nodos.items():
            # Muestra cada nodo y las conexiones que tiene (sus vecinos)
            print(f"{nodo} -> {vecinos}")

    # Opción 2: Calcular los caminos más cortos desde un nodo inicial
    elif opcion == "2":
        try:
            # Se pide al usuario el número del nodo de inicio
            inicio = int(input("Ingrese el número del nodo inicial (1-6): "))

            # Si el nodo no existe en el grafo, se muestra un mensaje de error
            if inicio not in grafo.nodos:
                print(" Ese nodo no existe.")
                continue  # vuelve al menú

            # Se aplica el algoritmo de Dijkstra desde el nodo inicial
            distancias = grafo.dijkstra(inicio)

            # Se muestran las distancias más cortas desde el nodo elegido
            print(f"\nDistancias más cortas desde el nodo {inicio}:")
            for nodo, distancia in distancias.items():
                print(f"  Hasta {nodo}: {distancia}")

        # Si el usuario ingresa algo que no es número, muestra error
        except ValueError:
            print(" Debe ingresar un número válido.")

    # Opción 3: salir del programa
    elif opcion == "3":
        print(" Programa finalizado.")
        break  # termina el ciclo y finaliza el programa

    # Si el usuario escribe otra cosa que no es 1, 2 o 3
    else:
        print(" Opción no válida. Intente de nuevo.")

# EJECUCIÓN DEL PROGRAMA
# Este bloque asegura que el programa se ejecute correctamente al iniciar
if __name__ == "__main__":
    main()
