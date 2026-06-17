# Una ferreteria tiene separado en dos listas los siguiente  productos
"""
1. Lista de productos de limpieza (10 productos)
2. Lista de materiales de construccion 
-------------------------------------------------
el dueño desea realizar las siguientes acciones:
1. En su lista de productos de limpieza existe un material de contruccion, debes eliminarlos y pasar el producto a lista que corresponde.
2. Indicar si en la lista de M.C existe cemento.
3. En la lista de P.L buscar el producto lejia y cambiar su valor por lejia sapolio.
4. Mostrar un mensaje donde se detalle cual es la lista de M.C y la lista de P.L formateado.
"""
#1. Crear mi lista de producto de limpieza:
Productos_limpieza:list[str]=['detergente','guantes','esponja','escoba','lejia','jabon','lava vajilla','cemento','recojedor','cemento']
print(Productos_limpieza)
#2.Crear mi lista de materiales de construccion:
Materiales_construccion:list[str]=['ladrillo','arena','fierro','yeso','clavo','mmadera','regla','alambre','espatula','calaminas ']
print(Materiales_construccion) 

# 1. Cambiar de lista al cemento:
elemento_retirado=Productos_limpieza.pop(Productos_limpieza.index("cemento"))
Materiales_construccion.append(elemento_retirado)

# 2. Indicar si existe cemento M.C:
existe:bool="cemento" in Materiales_construccion
print(f"existe el cemento?: {existe}")
## Segundo opcion utilizado un operador ternario:
print("cemento si existe" if existe else "cemento no existe")

# 3. Cambiar lejia por lejia sapolio:
buscar=Productos_limpieza.index("lejia")
Productos_limpieza[buscar]="lejia sapolio"
print(Productos_limpieza)

# 4. Mostrar mensaje
mensaje:str=f"""
    MI LISTA DE PRODUCTOS DE LIMPIEZA
    {Productos_limpieza}
    -------------------------------------------------------------------------------------------------------------------
    MI LISTA DE MATERIALES DE CONSTRUCCION
    {Materiales_construccion}
"""
print(mensaje)