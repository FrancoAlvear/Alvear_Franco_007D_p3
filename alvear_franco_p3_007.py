import numpy as np


lista_ruts = {}
lista_nombre_mascota = {}
lista_nombre_dueño = {}
lista_filas= {1,2}
lista_columna = {1,2,3,4,5,6,7,8,9,10}
lista_opc = {1,2,3,4}
lista_habitaciones_ocupadas = {}

print("bienvenido a la guarderia ")
print("""menú
1.  registrar mascota
2.  buscar mascota
3.  retirar mascota y mostrar el monto a pagar
4.  salir""")

while True:
    try:
        opc = int(input("escoja una de las 4 opciones mostradas en pantalla "))
        if opc in lista_opc:
            break
        else:
            print("ERROR! debe ser una de las opciones en pantalla")
    except:
        print("ERROR debe ser un numero entero")


if opc == 1:
    while True:
        try:
            rut = int(input("Ingrese rut sin digito verificador ni puntos "))
            if rut >= 1000000 and rut <= 99999999:
                break
            else:
                print("ERROR! RUT ENTRE 1000000 Y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
   
   
    while True:
        nom_mascota = input("Ingrese nombre: ")
        if len(nom_mascota.strip()) >= 3 and nom_mascota.isalpha():
            break
        else:
            print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")



    while True:
        nom_duenio = input("Ingrese nombre: ")
        if len(nom_duenio.strip()) >= 3 and nom_duenio.isalpha():
            break 
        else:
            print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")

    while True:
        try:
            nro_habitaciones = np.zeros((2,10))
            print("Eestas son las habitaciones disponibles ")
            print(nro_habitaciones)
            columna = int(input)("Escoja la columna de la habitacion que desea ")
            if columna in lista_columna:
                break
            else:
                print("ERROR! la columna debe ser del 1 al 10")
        except:
            print("ERROR! debe colocar un numero entero")


    while True:
        try:
            fila = int(input("Escoja la fila de la habitacion que desea "))
            if fila in lista_filas:
                break
            else:
                print("ERROR! el numero de ser 1 o 2!")
        except:
            print("ERROR! debe colocar un numero entero")
    
    while True:
        try:
            dias = int(input("Cuantos dias se quedara su mascota "))
            if dias > 30:
                break
            else:
                print("ERROR! no puede pasar de los 30 dias")
        except:
            ("ERROR! debe ser un numero entero")
if opc == 2:
    while True:
        try:
            rut_buscar = int(input("para buscar a su mascota necesitamos que coloque su rut sin puntos ni digito verificador "))
            if rut_buscar in lista_ruts:
                break
            else:
                print("ERROR ese rut no esta registrado")
        except:
            print("ERROR! debe ingresar un numero entero ")

    while True:
        try:
            columna_retirar_mascota = int(input("ingrese la columna de la habitacion donde se encuentra su mascota "))
            if columna_retirar_mascota in lista_columna:
                break
            else:
                print("ERROR! la columna debe ser del 1 al 10")
        except:
            print("ERROR! debe colocar un numero entero")

    while True:
        try:
            fila_retirar_mascota = int(input("ingrese la columna de la habitacion donde se encuentra su mascota "))
            if fila_retirar_mascota in lista_filas:
                break
            else:
                print("ERROR! la fila debe ser el 1 o 2")
        except:
            print("ERROR! debe colocar un numero entero")
    while True:
        if fila_retirar_mascota and columna_retirar_mascota in lista_habitaciones_ocupadas:
            print("Ya puede retirar a su mascota")
    
        
    



        