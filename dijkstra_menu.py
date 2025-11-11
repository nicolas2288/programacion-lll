# ALGORITMO DE DIJKSTRA
// Este programa permite crear un grafo con 6 nodos
// y calcular las rutas más cortas desde un nodo inicial

// Importa la librería heapq para usar una cola de prioridad (min-heap)
import heapq  # Librería para manejar colas de prioridad 

// Clase que representa el Grafo
class Grafo:
    
 // Constructor de la clase Grafo
    def __init__(self):
    // Diccionario donde cada nodo tendrá una lista de sus conexiones 
        self.nodos = {}

    // Método para agregar una conexión entre dos nodos con un peso
    def agregar_arista(self, origen, destino, peso):
        // Si el nodo origen no existe aún, crear su entrada en el diccionario
        if origen not in self.nodos:
            self.nodos[origen] = []
        // Si el nodo destino no existe aún, crear su entrada en el diccionario
        if destino not in self.nodos:
            self.nodos[destino] = []
        // Agregar la conexión del origen al destino con el peso indicado
        self.nodos[origen].append((destino, peso))
        // Agregar la conexión del destino al origen (grafo no dirigido)
        self.nodos[destino].append((origen, peso))

    // Algoritmo de Dijkstra para encontrar caminos más cortos desde 'inicio'
    def dijkstra(self, inicio):
        // Crear un diccionario de distancias e inicializar todas a infinito
        distancias = {nodo: float('inf') for nodo in self.nodos}
        // La distancia desde el inicio a sí mismo es 0
        distancias[inicio] = 0  # La distancia del inicio a sí mismo es 0
        Cola de prioridad (min-heap) que guarda tuplas (distancia, nodo)
        cola_prioridad = [(0, inicio)]
        // Mientras la cola no esté vacía, seguimos procesando nodos
        while cola_prioridad:
            // Sacar el elemento con menor distancia conocida
            distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

            // Si la distancia sacada es mayor a la ya guardada, la ignoramos
            if distancia_actual > distancias[nodo_actual]:
                continue

            // Recorremos cada vecino del nodo actual
            for vecino, peso in self.nodos[nodo_actual]:
                // Calculamos la distancia pasando por el nodo actual al vecino
                distancia_nueva = distancia_actual + peso
                // Si la nueva distancia es mejor que la almacenada, la actualizamos
                if distancia_nueva < distancias[vecino]:
                  distancias[vecino] = distancia_nueva
                // Insertamos en la cola la nueva distancia para procesarla luego
                    heapq.heappush(cola_prioridad, (distancia_nueva, vecino))

        // Devolvemos el diccionario con las distancias mínimas encontradas
        return distancias

// Función principal del programa
def main():
    # Crear el grafo donde guardaremos las aristas y nodos
    grafo = Grafo()
    # Agregar las aristas con sus pesos 
    grafo.agregar_arista(1, 2, 2)
    grafo.agregar_arista(1, 3, 1)
    grafo.agregar_arista(2, 4, 1)
    grafo.agregar_arista(3, 4, 2)
    grafo.agregar_arista(4, 5, 2)
    grafo.agregar_arista(5, 6, 3)
    grafo.agregar_arista(3, 6, 4)

    # Bucle principal que muestra el menú hasta que el usuario decida salir
    while True:
        # Mostrar las opciones disponibles en pantalla
        print("\n--- MENÚ ---")
        print("1. Mostrar todas las conexiones del grafo")
        print("2. Calcular el camino más corto desde un nodo")
        print("3. Salir")

        // Leer la opción elegida por el usuario
        opcion = input("Seleccione una opción: ")

        // Si el usuario elige la opción 1: mostramos las conexiones
        if opcion == "1":
            # Mensaje encabezado para la lista de conexiones
            print("\nConexiones del grafo:")
            // Recorrer el diccionario de nodos e imprimir cada entrada
            for nodo, vecinos in grafo.nodos.items():
                print(f"{nodo} -> {vecinos}")

        // Si el usuario elige la opción 2: calcular caminos más cortos
        elif opcion == "2":
            try:
                // Pedir al usuario el número del nodo inicial y convertirlo a entero
                inicio = int(input("Ingrese el número del nodo inicial (1-6): "))

                // Comprobar que el nodo ingresado exista en el grafo
                if inicio not in grafo.nodos:
                    # Si no existe, informar y volver al menú
                    print("Ese nodo no existe. Intente con uno del 1 al 6.")
                    continue

                // Ejecutar Dijkstra para obtener las distancias desde 'inicio'
                distancias = grafo.dijkstra(inicio)
                # Mostrar los resultados en pantalla
                print(f"\nDistancias más cortas desde el nodo {inicio}:")
                for nodo, distancia in distancias.items():
                    print(f"  Hasta {nodo}: {distancia}")

            /7 Capturar el error si el usuario no ingresa un número válido
            except ValueError:
                print("Debe ingresar un número válido.")

        // Si el usuario elige la opción 3: salir del programa
        elif opcion == "3":
            # Mensaje de cierre personalizado 
            print("Fin del programa. Desarrollado por Nicolás Carabalí.")
            # Romper el bucle y terminar la ejecución
            break

        // Si la opción no es 1, 2 ni 3, mostramos mensaje de error
        else:
            print("Opción no válida. Intente de nuevo.")

// EJECUCIÓN DEL PROGRAMA: este bloque ejecuta main() al correr el archivo
if __name__ == "__main__":
    main()
