# Ejercicio 10
# Escribe un programa que recorra una lista de cadenas y cuente cuántas
# veces aparece un caracter específico en cada cadena. Al final, muestra
# el conteo para cada cadena

list1 = []
# Solicitar al usuario que ingrese cadenas de texto
while True:
    text = input("Ingrese una cadena de texto ('exit' para salir): ")
    if text.lower() == 'exit':
        break
    list1.append(text)
# Solicitar al usuario que ingrese el carácter a contar
char_to_count = input("Ingrese el carácter a contar: ")
# Contar cuántas veces aparece el carácter en cada cadena
list2 = []
for item in list1:
    count = item.count(char_to_count)
    list2.append(count)
# Mostrar la lista original y el conteo de caracteres
print("Lista de cadenas:", list1)
print("Conteo de caracteres:")
for i, count in enumerate(list2):
    print(f"{list1[i]}: {count} veces")
# Mostrar la longitud total de todas las cadenas
total_length = sum(len(item) for item in list1)
print("Longitud total de todas las cadenas:", total_length)