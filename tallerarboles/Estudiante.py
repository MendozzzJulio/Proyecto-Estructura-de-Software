class Estudiante:
    def __init__(self, documento:int, nombre: str, edad: int, carrera: str, promedio: float):
        self.documento = int(documento)
        self.nombre = nombre
        self.edad = int(edad)
        self.carrera = carrera
        self.promedio = float(promedio)

    def __str__(self):
        return (
            f"Estudiante: {self.nombre}\n"
            f"Documento: {self.documento}\n"
            f"Edad: {self.edad}\n"
            f"Carrera: {self.carrera}\n"
            f"Promedio: {self.promedio}"
        )
