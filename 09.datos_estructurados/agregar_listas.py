## Deseamos agregar en una lista vacias los nombres de los paises que participaran en el mundial, desarrollar el programa que haga posibles esta tarea
# PRIMERA FORMA
paises:list[str]=[]
paises.append("peru")
paises.append("bolivia")
paises.append("chile")
print(paises)

# SEGUNDA FORMA
pais:str=input("ingresar el nombre del pais: ")
paises.append(pais)
print(paises)

# TERCER FORMA
rango:int=int(input("ingresa la cantidad de pais que deseas agregar: "))
for i in range(rango):
    nuevos_paises:str=input("ingrese un pais: ")
    paises.append(nuevos_paises)
print(paises)