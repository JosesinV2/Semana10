def crear_nodo(dato):
    return {"Dato": dato, "Siguiente": None}

def insertar_inicio(cabeza, dato):
    nuevo = crear_nodo(dato)
    nuevo = ["siguiente"] =  cabeza
    return nuevo

def insertar_final(cabeza, dato):
    nuevo = crear_nodo(dato)
    if cabeza is None:
        return nuevo
    actual = cabeza
    while actual["siguiente"] is not None:
        actual = actual["siguiente"]
    actual["siguiente"] = nuevo
    return cabeza
def menu():
    cabeza = None
    while True:
        print("\n1. Agregar turno  2. Mostrar  3. Buscar")
        print("4. Eliminar turno  5. Contar  0. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "0":
            break
        if opcion in ("1", "3", "4"):
            nombre = input("Nombre: ").strip()
            if not nombre:
                print("Escriba un nombre.")
                continue
        if opcion == "1":
            cabeza = insertar_final(cabeza, nombre)
        elif opcion == "2":
            mostrar(cabeza)
        elif opcion == "3":
            posicion = buscar(cabeza, nombre)
            if posicion == -1:
                print("No encontrado")
            else:
                print("Posición:", posicion)
        elif opcion == "4":
            cabeza, eliminado = eliminar(cabeza, nombre)
            print("Eliminado" if eliminado else "No encontrado")
        elif opcion == "5":
            print("Total:", contar(cabeza))
        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()
    