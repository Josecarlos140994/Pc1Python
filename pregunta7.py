##Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
##- Mostrar una suma de los dos números
##- Mostrar una resta de los dos números (el primero menos el segundo)
##- Mostrar una multiplicación de los dos números
##- En caso de introducir una opción inválida, el programa informará de que no es correcta.

a = float(input("ingrese primer numero:"))
b = float (input("ingrese segundo numero:"))

print("""
      Que desea hacer?
      1) Mostar una suma de los dos números
      2) Mostrar una resta de los dos números (el primero menos el segundo)
      3) Mostrar una multiplicación de los dos números
""")

opcion = input("Elija una opcion (1,2,3):")

if opcion == "1":
    resultado = a + b

elif opcion == "2":
    resultado = a - b

elif opcion == "3":
    resultado = a * b

else:
    resultado = str("Informacion incorrecta")

print(f"La opcion {opcion} es {resultado}")
