import os
from time import sleep
tipo_cambio = 3.87
bandera = "si"
print("""" 
      ================================
           CONVERTIDOR DE MONEDAS
      ================================
      
       """)
while bandera == "si":
    eleccion = int(input("""Ejija la moneda que desea convertir : 
                
                1) SOLES A DOLARES
                2) DOLARES A SOLES
                3) SALIR
                
                
                """))
    sleep(1)
    os.system("clear")
    # soles a dolares
    if eleccion == 1:
        soles = float(input("Escriba el monto de soles a convertir en dólares : "))
        sleep(1)
        os.system("clear")
        dolares = soles / tipo_cambio
        print(f'{soles} soles equivalen a {dolares} dolares')

        continuar = int(input("""Desea continuar : 
                        1) SI
                        2) NO
                        
                        
                        """))
        if continuar == 1:
            os.system("clear")
            pass

        elif continuar == 2:
            os.system("clear")
            print("Gracias por usar el convertidor de moneda")
            sleep(1)
            bandera = "no"
        else:
            print("Opcion no válida")
            sleep(1)
            bandera = "no"

    # dolares a soles
    elif eleccion == 2:
        dolares = float(input("Escriba el monto de dólares a convertir en soles : "))
        sleep(2)
        os.system("clear")
        soles = dolares * tipo_cambio
        print(f'{dolares} dolares equivalen a {soles} soles')

        continuar = int(input("""Desea continuar : 
                        1) SI
                        2) NO
                   
                        
                        """))
        if continuar == 1:
            os.system("clear")
            pass

        elif continuar == 2:
            os.system("clear")
            print("Gracias por usar el convertidor de moneda")
            sleep(1)
            bandera = "no"
        else:
            print("Opcion no válida")
            sleep(1)
            bandera = "no"
    
    elif eleccion == 3:
        os.system("clear")
        print("Gracias por usar el convertidor de moneda")
        sleep(1)
        exit()
    else:
        os.system("clear")
        print("Opcion no válida")
        sleep(1)
        exit()