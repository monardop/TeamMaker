import sys
from random import randint

def rute_check() -> str:
    try:
        path = sys.argv[1]
    except IndexError:
        print("Ruta no especificada.")
        exit(1)
    return path

def list_maker(path:str) -> list:
    lista = []
    with open(path, "r") as f:
        data = f.read()
    molde = data.split("\n")
    for n in molde:
        jugador = n.split(",")
        lista.append(jugador)
    return lista

def gk_check(lista: list) -> list:
    arqueros =  []
    for jugador in lista:
        if int(jugador[1]) == 1:
            arqueros.append(jugador[0])
            lista.remove(jugador)

    print(f"Los arqueros son: {arqueros}")
    return arqueros

def team_maker(equipoA: list):
    print(arqueros)
    print("El primer equipo es:")
    for n in equipoA:
        print(n[0])
        lista.remove(n)
    print("El segundo equipo es:")
    for n in lista:
        print(n[0])

def seed_generator(lista: list)->list:
    jugadores = len(lista)//2
    seed= []
    while len(seed) != jugadores:
        number = randint(0,len(lista)-2)
        if number not in seed:
            seed.append(number)
    return seed

def random_picker(lista: list):
    jugadores = seed_generator(lista)
    print("El primer equipo:")
    for n in jugadores:
        print(lista[n][0])
        lista.remove(lista[n])
    print("Segundo equipo:")
    for n in lista:
        print(n[0])





path = rute_check()
lista = list_maker(path)
arqueros = gk_check(lista)
random_picker(lista)
