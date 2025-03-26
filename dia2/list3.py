# Concatenacion de cadenas
nombre = "Diedereich"
apellido = "Aleman"

nombre_completo = nombre + " " + apellido
print(nombre_completo) # Diedereich Aleman

nombre_c = f"{nombre} {apellido}"
print(nombre_c) # Diedereich Aleman

# Concatenar
nombreCompleto = " ".join([nombre, apellido])
print(nombreCompleto) # Diedereich Aleman

#Lisya y concatenar
lista = []
lista.append(nombre)
lista.append(apellido)
nombreCompleto = " ".join(lista)
print(nombreCompleto) # Diedereich Aleman
