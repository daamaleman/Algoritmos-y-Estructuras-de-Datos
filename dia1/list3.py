# listas divididas
# 1. En pilas
# 2. En colas - Filas

# Pila

stack = [] # Pila

def push(val):
    if len(stack) < 5:
        stack.append(val)
    else:
        print("Stack overflow")
    
def pop():
    if len(stack) > 0:
       return stack.pop() # Devuelve el ultimo valor agregado
    else:
        print("Stack underflow")
     
def menu():
    print("1. Push")
    print("2. Pop")
    print("3. Salir")
    return int(input("Introduce una opcion: "))
          
while True:
    option = menu()
    if option == 1:
        push(int(input("Introduce un valor: ")))
    elif option == 2:
        print(pop())
    elif option == 3:
        break
    else:
        print("Opcion invalida")
        
print("Gracias por usar el programa!")
    