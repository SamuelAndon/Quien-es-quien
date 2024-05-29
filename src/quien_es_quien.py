from pyswip import Prolog
import random
from collections import Counter

prolog = Prolog()
prolog.consult('quien_es_quien.pl')

# Obtenemos la lista de personajes y con el random seleccionamos uno aleatorio
def personaje_objetivo():
    personaje = list(prolog.query("personaje(Nombre, Caracteristicas)"))
    personaje_objetivo = random.choice(personaje)
    return personaje_objetivo

# Mostramos el tablero con personajes actuales
def mostrar_tablero():
    personajes = list(prolog.query("personaje(Nombre, Caracteristicas)"))
    for p in personajes:
        nombre = p["Nombre"]
        caracteristicas = p["Caracteristicas"]
        print(f"Nombre: {nombre}, Caracteristicas: {caracteristicas}")

# Obtenemos una lista con el número de veces que se repite cada caracteristica y seleccionamos la del medio.
def caracteristica_a_preguntar():
    lista_caracteristicas = []
    caracteristicas = list(prolog.query("personaje(_,Caracteristicas)"))
    for c in caracteristicas:
        for ca in c['Caracteristicas']:
            lista_caracteristicas.append(ca)
    frecuencia_cada_caracteristica = Counter(lista_caracteristicas)
    frecuencia_cada_caracteristica = sorted(frecuencia_cada_caracteristica.items(), key=lambda i: i[1], reverse=True)
    print(frecuencia_cada_caracteristica)
    caracteristica_a_preguntar = frecuencia_cada_caracteristica[int(len(frecuencia_cada_caracteristica)/2)][0]
    return caracteristica_a_preguntar

def main():
    objetivo = personaje_objetivo()
    objetivo_sin_adivinado = True
    print(objetivo)
    mostrar_tablero()
    
    while objetivo_sin_adivinado:
        caract_a_preguntar = caracteristica_a_preguntar()
        print(f"El personaje tiene {caract_a_preguntar} ?")

main()