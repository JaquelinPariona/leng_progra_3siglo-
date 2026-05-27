# Crear haciendo uso de las clases anteriores, una calculadora.
# Que pida al usuario dos numeros enteros y luego
## De que manera ordenada mostrar por terminal el resultado


mensaje_bienvenido:str="""
======================================
=   * BIENVENIDO A MI CALCULADORA *  =
======================================
"""
print(mensaje_bienvenido)
print("A continuacion ingrese dos numeros para realizar la suma")
numero_uno:int=int(input("Ingrese el primer numero:"))
numero_dos:int=int(input("Ingrese el segundo numero:"))
resultado_suma:int=numero_uno+numero_dos
mensaje_resultado:str=f"""
el resultado de la suma del numero
{numero_uno}
con el numero 
{numero_dos}
es igual a {resultado_suma} 
"""
print(mensaje_resultado)