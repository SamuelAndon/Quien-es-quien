import pytest
from pyswip import Prolog
from src.quien_es_quien import personaje_objetivo, mostrar_tablero, caracteristica_a_preguntar, preguntar_la_caracteristica

prolog = Prolog()
prolog.consult('src/quien_es_quien.pl')

@pytest.mark.eleccion
def test_personaje_objetivo():
    personajes = list(prolog.query("personaje(Nombre, Caracteristicas)"))
    p_objetivo = personaje_objetivo()

    if p_objetivo in personajes:
        assert True

@pytest.mark.mostrar
def test_mostrar_tablero(capfd):
    personajes = list(prolog.query("personaje(Nombre, Caracteristicas)"))

    mostrar_tablero(personajes)

    salida_metodo, err = capfd.readouterr()

    salida_esperada = """Nombre: herman, Caracteristicas: ['hombre', 'pelirrojo', 'calva', 'nariz_grande', 'ojos_marrones', 'cejas_gruesas']
Nombre: maria, Caracteristicas: ['mujer', 'pelo_largo', 'sombrero', 'pendientes', 'pelo_castanho', 'ojos_marrones', 'boca_pequenha', 'cejas_finas', 'nariz_pequenha']
Nombre: claire, Caracteristicas: ['mujer', 'gafas', 'sombrero', 'pelirrojo', 'ojos_marrones', 'boca_pequenha', 'nariz_pequenha']
Nombre: charles, Caracteristicas: ['hombre', 'bigote', 'pelo_rubio', 'ojos_marrones', 'labios_gruesos', 'boca_grande', 'orejas_grandes', 'raya_al_lado', 'nariz_pequenha']
Nombre: richard, Caracteristicas: ['hombre', 'calva', 'barba', 'ojos_marrones', 'orejas_grandes', 'bigote', 'cara_alargada', 'nariz_pequenha']
Nombre: eric, Caracteristicas: ['hombre', 'pelo_rubio', 'gorra', 'sombrero', 'ojos_marrones', 'boca_grande', 'nariz_pequenha']
Nombre: alex, Caracteristicas: ['hombre', 'bigote', 'pelo_negro', 'ojos_marrones', 'boca_grande', 'labios_gruesos', 'orejas_grandes', 'pelo_corto', 'nariz_pequenha']
Nombre: peter, Caracteristicas: ['hombre', 'canas', 'pelo_blanco', 'nariz_grande', 'ojos_azules', 'cejas_gruesas', 'labios_gruesos', 'boca_grande', 'raya_al_lado']
Nombre: philip, Caracteristicas: ['hombre', 'barba', 'pelo_negro', 'ojos_marrones', 'orejas_grandes', 'mofletes', 'mejillas_sonrosadas', 'cejas_finas', 'pelo_corto', 'nariz_pequenha']
Nombre: joe, Caracteristicas: ['hombre', 'gafas', 'pelo_rubio', 'ojos_marrones', 'boca_pequenha', 'pelo_corto', 'nariz_pequenha']
Nombre: paul, Caracteristicas: ['hombre', 'gafas', 'pelo_blanco', 'canas', 'ojos_marrones', 'boca_pequenha', 'orejas_grandes', 'cejas_gruesas', 'raya_al_lado', 'nariz_pequenha']
Nombre: david, Caracteristicas: ['hombre', 'barba', 'pelo_rubio', 'ojos_marrones', 'orejas_grandes', 'raya_al_lado', 'nariz_pequenha']
Nombre: george, Caracteristicas: ['hombre', 'cara_triste', 'sombrero', 'pelo_blanco', 'canas', 'ojos_marrones', 'boca_grande', 'nariz_pequenha']
Nombre: frans, Caracteristicas: ['hombre', 'pelo_corto', 'cejas_gruesas', 'pelirrojo', 'ojos_marrones', 'boca_pequenha', 'nariz_pequenha']
Nombre: alfred, Caracteristicas: ['hombre', 'bigote', 'barba', 'pelirrojo', 'ojos_azules', 'boca_pequenha', 'orejas_grandes', 'pelo_largo', 'raya_al_medio', 'nariz_pequenha']
Nombre: bernard, Caracteristicas: ['hombre', 'pelo_castanho', 'sombrero', 'ojos_marrones', 'boca_pequenha', 'cejas_finas', 'nariz_grande']
Nombre: bill, Caracteristicas: ['hombre', 'barba', 'pelirrojo', 'ojos_marrones', 'orejas_grandes', 'mofletes', 'mejillas_sonrosadas', 'calva', 'boca_pequenha', 'nariz_pequenha']
Nombre: anita, Caracteristicas: ['mujer', 'pelo_largo', 'pelo_rubio', 'ojos_marrones', 'boca_pequenha', 'mofletes', 'mejillas_sonrosadas', 'raya_al_medio', 'nariz_pequenha']
Nombre: robert, Caracteristicas: ['hombre', 'cara_triste', 'pelo_castanho', 'ojos_azules', 'orejas_grandes', 'nariz_grande', 'raya_al_lado', 'cara_alargada', 'mofletes', 'mejillas_sonrosadas']
Nombre: anne, Caracteristicas: ['mujer', 'pelo_corto', 'pendientes', 'pelo_negro', 'ojos_marrones', 'boca_pequenha', 'nariz_grande']
Nombre: sam, Caracteristicas: ['hombre', 'gafas', 'calva', 'pelo_blanco', 'canas', 'ojos_marrones', 'boca_pequenha', 'nariz_pequenha']
Nombre: tom, Caracteristicas: ['hombre', 'gafas', 'calva', 'pelo_negro', 'ojos_azules', 'boca_pequenha', 'cara_alargada', 'nariz_pequenha']
Nombre: susan, Caracteristicas: ['mujer', 'pelo_largo', 'pelo_blanco', 'canas', 'ojos_marrones', 'labios_gruesos', 'mofletes', 'mejillas_sonrosadas', 'nariz_pequenha', 'raya_al_lado']
Nombre: max, Caracteristicas: ['hombre', 'bigote', 'pelo_negro', 'ojos_marrones', 'boca_grande', 'labios_gruesos', 'nariz_grande', 'orejas_grandes', 'pelo_corto']
"""

    assert salida_metodo == salida_esperada

@pytest.mark.caracteristicas
def test_caracteristica_a_preguntar():
    personajes = list(prolog.query("personaje(Nombre, Caracteristicas)"))
    assert caracteristica_a_preguntar(personajes) == 'labios_gruesos'

@pytest.mark.caracteristicas
def test_preguntar_la_caracteristica():
    assert preguntar_la_caracteristica('sam', 'calva') == True