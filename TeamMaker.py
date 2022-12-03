import sys

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
        dato = f.read()
        jugador = dato.split(',')
        jugador[1].strip()
        lista.append(jugador)
    return lista

def gk_check(lista: list) -> list:
    arqueros =  []
    for jugador in lista:
        if jugador[1] == 1:
            arqueros.append(jugador[0])
            lista.remove(jugador)
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

def random_picker(lista: list):
    jugadores = (len(lista)-len(arqueros)-1) // 2
    points = 0
    equipoA = []
    
    for n in lista:
        points += n[1]
    
    points /= 2

    while True:
        seed = range(jugadores)
        seed.sort()
        sum = 0
        for n in seed:
            equipoA.append(lista[n])
            sum += lista[n][1]
        if sum - points > -2 and sum - points < 2:
            team_maker(equipoA)
            break
        else:
            equipoA.clear()




path = rute_check()
lista = list_maker(path)
arqueros = gk_check(lista)
random_picker(lista)
