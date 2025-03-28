# Ejercicio 7
# Escribe un programa que recorra una lista de cadenas y divida cada cadena
# en subcadenas utilizando un delimitador específico (por ejemplo, una coma
# o un espacio).

list1 = []
# Solicitar al usuario que ingrese cadenas de texto
while True:
    text = input("Ingrese una cadena de texto ('exit' para salir): ")
    if text.lower() == 'exit':
        break
    list1.append(text)
# Solicitar al usuario que ingrese el delimitador
delimiter = input("Ingrese el delimitador para dividir las cadenas: ")
# Dividir cada cadena en subcadenas utilizando el delimitador
list2 = []
for item in list1:
    list2.append(item.split(delimiter))
# Mostrar la lista original y la lista de subcadenas
print("Lista de cadenas:", list1)
print("Lista de subcadenas:")
for sublist in list2:
    print(sublist)
# Mostrar la longitud total de todas las subcadenas
total_length = sum(len(sublist) for sublist in list2)
print("Longitud total de todas las subcadenas:", total_length)
