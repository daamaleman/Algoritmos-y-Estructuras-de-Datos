# Ejercicio 2
# Escribe un programa que recorra una lista de cadenas y calcule la longitud
# de cada cadena, almacenando los resultados en una nueva lista.

list1 = []
# Solicitar al usuario que ingrese cadenas de texto
while True:
    text = input("Ingrese una cadena de texto ('exit' para salir): ")
    if text.lower() == 'exit':
        break
    list1.append(text)
    
# Calcular la longitud de cada cadena y almacenarla en una nueva lista
list2 = []
for item in list1:
    list2.append(len(item))
# Mostrar la lista original y la lista de longitudes
print("Lista de cadenas:", list1)
print("Lista de longitudes:", list2)
# Mostrar la longitud total de todas las cadenas
total_length = sum(list2)
print("Longitud total de todas las cadenas:", total_length)