1. # Crear un programa que busque en el pensamiento de cesar acuña la palabra politicos.
# hay politicos que no hacen nada por que nunca han hecho nada.
# y mostrarlo por terminal si lo encuentra.

pensamiento_uno:str="hay politicos que no hacen nada por que nunca han hecho nada."
Palabra_buscar="politicos"
print("politicos" if pensamiento_uno.find(Palabra_buscar)>0 else "texto no encontrado")


2. #Crear un programa que en el siguiente texto 'yo ya no vivo en Trujillo, vivo en Peru'. busque Peru y lo reemplaze por Narnia. finalmente mostrarlo por terminal.  

pensamiento_dos:str='yo ya no vivo en Trujillo, vivo en Peru'
print(pensamiento_dos)
print(pensamiento_dos.replace("Peru","Narnia"))