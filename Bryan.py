def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: No se puede dividir por cero.")
        return None

def main():
    print("Bienvenido a la Calculadora Básica")
    while True:
        print("Por favor, seleccione una opción:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = suma(num1, num2)
            print("Resultado: ", resultado)
        elif opcion == "2":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = resta(num1, num2)
            print("Resultado: ", resultado)
        elif opcion == "3":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = multiplicacion(num1, num2)
            print("Resultado: ", resultado)
        elif opcion == "4":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = division(num1, num2)
            if resultado is not None:
                print("Resultado: ", resultado)
        elif opcion == "5":
            print("¡Gracias por usar la Calculadora Básica!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if _name_ == "_main_":
    main()