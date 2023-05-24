# Ejemplo de uso de GITHUB
print("ingreso de datos")
print("------------------ \n")
nom = input("ingrese su nombre: ")
while True:
    try:
        edad = int(input("ingrese su edad: "))
        break
    except:
        print("dato invalido")
print("-------------------")
print(f"su nombre es {nom}")
print(f"su edad es {edad}")
print("programa finalizado..")