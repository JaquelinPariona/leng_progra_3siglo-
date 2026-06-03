lista_vacia:list=[]
print(len(lista_vacia))
# Por regla el nombre de la variable no debe tener el tipo de dato que se va almacenar
amores:list[str]=['alex','luis','miguel','ryoga','julio']
print(f"la cantidad de elementos que tiene la variable amores es: {len(amores)}")


frutas:list[str]=['🍌','🍎','🍓','🍒']
# posicion o indice
# acceder al tercer elemento
print(frutas[2])
# acceder al 2 elemento por su indice negativo
print(frutas[-3])

## modificar el ultimo elemento con una naranja
frutas[-1]="🍊"
print(frutas) 

### slicing
ciudades:list[str]=['lima','ica','chincha','pauza','urcus']
# Si deseamos que los datos extraidos sean persistentes osea se mantenga almacenados durante la ejecucion de mi programa los almaceno en una variable.
datos_extraidos:list[str]=ciudades[-2:]
# si solo deseo mostrar y no almacenar el slicing lo realizo en el print.
print(ciudades[0:3])
print(datos_extraidos)
## reemplazo de elementos por slicing
num_pares:list[int]=[1,3,5,6,8,10]
print(num_pares)
num_pares[0:3]=[2,4]
print(f"mi lista modifica es: {num_pares}")