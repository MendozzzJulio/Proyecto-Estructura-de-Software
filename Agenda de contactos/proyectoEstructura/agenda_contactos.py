import json
import os
from contacto import Contacto

class AgendaContactos:
    """Esta clase gestiona una coleccion de contactos
    atributos:
        contactos(list): lista de objetos Contacto
        ruta_archivo(str): ruta del archivo JSON para guardar los contactos
    """

    def __init__(self, ruta_archivo='contactos.json'):

        """
        inicializa nueva agenda de contactos
        Args:
            ruta_archivo(str, opcional); Ruta al archivo para almacenar contactos  
        """

        self.contactos = []
        self.ruta_archivo = ruta_archivo
        # Intentar cargar contactos existentes si el archivo existe
        self.cargar()

    def agregar(self, contacto):
        """
        Añade un nuevo contacto a la agenda.
        """
        #Verificar si el contacto ya existe por nombre
        for c in self.contactos:
            if c.nombre.lower() == contacto.nombre.lower():
                return False  # Contacto ya existe
        # Si no existe, añadir el nuevo contacto
        self.contactos.append(contacto)
        return True
    
    def buscar(self, termino):
        """
        Busca un contacto por su termino. como nombre o telefono.
        Args:
            nombre(str): Nombre del contacto a buscar
        Returns:
            list: Lista que coincida con la busqueda 
        """
        resultados = []
        termino = termino.lower()

        for contacto in self.contactos:
            if(termino in contacto.nombre.lower() or
               termino in contacto.telefono.lower() or
               termino in contacto.email.lower()):
               resultados.append(contacto)
        return resultados
    
    def actualizar(self, nombre_actual, nombre=None, telefono=None, email=None, direccion=None):
        """
        Actualiza un contacto que ya existe.
        Args:
            nombre_actual(str): Nombre actual del contacto a actualizar
            nombre(str, opcional): Nuevo nombre del contacto
            telefono(str, opcional): Nuevo telefono del contacto
            email(str, opcional): Nuevo email del contacto
            direccion(str, opcional): Nueva direccion del contacto
        Returns:
            bool: True si el contacto fue actualizado, False si no se encontro
        """

        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre_actual.lower():
                contacto.actualizar(nombre, telefono, email, direccion)
                return True
        return False
    def eliminar(self, nombre):
        """
        Elimina un contacto de la agenda.
        Args:
            nombre(str): Nombre del contacto a eliminar
        Returns:
            bool: True si el contacto fue eliminado, False si no se encontro
        """

        for i, contacto in enumerate(self.contactos):
            if contacto.nombre.lower() == nombre.lower():
                del self.contactos[i]
                return True
        return False
    
    def listar(self):
        """
        Retorna una lista de todos los contactos en la agenda
        """
        return self.contactos
    

    def guardar(self): 
        """
        Devuelve un True si se gurda correctamente el contacto y False si no
        """
        try:
            datos = []
            for contacto in self.contactos:
                datos.append({
                    'nombre': contacto.nombre,
                    'telefono': contacto.telefono,
                    'email': contacto.email,
                    'direccion': contacto.direccion
                })
            # Lo guardamos en formato hijo de J    
            with open(self.ruta_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
                return True
        except Exception as e:
            print(f"Error al guardar contactos: {e}")
            return False

    def cargar(self):
        """
        Carga los contactos desde un archivo JSON.
        Returns:
            bool: True si se cargaron los contactos correctamente y False si nonas
        """
        if not os.path.exists(self.ruta_archivo):
            return False  # El archivo no existe, nada que cargar
        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
                
            # convertir diccionarios a objetos 
            self.contactos = []
            for dato in datos:
                contacto = Contacto(
                    dato['nombre'],
                    dato['telefono'],
                    dato.get('email', '  '),
                    dato.get('direccion', '  ')
                )
                self.contactos.append(contacto)
            return True
        except Exception as e:
            print(f"Error al cargar contactos: {e}")
            return False