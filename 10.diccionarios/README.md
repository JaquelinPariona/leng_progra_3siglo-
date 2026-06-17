# diccionario
los diccionarios son la forma mas comun de almacenar datos extructurados de objetos que nos rodea en el mundo, al igual que las listas que guardan informacion `enelmentos`, de igual manera los diccionarios almacenan sus datos en `elementos`
la diferencia es uqe las listas almacenan los elementos por ´indice´ 
y los diccionarios almacenan los elemntos por `clave:valor`.
**ejmplo:**
```python
vocales :list[str]=['a','e','i','o','u']
# Indices            0   1   2   3   4
# Un elemento en una lista esta conformado por dos cositas el indice y su valor.
# Para acceder a un valor en una lista
vocales[2] # i
alumno=dict={'nombre':'eduardo','edad':40}
# Un elemnto en un diccionario esta conformado por clave:valor.
# Para acceder a un diccionario
alumno["nombre"] # eduardo
```
## Acceder a elementos
- **Por clave (forma directa)**
```python
persona:dict={
    "nombre":"celia",
    "edad":"16",
    "ciudad":"cabo verde",
    "email":"celiaemail.com"
}
print(persona["edad"]) #16
print(persona["email"]) #celiaemail.com
```
- ** Por metodo (forma mas segura)**
```python
persona:dict={
    "nombre":"celia",
    "edad":"16",
    "ciudad":"cabo verde",
    "email":"celiaemail.com"
}
print(persona.get("nombre")) #celia
# La diferencia de este metodo es que no permite manejar errores
print(persona.get("telefono")) #None
print(persona.get("telefono","no disponible")) # Si la clave telefono no existe no mostra None si no el segundo parametro que le pasemos al metod get
```
## Modificar elementos
**Cambiar un valor existente**
```python
persona:dict={
    "nombre":"celia",
    "edad":"16",
}
persona["edad"]=19
# Agregar una nueva clave:valor
persona["carrera"]="agro"
# Si la clave no existe se crea automaticamente, si existe se actualiza.
```
## Agregar/actualizar multiples elementos 
Para esto tenemos que hacer uso del metodo `.update`
se puede agregar si los pares de `clave:valor` no existe y actualizar si el `clave:valor` existe.
```python
tienda:dict[str:str|int]={
    "razon_social":"bigote",
    "ruc":12387646
}
# Actualizar usando el metodo .update tengo dos maneras de usar este metodo
# 1. Diccionario
tienda.update({"ruc":12387646,"telefono":932478543})
# 2. Pares clave=valor 
tienda.update(h_atencion="9-12",gerente="kevin")
```

## Eliminar elementos 
```python
tienda:dict[str:str|int]={
    "razon_social":"bigote",
    "ruc":12387646
}
el_eliminado=tienda.pop("ruc")
tienda.popitem() # elimina el ultimo elemento
# Para limpiar todo el diccionario
tienda.clear()
```