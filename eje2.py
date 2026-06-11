#Sistema de Gestión de Inventario de una Librería

inventario = []

def registrar_libro():
    codigo = input("Ingrese el codigo del libro: ")
    
    for libro in inventario:
        if libro["codigo"] == codigo:
            print("Este codigo ya exite")
            return
    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el nombre del autor: ")
    
    try:
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio del libro:"))
        
    except ValueError:
        print("Error: debe ingresar un numero entero valido")
        return
    libro = {
        "codigo":codigo,
        "titulo": titulo,
        "autor": autor,
        "cantidad": cantidad,
        "precio": precio
    }
    
    inventario.append(libro)
    print("Libro registrado con exito")

def buscar_libro():
    codigo = input("Ingrese el codigo para buscar: ")
    
    for libro in inventario:
        if libro["codigo"] == codigo:
            print("\n----Libro encontrado----")
            print(f"Codigo: {libro["codigo"]}")
            print(f"Titulo: {libro["titulo"]}")
            print(f"Autor: {libro["autor"]}")
            print(f"Cantidad: {libro["cantidad"]}")
            print(f"Precio: {libro["precio"]}")
            return
    print("Codigo no encontrado")
            
def actualizar_stock():
    codigo = input("Ingrese el codigo para actualizar cantidad: ")
    
    for libro in inventario:
        if libro["codigo"] == codigo:
            try:
                nueva_cantidad = int(input("Ingrese nueva cantidad: "))
                libro["cantidad"] = nueva_cantidad
                print("Cantidad Actualizada")
            except ValueError:
                print("Error: debe ingresar un numero entero valido")
            return
    print("Codigo no encontrado")
    
def mostrar_inventario():
    print("\n--------Inventario--------")
    for libro in inventario:
        print(f"Codigo: {libro["codigo"]}")
        print(f"Titulo: {libro["titulo"]}")
        print(f"Autor: {libro["autor"]}")
        print(f"Cantidad: {libro["cantidad"]}")
        print(f"Precio: {libro["precio"]}")
        print("----------------------------")