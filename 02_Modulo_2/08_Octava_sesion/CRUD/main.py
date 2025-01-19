from controller.menu_controller import MenuController

def mostrar_menu_principal():
    print("\n==============================")
    print("     SISTEMA DE VETERINARIA")
    print("==============================")
    print("1. Registrar Cliente")
    print("2. Registrar Mascota")
    print("3. Programar Cita")
    print("4. Consultar Historial de Mascotas")
    print("5. Gestionar Citas")
    print("6. Salir")
    print("==============================")
    opcion = input("Selecciona una opción: ")
    return opcion

def main():
    controlador_menu = MenuController()

    while True:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            controlador_menu.registrar_cliente()
        elif opcion == "2":
            controlador_menu.registrar_mascota()
        elif opcion == "3":
            controlador_menu.programar_cita()
        elif opcion == "4":
            controlador_menu.consultar_historial()
        elif opcion == "5":
            controlador_menu.gestionar_citas()
        elif opcion == "6":
            print("\nGracias por utilizar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingresa una opción correcta.")

if __name__ == "__main__":
    main()
