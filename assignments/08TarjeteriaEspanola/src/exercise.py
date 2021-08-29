import math

def tarjetas(pliegos, plumones):
    pliego=pliegos*12
    plumon=plumones*35
    if pliego<plumon:
        tarjetas=math.floor(pliego)
    else:
        tarjetas=math.floor(plumon)
    return tarjetas

def main():
    #escribe tu código abajo de esta línea
    pliegos=int(input("Dame la cantidad de pliegos de papel albanene: "))
    plumones=int(input("Dame la cantidad de plumones: "))

    print("El número máximo de tarjetas que se pueden hacer es:", tarjetas(pliegos, plumones))

if __name__=='__main__':
    main()

