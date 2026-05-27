# Datos estructurados
- Tenemos 3 tipos  de datos primarios (string, numericos, boleanos)
- Tenemos 2 tipos de datos estructurados (lista, diccionarios)
## Listas
Son la manera de como python puede organizar multiples tipos de datos en una sola variable.
se puede tener:
- listas de tipo numerica
- listas de tipo texto
- listas de tipo mixto
Python nos permite acceder a estas listas a travez de indices, los indices son acendentes enpesando del numero 0.
### Creacion de listas
Para listas solo basta encerrar los elementos que deseamos almacenar con `[]` inmediatamente despues del operador de asignacion `=`
```python
# Creando una lista vacia
lista:list=[] #lista vacia
# lista numerica
## OJON: Los elementos de una lista se separan por comas
lista_numerica:list[int]=[3.6,7,.7]
# lista de texto
amigos:list[str]=[`eduardo`,`kevin`]
# lista mixta
lista_mixta:list=[`pedro`,20,false,2.67]
```
### Acceder y modificar elementos de una lista
Para poder acceder a un elementos de la lista trabajamos con los indices que  python le asigna a cada elementos tenemos:
- los indices positivos (comienzan de 0 y van de izquierda a derecha)
- los indices negativos (comienzan de -1 y van de derecha a izquierda)
Con estos indices podemos acceder al valor del elemento y tambien podremos modificarlos.
Tenemos dos formas de acceder a los elementos:
- por indice (posicion)
-  por rango (slicing)
```python
frutas:list[str]=[🍌,🍎,🍓,🍒]
# posicion o indice
# acceder al tercer elemento
print(frutas[2])
# acceder al 2 elemento por su indice negativo
print(frutas[-3])
# acceder por rango

```
## Diccionarios

