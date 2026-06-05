# crear una lista de 5 vertebrados y 5 invertebrados el orden debera ser aleatorio, tendras que hacer las siguientes correcciones.
"""
1. modificar los 3 primero elementos por aves.
2. modificar el 6 y ultimo elemento por reptiles.
3. modificar el elemento 8 por gianfranco 
4. mostrar toda la lista nueva con las modificaciones
"""

animales:list[str]=['rinoceronte','raton','burro','jirafa','caballo','mosca','araña','mariposa','hormiga','pulpo']

print(f"los animales som:{animales}")

animales[0]=['flamenco']

animales[1]=['zorzal']

animales[2]=['gaviota']

animales[5]=['camaleon','iguana','serpiente','cobra','gecko']

animales[7]=['gianfranco']

print(f"lista modificada es: {animales}")