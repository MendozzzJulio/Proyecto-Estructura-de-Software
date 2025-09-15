class Contacto: 

    """ Esta clase representa un contacto en la agenda
    """
def __init__(self, nombre, telefono, email= '  ' , direccion= '  ' ):
        # inicializamos los atributos del contacto

        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.direccion = direccion

        def __str__(self): 
            """
            retorna una representacion en Str del contacto
            """
            return f"Contacto: {self.nombre} \nTelefono: {self.telefono} \nEmail: {self.email} \nDireccion: {self.direccion}"
             

def actualizar(self, nombre= None, telefono= None, email= None, direccion= None):
        """ Actualiza los atributos del contacto con los nuevos valores proporcionados.
            Si un valor es None, no se actualiza ese atributo.
        """
        
        if nombre is not None:
            self.nombre = nombre
        if telefono is not None:
            self.telefono = telefono
        if email is not None:
            self.email = email
        if direccion is not None:
            self.direccion = direccion

        def __str__(self): 
            """
            retorna una representacion en Str del contacto
            """
            return f"Contacto: {self.nombre} \nTelefono: {self.telefono} \nEmail: {self.email} \nDireccion: {self.direccion}"
             
    
       