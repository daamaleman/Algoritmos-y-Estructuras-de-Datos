# Ejercicio 5
# Escribe un programa que recorra una lista de cadenas y reemplace todas las apariciones
# de un caracter específico por otro carácter, luego imprime la lista modificada.

list1 = []
# Solicitar al usuario que ingrese cadenas de texto
while True:
    text = input("Ingrese una cadena de texto ('exit' para salir): ")
    if text.lower() == 'exit':
        break
    list1.append(text)
# Solicitar al usuario que ingrese el carácter a reemplazar y el nuevo carácter
char_to_replace = input("Ingrese el carácter a reemplazar: ")
new_char = input("Ingrese el nuevo carácter: ")
# Reemplazar el carácter en cada cadena de la lista
list2 = []
for item in list1:
    list2.append(item.replace(char_to_replace, new_char))
# Mostrar la lista original y la lista modificada
print("Lista de cadenas:", list1)
print("Lista modificada:", list2)
# Mostrar la longitud total de todas las cadenas
total_length = sum(len(item) for item in list2)
print("Longitud total de todas las cadenas:", total_length)
