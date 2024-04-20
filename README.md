# Quien-es-quien
Práctica del curso de especialización de Inteligencia Artificial y Big Data - IES de Teis

## Preguntas a desarrollar

 * [1. Optimización vs Búsquedas](#1-optimización-vs-búsquedas)
 * [2. Entorno del agente](#2-entorno-del-agente)
 * [3. Algoritmo](#3-algoritmo)
 * [4. Estrutura del agente](#4-estrutura-del-agente)
 * [5. Programación lógica](#5-programación-lógica)
 * [6. Base de datos Prolog](#6-base-de-datos-prolog)

## 1. Optimización vs Búsquedas

El **quien es quien** se puede considerar un problema de optimización, ya que un problema de optimización es aquel que busca encontrar el mejor estado posible según una función objetivo. 

En este caso el juego consiste en encontrar el personaje que seleccionó la otra persona lo antes posible, con lo cual tendriamos que buscar las mejores preguntas para reducir las opciones y encontrar el personaje lo antes posible.

Siendo el mejor estado el conocimiento de la mayor cantidad de información para adivinar el personaje usando las menos preguntas posibles, y la función objetivo es usar las mínimas preguntas para encontrarlo.

Por eso el **quien es quien** es un problema de optimización y no de búsqueda, ya que en este caso buscamos obtener el personaje objetivo con las mínimas preguntas sin la necesidad de hacer una búsqueda completa.

## 2. Entorno del agente

Entorno de tareas | Completamente / parcialmente Observable| Agentes | Determinista / Estocástico | Episódico / Secuencial | Estático / Dinámico | Discreto / Continuo
:---: | :---: | :---: | :---: | :---: | :---: | :---: |
 Quien es quien | Parcialmente observable | Multiagente | Determinista | - | Estático |  Discreto |

- **Parcialmente observable:** A la hora de empezar el juego el personaje que se debe adivinar es una carta que coje nuestro adversario de forma aleatoria. Con lo cual a medida que pasa el juego nosotros solo podemos observar los personajes que descartamos y los que nos quedan como posibles opciones en nuestro tablero, pero no podemos observar las distintas caracteristicas del personaje objetivo, ni el tablero del adversario para saber las opciones que le quedan.

- **Multiagente:** Mientras está en proceso la partida es necesario la interacción de otro agente, a la hora de realizar preguntas y responderlas para continuar en la búsqueda del personaje que tenemos que adivinar.

- **Determinista:** Puede parecer estocástico ya que al inicio del juego el personaje se coje de forma aleatoria, pero es determinista, ya que en el proceso del juego las preguntas que se realizan tienen respuestas fijas "si" o "no", no existe aleatoriedad en ellas.

- **Secuencial** 

- **Estático** Se trata de un entorno estático ya que mientras se están realizando las preguntas, el entorno no se modifica, como tampoco lo hace el tablero ni el personaje objetivo.

- **Discreto** Se trata de un agente discreto ya que tiene un número finito de estados. A la hora de seleccionar el personaje, se escoje de una baraja que contiene un número limitado de personajes, además, a la hora de realizar las preguntas también hay un numero limitado, ya que depende de las caracteristicas de los personajes anteriores. Y por último, las respuestas también son limitadas ya que solo pueden ser "si" o "no".

## 3. Algoritmo.


## Bibliografía

- Russell, Peter. _ARTIFICIAL INTELLIGENCE : A Modern Approach_, Global Edition. S.L., Pearson Education Limited, 2021.
- @dfleta. "quienesquien". _github_. https://github.com/dfleta/quienesquien