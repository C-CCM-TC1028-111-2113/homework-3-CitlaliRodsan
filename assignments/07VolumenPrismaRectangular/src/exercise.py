def areaRect(base, altura):
    area=base*altura
    return area

def volPrism(profundo):
    base=areaRect(b,h)
    vol=base*profundo
    return vol

def main():
    #escribe tu código abajo de esta línea
    global b
    global h
    b=float(input("Dame la base: "))
    h=float(input("Dame la altura: "))
    p=float(input("Dame la profundidad: "))

    print("El volumen del prisma es:", volPrism(p))

if __name__=='__main__':
    main()
