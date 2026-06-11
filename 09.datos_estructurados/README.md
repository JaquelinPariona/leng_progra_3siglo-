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
- acceder y modificar por indice (posicion)
- por indice (posicion)
-  por rango (slicing)
```python
frutas:list[str]=[🍌,🍎,🍓,🍒]
# posicion o indice
# acceder al tercer elemento
print(frutas[2])
# acceder al 2 elemento por su indice negativo
print(frutas[-3])
# modificar 
frutas[3]="naranja"
# acceder por rango
´´´

- acceder  y modificar por rango (slicing)
´´´python
vocales:str=['a','e','i','o','u']
# acceder a eelementos por slicing
# esta tecnica nos permite accede a mas de un elemento en una sola linea de codigo
vocales[0:3]
## reemplaza elemento por slicing
vocales[0:3]=['A','E','I']
```
### Metodos para listas 
Un  metodo es una accion que puede realizar en una lista, los metodos de las variables y se accede al metodos a traves de un punto.
Los metodos mas comunes son aquellos que nos permite, agregar, modificar y eliminar
´´´python
# Agregar elementos
## Append
animales:list[str]=[]
animales.append("leon")
animales.append("gato")
# El metodo append agrega los elementos en la ultima posicion de nuentra  lista
## Insert
numeros_pares:list[int]=[4,6,10]
numeros_pares.insert(0,2)
numeros_pares.insert(3,8)
amigo:list[str]=["juan","jose"]
amigo:insert(1,"deduardo")
# Eliminar elementos
## Eliminar por indice
vocales:list[str]=["a","e","i","o","U"]
del vocal[-1]
## Eliminar por valor
vocales:list[str]=["a","e","i","o","U"]
vocales.remove("U")
## Usando metodo pop
vocales:list[str]=["a","e","i","o","U"]
vocales.pop()
# En este caso pop elimina por defecto el ultimo elemento
vocales.pop(3)
# En este caso eliminara el elmento que se encuentre en la posicion 3
´´´

´´´python
# buscar

amantes:list[str]=['chapo','cristian','emerson','victor']
# Quiero ubicar si en mi lista de infieles existe victor 
buscar:int=amantes.index("victor") # retorna un indice si existe 3
amantes[buscar] # victor
## Busqueda porpertenencia
existe:bool="chapo" in amantes
´´´
## Diccionarios


