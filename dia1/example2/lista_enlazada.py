import datetime as date


class Solicitud:
    def __init__(self, nombre, asunto, carrera, siguiente=None):
        self.nombre = nombre
        self.fecha = date.today()
        self.asunto = asunto
        self.carrera = carrera
        self.siguiente = siguiente
        
    def __str__(self):
        return f"Estudiante: {self.nombre}, Asunto: {self.asunto}, Carrera: {self.carrera} ->"
    
lista_solicitudes = []

def agregar_solicitud(nombre, asunto, carrera):
    nueva_solicitud = Solicitud(nombre, asunto, carrera)
    lista_solicitudes.append(nueva_solicitud)
    return nueva_solicitud

def mostrar_solicitudes():
    for solicitud in lista_solicitudes:
        print(solicitud)
    
def main():
    while True:
        print("1. Agregar Solicitud")
        print("2. Mostrar Solicitudes")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese su nombre: ")
            asunto = input("Ingrese el asunto: ")
            carrera = input("Ingrese la carrera: ")
            agregar_solicitud(nombre, asunto, carrera)
            print("Solicitud agregada.")
        elif opcion == "2":
            mostrar_solicitudes()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

    

        