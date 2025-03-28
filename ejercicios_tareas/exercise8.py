# Ejercicio 8
# Escribe un programa que recorra una lista de cadenas y las ordene alfabéticamente
# en orden ascendente. 

list1 = []
# Solicitar al usuario que ingrese cadenas de texto
while True:
    text = input("Ingrese una cadena de texto ('exit' para salir): ")
    if text.lower() == 'exit':
        break
    list1.append(text)
# Ordenar la lista alfabéticamente en orden ascendente
list1.sort()
# Mostrar la lista ordenada
print("Lista ordenada:", list1)
# Mostrar la longitud total de todas las cadenas
total_length = sum(len(item) for item in list1)
print("Longitud total de todas las cadenas:", total_length)