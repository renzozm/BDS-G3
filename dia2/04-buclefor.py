# BUCLE FOR

x = input("INGRESE EL NUMERO PARA DESARROLLAR SU TABLA DE MULTIPLICACION : ")
for contador in range(1,13):
    multiplicacion = int(x) * contador
    print(f'{x} x {contador} = {multiplicacion}')