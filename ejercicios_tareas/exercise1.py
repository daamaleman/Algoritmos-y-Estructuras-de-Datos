# Ejercicio 1
# Crea una lista de cadenas de texto. Escriba un programa que recorra
# esta lista y concatene todas las cadenas en una sola cadena, separadas
# por un espacio.

list1 = []

# Solicitar al usuario que ingrese cadenas de texto
while True:
    text = input("Ingrese una cadena de texto ('exit' para salir): ")
    if text.lower() == 'exit':
        break
    list1.append(text)
    
# Concatenar las cadenas en una sola cadena, separadas por un espacio
result = ' '.join(list1)
print("Lista de cadenas:", list1)
# Mostrar el resultado
print("Cadena concatenada:", result)