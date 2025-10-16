from tallerarboles.estudiante import Estudiante
from tallerarboles.arbol_bb import ArbolBB

DATA_FILE = 'datos_estudiantes.txt'

def cargar_datos(arbol):
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    est = Estudiante.from_string(line)
                    arbol.insertar(est)
                except Exception as e:
                    print('Error al parsear línea:', line, e)
        print('Carga completada.')
    except FileNotFoundError:
        print('Archivo de datos no encontrado:', DATA_FILE)

def mostrar_lista(lista):
    if not lista:
        print('No hay resultados.')
        return
    for e in lista:
        print(e)
        print('---')

def menu():
    arbol = ArbolBB()
    cargar_datos(arbol)
    while True:
        print('\n--- Menú Taller ABB Estudiantes ---')
        print('1. Buscar por documento')
        print('2. Buscar por nombre')
        print('3. Listar por carrera')
        print('4. Listar por rango de edad')
        print('5. Listar por promedio mínimo')
        print('6. Estudiante más joven y más viejo')
        print('7. Eliminar por documento')
        print('0. Salir')
        opt = input('Opción: ').strip()
        if opt == '1':
            d = input('Documento: ').strip()
            r = arbol.buscar_por_documento(d)
            print(r if r else 'No encontrado')
        elif opt == '2':
            n = input('Nombre exacto: ').strip()
            mostrar_lista(arbol.buscar_por_nombre(n))
        elif opt == '3':
            c = input('Carrera: ').strip()
            mostrar_lista(arbol.listar_por_carrera(c))
        elif opt == '4':
            lo = int(input('Edad mínima: '))
            hi = int(input('Edad máxima: '))
            mostrar_lista(arbol.listar_por_rango_edad(lo, hi))
        elif opt == '5':
            m = float(input('Promedio mínimo: '))
            mostrar_lista(arbol.listar_por_promedio_min(m))
        elif opt == '6':
            joven, viejo = arbol.estudiante_mas_joven_y_mayor()
            print('Más joven:')
            print(joven if joven else 'N/A')
            print('\nMás viejo:')
            print(viejo if viejo else 'N/A')
        elif opt == '7':
            d = input('Documento a eliminar: ').strip()
            ok = arbol.eliminar(d)
            print('Eliminado' if ok else 'No encontrado')
        elif opt == '0':
            print('Saliendo...')
            break
        else:
            print('Opción inválida')

if __name__ == '__main__':
    menu()
