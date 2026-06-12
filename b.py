sys = []

def agregar_tarea():
    descripcion = input("Ingrese la descripcion de la tarea: ")
    
    for tarea in sys:
        if tarea["descripcion"] == descripcion:
            print("Esta descripcion ya esta registrada")
            return
    
    #Valida si esta vacia y con espacio en blanco
    if len(descripcion) == 0 and "" in descripcion:
        print("Debe ingresar una descripcion correcta")
    else:
        print("Descripcion registrada")
        
    try:
        prioridad = float(input("Ingrese la prioridad de la tarea (1-10): "))
        
        #Valida la prioridad (1-10)
        if prioridad < 1 and prioridad > 10:
            print("Debe ingresar un numero entre (1-10)")
        
        elif prioridad >= 1 and prioridad <= 10:
            print("Prioridad registrada")
        
    except ValueError:
        print("Error: debe ingresar un numero entero valido")
        return
    
    try:
        tiempo_estimado = float(input("Ingrese el tiempo estimado para la tarea (mayor a 0): "))
        
        #Valida el timepo
        if tiempo_estimado > 0:
            print("Tiempo registrado")
        else:
            print("Debe ingresar un numero mayor a 0")
        
    except ValueError:
        print("Error: debe ingresar un numero entero valido")
    
    completada = "NO COMPLETADA"
    
    completada = input("¿La tarea esta completada? (S/P/N)").lower
    if completada == "s":
        completada == "COMPLETADA"
    elif completada == "p":
        completada == "PENDIENTE"
    else:
        completada == "NO COMPLETADA"
    
    tarea = {
        "descripcion",
        "prioridad",
        "tiempo_estimado",
        "completada"
    }
    
    sys.append(tarea)
    print("Tarea registrada con exito")
    
def mostrar_tarea():
    if len(sys) == 0:
        print("No hay tareas registradas")
        return
    
    print("------Tareas------")
    for tarea in sys:
        print(f"Descripcion: {tarea["descripcion"]}")
        print(f"Prioridad: {tarea["prioridad"]}")
        print(f"Tiempo estimado: {tarea["tiempo_estimado"]}")
        print(f"Estado: {tarea["completada"]}")
        print("--------------------")
        return
    

while True:
    print("1. agregar")
    print("2. mostrar")
    
    try:
        op = int(input("Ingrese la opcion (1-6)"))
        
        if op == 1:
            agregar_tarea()
        elif op == 2:
            mostrar_tarea()
        elif op == 3:
            break
        else:
            print("Ererer")
            
    except ValueError:
        print("Error: debe ingresar un numero entero valido")