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
        precio = float(input("Ingrese el precio del libro: "))

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
    if len(inventario) == 0:
        print("No existen libros registrados")
        return

    print("\n--------Inventario--------")
    for libro in inventario:
        print(f"Codigo: {libro["codigo"]}")
        print(f"Titulo: {libro["titulo"]}")
        print(f"Autor: {libro["autor"]}")
        print(f"Cantidad: {libro["cantidad"]}")
        print(f"Precio: {libro["precio"]}")
        print("----------------------------")
        return

def libro_mas_caro():
    if len(inventario) == 0:
        print("No existen libros registrados")
        return
    
    mas_caro = inventario[0]
    for libro in inventario:
        if libro["precio"] > mas_caro["precio"]:
            mas_caro = libro
    
    print("\n-------Libro mas caro------")
    print(f"Codigo: {mas_caro["codigo"]}")
    print(f"Titulo: {mas_caro["titulo"]}")
    print(f"Autor: {mas_caro["autor"]}")
    print(f"Cantidad: {mas_caro["cantidad"]}")
    print(f"Precio: {mas_caro["precio"]}")
    print("-----------------------------")
    return

def eliminar_libro():
    codigo = input("Ingrese el codigo del libro a eliminar: ")
    
    for libro in inventario:
        if libro["codigo"] == codigo:
            inventario.remove(libro)
            print("Libro eliminado correctamente")
            return
    print("Este codigo no esta registrado")
    
while True:
    print("\n------Menu------")
    print("1. Registrar libro")
    print("2. Buscar libro")
    print("3. Actualizar stock")
    print("4. Mostrar inventario")
    print("5. Mostar libro mas caro")
    print("6. Eliminar libro")
    print("7. Salir")
    
    try:
        op = int(input("Ingrese una opcion (1-7): "))
    
        if op == 1:
            registrar_libro()
        elif op == 2:
            buscar_libro()
        elif op == 3:
            actualizar_stock()
        elif op == 4:
            mostrar_inventario()
        elif op == 5:
            libro_mas_caro()
        elif op == 6:
            eliminar_libro()
        elif op == 7:
            print("Saliendo del programa...")
            break
        else:
            print("Debe ingresar una opcion entre (1-7)")
        
    except ValueError:
        print("Error: debe ingresar un numero entero valido")
