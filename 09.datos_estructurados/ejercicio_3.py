alumnos:list[str]=['deduardo','noemi','victor','emerson','yo']
print(alumnos)
# Eliminar por valor
alumnos.remove('yo') 
print(alumnos)
# Eleminar el ultimo valor por defecto
alumnos.pop()
print(alumnos)
# Pop tambien elimina elementos por indice
### El metodo pop tiene la caracteristica de recuperar el elmento eliminado eso quiero decir que podemos almacenarlo en una variable.
a=alumnos.pop(1)
print(f"elimine: {a}")
print(f"mi lista de desaprobados sera: {alumnos}")

# Tengo una lista de marcas de veiculos(toyota,nissan,datsun,daewod,simo mack,mazda,honda),crear un programa que realize lo siguiente:
"""
1. eliminar el 5 elemento.
2. En su lugar agrega la marca mitsubishi.
3. buscar nissap y mostrar su valor por terminal 
4. mostrar si existe honda en mi lista de vehiculos
"""
m_veiculos:list[str]=['toyota','nissap','datsun','daewod','simo mack''mazda','honda']
# 1
m_veiculos.pop(4)
# 2
m_veiculos.insert(4,'mitsubishi') 
# 3
buscar:int=m_veiculos.index("nissap") 
print (m_veiculos[buscar])
# 4
existe:bool="honda" in m_veiculos
print(existe)