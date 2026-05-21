# este tipo de dato sirve para alamacenar informacion de tipo texto, texto simples o texto extenso. 
# para almacenarundato de tipo texto la informacion debera de estar encerrada entre comillas ("",'',""""""").
## - comillas dobles ("")
## - comillas sinples ('')
## - docstring ("""""",'''''')
nombre_instituto:str="IESPT-JMA"
nombre_curso:str='lenguaje de pro.'
descripcion_curso:str="""
El curso de "lenguaje de programacion",
tiene una duracion de un semestre 
educativo con 6 horas semanales y
eprendera a programar en el lenguaje
"paython"
"""

## Los string tienen funciones basicas para poder interactuar con los datos que estamos almacenando
## La estructura de una funcion es la siguiente
## nombre_funcion(argumento)
## *argumento - es un valor que se le pasa a una funcio, funcion que en base a su progracion retornara otro valor distinto al pasado por el argumento 
# funcion mostrar informacion por terminal
print("hola mundo") # salida: hola mundo
print("hola","mundo") # salida: hola mundo

# Funcion para mostrar la cantidad de caracteres que tiene un string-texto
texto:str = "soy deduardo"
cantidad_caracteres:int = len(texto)
print("cantidad_caracteres:",cantidad_caracteres)

# forma d acceder a un caracter en especial 
## para esto hacemos uso de la notacion de corchete[]
## Para esto tenemos que entender que python asigna a cada caracteres con un indice de base cero

# ejemplo: celia
# indices 01234
nombre_celia:str = "celia"
print(nombre_celia)
print(nombre_celia[2])

# troceado de texto
## para esto se utiliza la notacion de corchetes con la diferencia que se debe indicar un indice inicial y un final de texto a extraer.
## texto[i_inicial:i_final]
vocales:str = "aeiou"
print(vocales[1:3])
print(vocales[3:])
print(vocales[:3])
