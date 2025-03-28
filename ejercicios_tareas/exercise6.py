# Ejercicio 6
# Escribe un programa que recorra una lista de cadenas y elimine los espacios 
# en blanco al principio y al final de cada cadena.

list1 = []
# Solicitar al usuario que ingrese cadenas de texto
while True:
    text = input("Ingrese una cadena de texto ('exit' para salir): ")
    if text.lower() == 'exit':
        break
    list1.append(text)
# Eliminar los espacios en blanco al principio y al final de cada cadena
list2 = []
for item in list1:
    list2.append(item.strip())
# Mostrar la lista original y la lista modificada
print("Lista de cadenas:", list1)
print("Lista modificada:", list2)
# Mostrar la longitud total de todas las cadenas
total_length = sum(len(item) for item in list2)
print("Longitud total de todas las cadenas:", total_length)