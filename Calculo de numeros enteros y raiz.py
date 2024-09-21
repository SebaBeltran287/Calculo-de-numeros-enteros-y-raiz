import math   # para usar las funciones de la libreria

numero1 = int(input("ingrese un numero"))
numero2 = int(input("ingrese otro numero"))
resultado = 0
print ("1. SUMAR")
print ("2. RESTAR")
print ("3. MULTIPLICAR")
print ("4. raiz cuadrada del primer numero")
opcion = input("Seleccione una opción. ")
if opcion=="1":
    resultado = numero1 + numero2
    print(f"el resultado de la suma es: {resultado}")
elif opcion=="2":
    resultado = numero1 - numero2
    print(f"el resultado de la resta es: {resultado}")
elif opcion=="3":
    resultado = numero1 * numero2
    print(f"el resultado de la multiplicación es: {resultado}")
elif opcion=="4":
    resultado = math.sqrt(numero1)   # para calcular raiz cuadrada
    print(f"la raiz cuadrada es: {resultado}")
else:
    print("no seleccionó ninguna opción válida")