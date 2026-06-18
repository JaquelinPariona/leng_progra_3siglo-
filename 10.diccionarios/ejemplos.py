# Modulos y libreria estandar
# Libreria estandar typing tipar datos a list y diccionarios para hacer mas optimo el codigo
# Modulo es una porcio de codigo utilizable, para poder usarlo necesitamos inporta la parte el codigo que deseamos utlizar.

# En este codigo estoy inportando desde 1 libreria typing la funcion Union,
# Union me permite tipar una coleccion de tipos, que si no sabes el tipo de datos con union lo podemos pasar una lista de los posibles tipos de datos que puede tener mi valor.
from typing import Union,Dict,List
# sin libreria
#alumno:dict[str:str int]
alumno:dict[str:Union[str,int,float,bool]]={
    "id_alumno":1,
    "dni":78654328,
    "nombre":"mio",
    "edad":20,
    "matricula":True
}
# Acceder 
## clasica
print(alumno["dni"])
# codigo erroneo print(alumno["tricula"])
## metodos 
print(alumno.get("edad","valor no encontrado"))
# Crear/modificar un valor
print(alumno)
alumno["nombre"]="otro" # si existe la clave actualiza el valor
alumno["ruc"]=90876543267 # si no existe la clave lo crea
print(alumno)
# Crear/modificar varios
alumno.update({"nombre":"celia","edad":15})
alumno.update({"carrera":"agro","semestre":"III"})
print(alumno)
# Eliminar
eliminado=alumno.pop("carrera")
print(F"El elemento eliminado es: {eliminado}")
print(f"Mi nuevo diccionario {alumno}")