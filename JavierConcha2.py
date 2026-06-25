sys = []

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_edad(edad):
    return int(edad) > 0 and int(edad) <= 100

def validar_temperatura(temperatura):
    return temperatura.isdigit() and 35 <= float(temperatura) <= 42

def mostrar_menu():
    print("\n=======MENU PRINCIPAL=======")
    print("1. Agregar paciente")
    print("2. Buscar paciente")
    print("3. Elminar paciente")
    print("4. Actualizar estado")
    print("5. Mostrar pacientes ")
    print("6. Salir ")
    print("=============================")

def leer_opcion():
    while True:
        try:
            opcion=int(input("Seleccione una opcion(1-6): "))
            if 1<=opcion<=6:
                return opcion
            else:
                print("Debe ingresar una opcion entre 1 y 6")
        except ValueError:
            print("Error: Debe ingresar un numero valido ")

def agregar_paciente(lista):
    nombre = input("Ingrese el nombre del paciente: ")

    if not validar_nombre(nombre):
        print("Error: El nombre no puede estar vacio")
        return

    edad = input("Ingrese la edad del paciente: ")

    if not validar_edad(edad):
        print("Error: La edad debe ser valida")
        return
    temperatura = input("Ingrese la T° del paciente: ")

    if not validar_temperatura(temperatura):
        print("Error: Debe ingresar una T° valida")
        return

    paciente = {
        "nombre": nombre,
        "edad": int(edad),
        "temperatura": float(temperatura),
        "atendido": False
    }
    lista.append(paciente)
    print("Paciente registrado")

def buscar_paciente(lista, nombre):
    for i in range(len(lista)):
        if lista[i]["nombre"] == nombre:
            return i + 1
    return -1

def actualizar_estado(lista):
    for paciente in lista:
        if paciente["temperatura"] <= 37:
            paciente["atendido"] = True
        else:
            paciente["atendido"] = False

def mostrar_pacientes(lista):
    if len(lista) == 0:
        print("No existen pacientes registrados.")
        return
    print("\n=== LISTA DE PACIENTES ===")
    for paciente in lista:
        print(f"Nombre: {paciente['nombre']}")
        print(f"Edad: {paciente['edad']}")
        print(f"Temperatura: {paciente['temperatura']}")
        if paciente["atendido"]:
            print("Estado: ATENDIDO")
        else:
            print("Estado: REQUIERE ATENCION")
        print("=" * 26)

while True:

    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_paciente(sys)
    elif opcion == 2:
        nombre = input("Ingrese nombre del paciente a buscar: ")
        posicion = buscar_paciente(sys, nombre)
        if posicion != -1:
            print("\n======Paciente encontrado======")
            print("Posición:", posicion)
            for paciente in sys:
                print(f"Nombre: {paciente['nombre']}")
                print(f"Edad: {paciente['edad']}")
                print(f"Temperatura: {paciente['temperatura']}")
                if paciente["atendido"]:
                    print("Estado: ATENDIDO")
                else:
                    print("Estado: REQUIERE ATENCION")
            print("==========================")
        else:
            print("El paciente no existe.")

    elif opcion == 3:
        nombre = input("Ingrese nombre del paciente a eliminar: ")
        posicion = buscar_paciente(sys, nombre)
        if posicion != -1:
            sys.pop(posicion)
            print("Paciente eliminado correctamente.")
        else:
            print(f"El paciente '{nombre}' no se encuentra registrada.")

    elif opcion == 4:
        actualizar_estado(sys)
        print("Estados de pacientes actualizados correctamente.")
    elif opcion == 5:
        mostrar_pacientes(sys)
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break