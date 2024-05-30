from pyswip import Prolog
import random
from collections import Counter

prolog = Prolog()
prolog.consult('quien_es_quien.pl')

# Obtenemos la lista de personajes y con el random seleccionamos uno aleatorio siendo el personaje objetivo
def personaje_objetivo():
    personajes = list(prolog.query("personaje(Nombre, Caracteristicas)"))
    personaje_objetivo = random.choice(personajes)
    return personaje_objetivo

# Mostramos el tablero con los personajes actuales
def mostrar_tablero(personajes):
    for personaje in personajes:
        nombre = personaje["Nombre"]
        caracteristicas = personaje["Caracteristicas"]
        print(f"Nombre: {nombre}, Caracteristicas: {caracteristicas}")

# Obtenemos una lista con el número de veces que se repite cada caracteristica y seleccionamos la del medio.
def caracteristica_a_preguntar(personajes):
    lista_caracteristicas = []
    
    for personaje in personajes:
        for caracteristica in personaje['Caracteristicas']:
            lista_caracteristicas.append(caracteristica)

    frecuencia_cada_caracteristica = Counter(lista_caracteristicas)
    frecuencia_cada_caracteristica = sorted(frecuencia_cada_caracteristica.items(), key=lambda i: i[1], reverse=True)
    caracteristica_a_preguntar = frecuencia_cada_caracteristica[int(len(frecuencia_cada_caracteristica)/2)][0]
    return caracteristica_a_preguntar

# Con el método sabemos si el personaje objetivo tiene la caracteristica a preguntar
def preguntar_la_caracteristica(nombre, caracteristica):
    caracteristicas_personaje_objetivo = list(prolog.query(f"personaje('{nombre}', Caracteristicas)"))
    if caracteristica in caracteristicas_personaje_objetivo[0]["Caracteristicas"]:
        return True
    return False

def main():
    personajes = list(prolog.query("personaje(Nombre, Caracteristicas)"))
    objetivo = personaje_objetivo()
    print(f"Personaje objetivo --> {objetivo}")
    contador_preguntas = 0
    
    while len(personajes) > 1:
        contador_preguntas += 1
        print("Personajes actuales")
        mostrar_tablero(personajes)
        caract_a_preguntar = caracteristica_a_preguntar(personajes)
        print(f"El personaje tiene {caract_a_preguntar}?")
        tiene = preguntar_la_caracteristica(objetivo["Nombre"], caract_a_preguntar)
        lista_temp = []
        if tiene:
            print('SI')
            for personaje in personajes:
                if caract_a_preguntar in personaje["Caracteristicas"]:
                    lista_temp.append(personaje)
        else:
            print('NO')
            for personaje in personajes:
                if caract_a_preguntar not in personaje["Caracteristicas"]:
                    lista_temp.append(personaje)

        personajes = lista_temp
        if len(personajes) == 1:
            print(f"El personaje es {personajes}")
    print(f"El personaje fue adivinado en {contador_preguntas} preguntas")
main()