def es_bisiesto(año):
    if (not(año%100==0)):
        bool=False
        if año%400==0:
            bool=True
        elif año%4==0:
            bool=True
    else: 
        bool=False
    return bool

def main():
    #escribe tu código abajo de esta línea
        
    año=int(input())
        
    print(es_bisiesto(año))

if __name__=='__main__':
    main()
