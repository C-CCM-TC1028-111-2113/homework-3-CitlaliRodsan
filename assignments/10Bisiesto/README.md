![Tec de Monterrey](../../images/logotecmty.png)
# Año bisiesto
Funciones-AñoBisiesto

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

¡¡¡IMPORTANTE!!! el archivo exercise.py ya tiene una función main() definida, las funciones que tu definas, deben estar arriba antes de la linea def main(): ¡¡¡IMPORTANTE!!!

Modifica el programa para que haga lo siguiente:

Escribe un programa en el cual definas la función es_bisiesto. 

Esta función debe recibir como parámetro un número entero que representa un año, y te debe regresar True si el año es bisiesto, y False en caso contrario.

Recuerda que un año es bisiesto si es divisible entre 4, excepto cuando es divisible entre 100. Aquellos años que son divisibles entre 100 no son bisiestos, a menos que sean divisibles entre 400.

Ejemplo de ejecución

```
1801
False
```
```
1996
True
```
```
2020
True
```

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

[//]: # (Autor: Gil Huesca - ghjuarez at tec.mx)