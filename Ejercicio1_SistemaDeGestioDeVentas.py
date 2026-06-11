#============================
#SISTEMA DE GESTION DE VENTAS
#============================

def calcular_subtotal(precio, cantidad):
    return precio * cantidad

def calcular_descuento(subtotal):
    if subtotal>=100000:
        return subtotal*0.15
    elif subtotal>=50000 and subtotal<100000:
        return subtotal*0.10
    else:
        return 0

def calcular_iva(monto):
    return monto*0.19

def calcular_total(subtotal, descuento,iva):
    return subtotal -descuento+iva

def mostrar_resumen(producto,precio,cantidad,subtotal,
                    descuento,iva, total):
    
    print("\n===RESUMEN DE COMPRA====")
    print(f"Producto: {producto}")
    print(f"Precio: ${precio}")
    print(f"Cantidad: {cantidad}")
    print(f"Subtotal: ${subtotal}")
    print(f"descuento: ${descuento}")
    print(f"IVA: ${iva}")
    print(f"Total: ${total}")
    print("==========================")
    
#Variable para acumular ventas
venta_acumuladas=0

while True:
    print("\n=====MENU=====")
    print("1.Registrar ventas")
    print("2.Mostrar total de ventas acumuladas")    
    print("3.Salir")
    
    try:
        opcion=int(input("Ingrese una opcion(1-3): "))
        
        if opcion==1:
            producto=input("Ingrese el nombre del producto: ")
            
            precio=float(input("Ingrese el precio unitario"))
            cantidad=int(input("Ingrese cantidad: "))
            
            subtotal= calcular_subtotal(precio,cantidad)
            descuento=calcular_descuento(subtotal)
            
            #IVA calculado sobre el subtotal con descuento
            
            iva=calcular_iva(subtotal-descuento)
            
            total=calcular_total(subtotal,descuento,iva)
            
            venta_acumuladas += total
            
            mostrar_resumen(
                producto,
                precio,
                cantidad,
                subtotal,
                descuento,
                iva,
                total
            )
        
        elif opcion==2:
            print(f"\nTotal de ventas acumuladas: ${venta_acumuladas}")
            
        elif opcion==3:
            print("Saliendo del programa.....")
            
        else:
            print("ingrese una opcion valida")
    except ValueError:
        print("Error: Ingrese un valor numerico entero") 
                       
            