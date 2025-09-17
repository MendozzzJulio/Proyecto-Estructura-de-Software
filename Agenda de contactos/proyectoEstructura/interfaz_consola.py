from agenda_contactos import AgendaContactos
from contacto import Contacto

class InterfazConsola:
    """
       Clase que maneja la interaccion con el usuario a traves de la cosola
    """
    def __init__(self):
        # inicializa la interfaz con una nueva agenda de contactos
        self.agenda = AgendaContactos()

    def mostrar_menu(self):
        # Muestra el menu principal en consola

        print("\n=====AGENDA DE CONTACTOS=====")

        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Listar contactos")
        print("6. Guardar cambios")
        print("0. Salir")
        print("===================")

    
    def ejecutar(self):
        # Ejecuta el bucle principal de la interfaz
        while True:
            self.mostrar_menu()
            opcion = input("Selecione una opción: ")
            if opcion == "1":
                self.agregar_contacto()
            elif opcion == "2":
                self.buscar_contacto()
            elif opcion == "3":
                self.actualizar_contacto()
            elif opcion == "4":
                self.eliminar_contacto()
            elif opcion == "5":
                self.listar_contactos1()
            elif opcion == "6":
                self.guardar_cambios()
            elif opcion == "0":
                if input("¿Desea guardar los cambios antes de salir?(s/n)").lower() == "s":
                    self.guardar_cambios()
                print("Saliendo de la agenda. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor intente de nuevo.")     

    def agregar_contacto(self):
        # Solicita datos al usuario y agrega el nuevo contacto
        print("\n----Agregar nuevo contacto---")
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el telefono del contacto: ")
        email = input("Ingrese el email del contacto (opcional): ")
        direccion = input("Ingrese la direccion del contacto (opcional): ")
        nuevo_contacto = Contacto(nombre, telefono, email, direccion)
        if self.agenda.agregar(nuevo_contacto):
            print(f"Contacto {nombre} agregado exitosamente.")
        else:
            print(f"El contacto {nombre} ya existe en su agenda")
            
    def buscar_contacto(self):
                # Busca y muestra contactos segun el termino de busqueda
                print("\n----Buscar contacto----")
                termino = input("Ingrese el nombre o telefono a buscar: ")
                resultados = self.agenda.buscar(termino)

                if resultados:
                    print(f"Se han encontrado {len(resultados)} contactos:")
                    for i, contacto in enumerate(resultados, 1):
                        print(f"\n---- Contacto {i}")
                        print(contacto)
                else:
                    print("No se han encontrado contactos que coincidan con la busqueda.")
            

    def actualizar_contacto(self):
        # Actualiza un contacto que existe 
        print("\n ---Actualizar contacto----")
        nombre = input("Nombre del contacto a actualizar: ")

        # Buscar si existe el contacto
        resultados = self.agenda.buscar(nombre)
        contacto_encontrado = None

        for contacto in resultados:
            if contacto.nombre.lower() == nombre.lower():
                contacto_encontrado = contacto
                break
        if contacto_encontrado:
            print(f"\nContacto encontrado: \n{contacto_encontrado}")
            print("\nIngrese los nuevos datos (deje en blanco para no modificar): ")

            nuevo_nombre = input(f"Nuevo nombre [{contacto_encontrado.nombre}]: ")
            nuevo_telefono = input(f"Nuevo telefono [{contacto_encontrado.telefono}]: ")
            nuevo_email = input(f"Nuevo email [{contacto_encontrado.email}]: ")
            nueva_direccion = input(f"Nueva dirección [{contacto_encontrado.direccion}]: ")

            # Si el user dejo en blanco un campo en blando mantengo el valor 
            nuevo_nombre = None if nuevo_nombre == "" else nuevo_nombre
            nuevo_telefono = None if nuevo_telefono == "" else nuevo_telefono   
            nuevo_email = None if nuevo_email == "" else nuevo_email
            nueva_direccion = None if nueva_direccion == "" else nueva_direccion

            if self.agenda.actualizar(contacto_encontrado.nombre, nuevo_nombre, nuevo_telefono, nuevo_email, nueva_direccion):
                print("Contacto actualizado exitosamente.")
            else:
                print(f"No se encontró un contacto con el nombre {nombre}.")


    

    def eliminar_contacto(self):
                # Elimina un contacto que ya existe
                print("\n----Eliminar contacto----")
                nombre = input("Ingrese el nombre del contacto a eliminar: ")

                if self.agenda.eliminar(nombre):
                    print(f"Contacto {nombre} eliminado exitosamente.")
                else:
                    print(f"No se encontró un contacto con el nombre {nombre}.")

            
    def listar_contactos1(self):
                # Lista todos los contactos en la agenda
                print("\n----Lista de contactos----")
                contactos = self.agenda.listar()

                if contactos:
                    for i, contacto in enumerate(contactos, 1):
                        print(f"\n---- Contacto {i} ----")
                        print(contacto)
                else:
                    print("No hay contactos en la agenda.")
                

    def guardar_cambios(self):
                #Guarda los contactos en un archvivo

                if self.agenda.guardar():
                    print("Cambios guardados correctamente")
                else:
                    print("Error al guardar los cambios")


                
