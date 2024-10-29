# Hacer un programa que funcione con arreglos.

import os
#import kivy 
#from kivy.app import App

def suma_productos(orden, costo ):
    opp = 0 
    suma = 0 
    while opp !='n':
        try:
            print("ingrese 's' para ingresar los productos\nIngrese 'n' para salir")
            opp=input()
            if opp not in ['s', 'n']:
                raise ValueError('Debes ingresar (s/n).')
            if opp =='s':
                while opp !='n':
                    print('Ingresa el nombre del producto: ')
                    orden.append(input())
                    bin = False
                    while bin==False: 
                        # falta hacer que solo acepte int
                        print('Ingresa el costo del articulo que acabas de ingresar: ')
                        costo.append(int(input()))
                        print('Ingrese 1 para afirmar que ese es el precio.\nCualquier otro numero si no es el correcto.')
                        OPP = input()
                        try: 
                            if OPP.isdigit(): 
                                OPP = int(OPP)
                                print('Numero aceptado')
                                if OPP == 1: 
                                    bin = True 
                                else: 
                                    costo.pop()
                                    bin = False
                        except Exception as e: 
                            print('Ingresaste un caracter no aceptado')
                    print("Precione 's' pasa seguir\nPrecione 'n' para salir")
                    opp=input('Ingrese su eleccion: ')
                    if opp not in ['s', 'n']:
                        raise ValueError("Ingrese 's' para seguir o 'n' para salir. ")                    
            elif opp == -1:
                print('Saliendo...')
            else: 
                print("Opcion no valida\nIngrese 's' para continuar o 'n' para salir.")
        except ValueError as e:
            print(f'ERROR: {e}')

    print("Desea ingresar verduras? (s/n)")
    ver = 0
    while ver != ['s','n']:
        try:
            ver= input()
            if ver not in ['s','n']:
                raise ValueError ('Debes ingresar (s/n)')
            if ver == 'n':
                os.system("clear")
                print('---------------------------\n')
                for producto in orden:
                    print('Producto: '+producto)
                print('---------------------------')
                for articulo in costo: 
                    print('costo: $',articulo)
                    suma += articulo 
                print('---------------------------') 
                print('Total: $',suma)
                print('\n---------------------------')
            elif ver =='s':
                print('Seguira...')
                #verduras_frutas(orden, costo)
            else: 
                 print('Opcion no valida, ingresa (s/n)')
        except ValueError as e:
            print(f'Error: {e}')


#def verduras_frutas(orden, costo):
    #tenemos que hacer que te ponga el precio de las verduras.
#    Opp = 0
#    while Opp != 'n':
#        try: 
#            print("Deseas seguir? (s/n)")
#            Opp = (input())
#            if Opp not in ['s','n']:
#                raise ValueError ('Debes ingresar (s/n)')
#            if Opp == 's':
#                while Opp !='n': 
#                    print('Ingresa el nombre del producto: ')
#                    orden.append(input())
#                    bin = False 
#                    while bin == False: 
#                        precio_kilo = input('Ingrese el costo por kilo del articulo: ')
#                        peso = input('Ingrese el peso de su articulo')
#                        total= 1


                        


        print('Ingresa el nombre de la verdura: ')
        orden.append(input())


def main():
    os.system("clear")
    pedido =[]
    dinero = [] 
    print('Este programa es para hacer tus compras\n')
    suma_productos(pedido, dinero )


main()
