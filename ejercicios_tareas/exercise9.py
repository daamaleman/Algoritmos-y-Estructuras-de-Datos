# Ejercicio 9
# Escribe un programa que recorra una lista de cadenas y elimine aquellas
# que estén vacías. Imprime la lista resultante.

list1 = []
# Solicitar al usuario que ingrese cadenas de texto
while True:
    text = input("Ingrese una cadena de texto ('exit' para salir): ")
    if text.lower() == 'exit':
        break
    list1.append(text)
# Eliminar las cadenas vacías
list2 = []
for item in list1:
    if item:  # Verifica si la cadena no está vacía
        list2.append(item)
# Mostrar la lista original y la lista modificada
print("Lista de cadenas:", list1)
print("Lista modificada:", list2)
# Mostrar la longitud total de todas las cadenas
total_length = sum(len(item) for item in list2)
print("Longitud total de todas las cadenas:", total_length)

