# Para declarar una varible en paython usaremos la convencion snake_case
## reglas 
### 1. El nombre de la variable debe indicar que dato se esta almacenando
### 2. Las variable no deben contener numeros ni caracteres especiales(,/,!,?)
nombre_curso="lenguaje de programacion"
creditos_curso=3
horas_semanales_curso=6
# ADVERTENCIA - Las variables son mutables
print(creditos_curso) #salida: 3
creditos_curso=10
print(creditos_curso) #salida: 10

# NOTA INPORTANTE PARA TODO EL CURSO - Cada vez que declaremos variables usaremos anotaciones para indicar que tipo de dato se va a almacenar.

nombre_alumno:str = "deduardo"
edad_alumno:int = 28
estatura_alumno:float = 1.59
asistencia_alumno:bool = True
amigos_alumno:list =[]
direccion_alumno:dict ={
 "n_calle":"psj belen",
 "numero_casa":230,
 "barrio":"ccayao"  
}

# Asignacion se un variable a otra variable
edad_alumno:int = 21
edad_docente:int = edad_alumno

## INPORTANTE NO OLVIDAR
### Un decorador en python nos indica que tipo de dato va almcenar nuestra variable 
### Los decoradores que python trae por defecto son:

############ datos primitivos #########
# decoradores para datos primitivos 
### :int - enteros 
### :float - decimales, como flotante
### :str - string texto
### :bool - datos boleano true o false
 
 ########### Datos estructurados #########
 # decoradores para datos estructurados 
 ### :list - lista
 ### :dict - diccionarios

 ## Como hacemos uso de la variables
 ## Para hacer uso del dato almacenado en una variable basta con hacer el llamado del nombre de la variable
primer_numero:int = 30
segundo_numero:int = 20
suma:int = primer_numero+segundo_numero
