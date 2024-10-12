# Este proyecto de grafo no solo permite representar y recorrer grafos,
# sino también realizar cálculos importantes como la distancia más barata entre 
# dos nodos o el análisis de los pesos de los arcos. 

#Modulo de prueba del Grafo
from Grafo import GrafoListaConPesos

# Crear el grafo
grafo1 = GrafoListaConPesos()

# Adicionar vértices
grafo1.adicionarVertice("Buenavista")
grafo1.adicionarVertice("Viva")
grafo1.adicionarVertice("Universidad De La Costa")
grafo1.adicionarVertice("Parque Alegra")
grafo1.adicionarVertice("Portal Del Prado")
grafo1.adicionarVertice("Villa Contri")
grafo1.adicionarVertice("Unico")
grafo1.adicionarVertice("Panorama")
grafo1.adicionarVertice("Gran Centro")
grafo1.adicionarVertice("Plaza Campestre")


# Adicionar arcos
grafo1.adicionarArco("Universidad De La Costa", "Buenavista", 3000)
grafo1.adicionarArco("Universidad De La Costa", "Viva", 2800)
grafo1.adicionarArco("Universidad De La Costa", "Parque Alegra", 4000)
grafo1.adicionarArco("Buenavista", "Unico", 2500)
grafo1.adicionarArco("Buenavista", "Gran Centro", 3000)
grafo1.adicionarArco("Buenavista", "Villa Contri", 2000)
grafo1.adicionarArco("Parque Alegra", "Portal Del Prado", 3500)
grafo1.adicionarArco("Parque Alegra", "Panorama", 2800)
grafo1.adicionarArco("Parque Alegra", "Plaza Campestre", 2200)
grafo1.adicionarArco("Viva", "Plaza Campestre", 2000)
grafo1.adicionarArco("Viva", "Portal Del Prado", 3000)
grafo1.adicionarArco("Viva", "Unico", 2300)
grafo1.adicionarArco("Portal Del Prado", "Villa Contri", 2000)

# Imprimir el grafo
print("El grafo es:\n", grafo1, sep="")
print("_____________________________________________________________________________________")

# Imprimir el recorrido BFS 
print("Recorrido en anchura (BFS) desde Parque Alegra:", grafo1.recorrerAnchura("Parque Alegra"))
print("_____________________________________________________________________________________")

# Calcular e imprimir el camino más barato (menor peso) 
camino, precio = grafo1.caminoMasCorto("Universidad De La Costa", "Plaza Campestre")
print("\nEl camino más barato de La Universidad De La Costa hasta Parque Campestre es:", camino)
print("La distancia más corta es:", precio)
print("_____________________________________________________________________________________")

# Imprimir el recorrido DFS desde
print("\nRecorrido en profundidad (DFS) desde Universidad De La Costa:", grafo1.recorrerProfundidad("Universidad De La Costa"))
print("_____________________________________________________________________________________")

# Contar la suma de los pesos
suma_pesos = grafo1.contarPesos()
print("La suma de los precios es:", suma_pesos)
print("_____________________________________________________________________________________")

# Imprimir el peso promedio
print("Peso promedio de los arcos en el grafo:", grafo1.pesoPromedio())
print("_____________________________________________________________________________________")

# Imprimir el arco con mayor peso
arco_mayor = grafo1.arcoMayorPeso()
print("Arco con mayor peso:", arco_mayor)
print("_____________________________________________________________________________________")

# Imprimir el arco con menor peso
arco_menor = grafo1.arcoMenorPeso()
print("Arco con menor peso:", arco_menor)
print("_____________________________________________________________________________________")

#Imprimir la obtencion del peso del arco 
peso = grafo1.obtenerPesoArco("Buenavista", "Gran Centro")
print("\nPeso del arco entre Buenavista y Gran Centro:", peso)
print("_____________________________________________________________________________________")

resultado = grafo1.esArcoParOImpar('Buenavista', 'Villa Contri')
print(resultado)
print("_____________________________________________________________________________________")
