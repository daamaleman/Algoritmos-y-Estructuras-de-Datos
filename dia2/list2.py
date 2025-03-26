# Listas de cadenas 
lista = ["Hola", "Mundo", "Python", "Programacion"]


print(lista)

print(lista[0]) # Hola

print(lista[-1]) # Programacion

print(lista[-2]) # ['Hola', 'Mundo']
print(lista[2: -5]) # ['Python']

lista.append("Ruby")
print(lista) # ['Hola', 'Mundo', 'Python', 'Programacion', 'Ruby']

# Insertar en una posicion especifica
lista.insert(2, "JavaScript")
print(lista) # ['Hola', 'Mundo', 'JavaScript', 'Python', 'Programacion', 'Ruby']