# Convertir a mayúsculas 

texto = "La UAM es la mejor universidad"
print(texto)

texto_mayus = texto.upper()
print(texto_mayus)

# Convertir a minúsculas
texto2 = "VAMOS JAGUARES"
texto2_minus = texto2.lower()
print(texto2_minus)

# Convertir la letea de cada palabra en mayúscula
nombre = "diedereich aleman"
nombre = nombre.title()
print(nombre)

# Remplazar texto
texto = "Hola mundo C#"
print(texto)

texto = texto.replace("C#", "Python")
print(texto)

# Eliminar espacios en blanco 
texto = "     Hola Mundo      "
print(texto)
texto = texto.strip()
print(texto)

# Formato de numeros
numero = 1500
print(numero)
numero = "{.}".format(numero)
print(numero)

# Formato de numero con decimales
numero = 1500.00
print(numero)
numero = "{:,.2f}".format(numero)
print(numero)
