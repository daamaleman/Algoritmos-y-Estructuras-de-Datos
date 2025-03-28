# Ejercicio 3
# Escribe un programa que recorra una lista de cadenas y convierta cada cadena
# a mayúsculas o minusculas dependiendo de un criterio. Si la longitud de la cadena
# es par, conviértela a mayúsculas; si es impar, conviértela a minúsculas.

list1 = []
# Solicitar al usuario que ingrese cadenas de texto
while True:
    text = input("Ingrese una cadena de texto ('exit' para salir): ")
    if text.lower() == 'exit':
        break
    list1.append(text)

# Convertir cada cadena a mayúsculas o minúsculas dependiendo de su longitud
list2 = []
for item in list1:
    if len(item) % 2 == 0:
        list2.append(item.upper())
    else:
        list2.append(item.lower())
# Mostrar la lista original y la lista convertida
print("Lista de cadenas:", list1)
print("Lista convertida:", list2)
# Mostrar la longitud total de todas las cadenas
total_length = sum(len(item) for item in list2)
print("Longitud total de todas las cadenas:", total_length)
