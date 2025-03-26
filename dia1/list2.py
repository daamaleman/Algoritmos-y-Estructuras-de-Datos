# Agregar nombres de X cantidad de estudiantes a una lista

list_students = list()

def add_students():
    student = input("Introduce el nombre del estudiante: ")
    list_students.append(student)
    
def show_students():
    print(list_students)
    for student in list_students:
        print(student)
        
while True:
    add_students()
    show_students()
    if input("Deseas agregar otro estudiante? (s/n): ").lower() != "s":
        break
    
print("Gracias por usar el programa!")