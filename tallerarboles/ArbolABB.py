from tallerarboles import NodoABB

class ArbolABB:
    def __init__(self):
        self.raiz = None

    def insertar(self,estudiante):#esta es la funcion publica
        " Inserta un nuevo estudiante en el árbol binario de búsqueda "
        if self.raiz is None:
            self.raiz = NodoABB(estudiante)    
        else:
            self._insertar_recursivo(self.raiz, estudiante)

    def _insertar_recursivo(self, nodo, estudiante):
        if estudiante.documento < nodo.estudiante.documento:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoABB(estudiante)
            else:
                self._insertar_recursivo(nodo.izquierdo, estudiante)
        elif estudiante.documento > nodo.estudiante.documento:
            if nodo.derecho is None:
                nodo.derecho = NodoABB(estudiante)
            else:
                self._insertar_recursivo(nodo.derecho, estudiante)
        else:
            # Documento ya existe, no se permiten duplicados
            print(f"Estudiante con documento {estudiante.documento} ya existe.")

    "usamos la funcion de buscar el estudiante por su documenteyson"
    def buscar_por_documento(self, documento):   #esta es la funcion publica
         return self.buscar(self.raiz,documento) #se llama desde fuera de la clase
                                                #no se necesita que el usuario sepa como funciona internamente
       
    def buscar(self, nodo, documento):
        if nodo is None:
            return None
        if documento == nodo.estudiante.documento:
            return nodo.estudiante
        elif documento < nodo.estudiante.documento:
            return self.buscar(nodo.izquierdo, documento)
        else:
            return self.buscar(nodo.derecho, documento)
     
    def buscar_por_nombre(self, nombre):#esta es la funcion publica
        resultados = []
        self.buscar_nombre(self.raiz, nombre, resultados)
        return resultados

    def buscar_nombre(self, nodo, nombre, resultados):
        if nodo:
            self.buscar_nombre(nodo.izquierdo, nombre, resultados)
            if nodo.estudiante.nombre.lower() == nombre.lower():
                resultados.append(nodo.estudiante)
            self.buscar_nombre(nodo.derecho, nombre, resultados)

    def buscar_por_carrera(self, carrera):#esta es la funcion publica
        resultados = []
        self.buscar_carrera(self.raiz, carrera, resultados)
        return resultados
    
    def buscar_carrera(self, nodo, carrera, resultados):
        if nodo:
            self.buscar_carrera(nodo.izquierdo,carrera,resultados)
            if nodo.estudiante.carrera.lower() == carrera.lower():
                resultados.append(nodo.estudiante)
            self.buscar_carrera(nodo.derecho,carrera,resultados)

    def buscar_por_rango_edad(self, edad_min, edad_max):#esta es la funcion publica
        resultados = []
        self.buscar_edad(self.raiz, edad_min, edad_max, resultados)
        return resultados
    
    def buscar_edad(self, nodo, edad_min, edad_max, resultados):
        if nodo:
            self.buscar_edad(nodo.izquierdo, edad_min, edad_max, resultados)
            if edad_min <= nodo.estudiante.edad <= edad_max:
                resultados.append(nodo.estudiante)
            self.buscar_edad(nodo.derecho, edad_min, edad_max, resultados)

    
    def buscar_por_promedio(self, promedio_min):#esta es la funcion publica
        resultados = []
        self.buscar_promedio(self.raiz, promedio_min, resultados)
        return resultados
    
    def buscar_promedio(self, nodo, promedio_min, resultados):
        if nodo:
            self.buscar_promedio(nodo.izquierdo, promedio_min, resultados)
            if nodo.estudiante.promedio >= promedio_min:
                resultados.append(nodo.estudiante)
            self.buscar_promedio(nodo.derecho, promedio_min, resultados)
   
    def estudiante_mas_joven(self): #esta es la funcion publica
        return self.estudiante_joven(self.raiz,menor = True)
    
    def estudiante_joven(self,nodo,menor = True):
        if nodo is None:
            return None
        
        candidato_izq = self.estudiante_joven(nodo.izquierdo,menor)
        candidato_der = self.estudiante_joven(nodo.derecho,menor)

        candidato = nodo.estudiante
        for x in [candidato_izq,candidato_der]:
            if x:
                if(menor and x.edad < candidato.edad) or (not menor and x.edad > candidato.edad):
                    candidato = x
        return candidato
                
    def estudiante_mayor(self):
        return self.estudiante_joven(self.raiz,menor = False)
    #reutilizamos la misma funcion interna evitar que se duplique el codigo

    def eliminar(self, documento):
        self.raiz = self._eliminar_recursivo(self.raiz, documento)

    def _eliminar_recursivo(self, nodo, documento):
        if nodo is None:
            return None

        if documento < nodo.estudiante.documento:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, documento)
        elif documento > nodo.estudiante.documento:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, documento)
        else:
            # Nodo encontrado
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo

        # Nodo con dos hijos: buscar el sucesor (mínimo en el subárbol derecho)
        sucesor = self._minimo_nodo(nodo.derecho)
        nodo.estudiante = sucesor.estudiante
        nodo.derecho = self._eliminar_recursivo(nodo.derecho, sucesor.estudiante.documento)

        return nodo
    def _minimo_nodo(self, nodo):
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual
       