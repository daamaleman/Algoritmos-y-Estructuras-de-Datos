# Ejercicio 4
# Escribe un programa que busque si una sub cadena esta presente en cada una de las
# cadenas de una lista. El programa debe devolver una lista con los valores booleanos
# que indiquen que la sub cadena fue encontrada en cada cadena.

list1 = []
# Solicitar al usuario que ingrese cadenas de texto
while True:
    text = input("Ingrese una cadena de texto ('exit' para salir): ")
    if text.lower() == 'exit':
        break
    list1.append(text)
# Solicitar al usuario que ingrese la sub cadena a buscar
substring = input("Ingrese la sub cadena a buscar: ")
# Buscar la sub cadena en cada cadena de la lista
list2 = []
for item in list1:
    list2.append(substring in item)
# Mostrar la lista original y la lista de resultados
print("Lista de cadenas:", list1)
print("Lista de resultados:", list2)
# Mostrar la longitud total de todas las cadenas
total_length = sum(len(item) for item in list1)
print("Longitud total de todas las cadenas:", total_length)
