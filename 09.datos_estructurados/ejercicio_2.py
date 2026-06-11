# Crear un programa que permita agregar a mi lista de comprar los siguientes ingredientes (trucha,cabello,limon,culandro,pinguita de nomo, papa, chancha)
# Entrada de datos 
ingredientes:list[str]=[]
# Desarrollo
for i in range(7):
    ingredientes:str=input("ingrese su ingrediente: ")
    ingredientes.append(ingredientes)
# Datos de salida
print(ingredientes)
# Crear un programa crea agrege al principio de la lista del grupo a de los paises participantes en el mundial.
grupo_a:list[str]=[]
grupo_a.insert(0,"rep. checa")
# ["rep. checa"]
grupo_a.insert(0."corea del sur")
# ["corea del sur","rep. checa"]
grupo_a.insert(0,"sudafrica")
# ["sudafrica","corea del sur","rep. checa"]
grupo_a.insert(0,"mexico")
# ["mexico","sudafrica","corea del sur","rep. checa"]
print(grupo_a)
