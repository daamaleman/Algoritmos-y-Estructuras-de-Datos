# Almacenar 10 numeros enteros

list_int = list()

def add_numbers():
    for i in range(10):
        number = int(input("Introduce un numero entero: "))
        if number % 2 != 0 and number > 18: 
            list_int.append(number)
        else:
            print("El numero no es impar o es menor o igual a 18")
            
add_numbers()
print(list_int)