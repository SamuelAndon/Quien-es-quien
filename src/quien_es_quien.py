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

# Obtenemos la caracteristica que más se repite
def caracteristica_mas_habitual():
    caracteristicas = list(prolog.query("personaje(_,Caracteristicas)"))
    lista_caracteristicas = [caracteristica for c in caracteristicas for caracteristica in c['Caracteristicas']]
    frecuencia_cada_caracteristica = Counter(lista_caracteristicas)
    mas_habitual = frecuencia_cada_caracteristica.most_common(1)
    return mas_habitual

def main():
    print(personaje_objetivo())
    mostrar_tablero()
    print(caracteristica_mas_habitual())
    

main()