bandera = "si"
while(bandera == "si"):
    print("=============== CALCULADORA CON PYTHON ================")
    numero1 = int(input("Número 1 : "))
    numero2 = int(input("Numero 2 : "))
    operacion = int(input("""Ingrese el tipo de operacion 
                        1) SUMA
                        2) RESTA
                        3) MULTIPLICACION
                        4) DIVISION
                          
                        INGRESE OPCION : """))
    if(operacion == 1):
        resultado = numero1 + numero2
        print(f'El resultado de la suma de {numero1} con {numero2} es {resultado}')
    elif(operacion == 2):
        resultado = numero1 - numero2
        print(f'El resultado de la resta de {numero1} con {numero2} es {resultado}')
    elif(operacion == 3):
        resultado = numero1 * numero2
        print(f'El resultado de la multiplicacion de {numero1} con {numero2} es {resultado}')
    elif(operacion == 4):
        resultado = numero1 / numero2
        print(f'El resultado de la division de {numero1} con {numero2} es {resultado}')
    else:
        print("La operacion seleccionada no existe!!!")
    
    continuar = input("Desea continuar? (si / no) : ")
    if continuar == "no":
        exit()
    #bandera = input("Quiere continuar con la calculadora? (si / no) : ")
