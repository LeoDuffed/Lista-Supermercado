# Hacer un programa que funcione con arreglos.
# 
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
                raise ValueError('Debes ingresar un numero de un digito.')
            if opp =='s':
                while opp !='n':
                    print('Ingresa el nombre del producto: ')
                    orden.append(input())
                    bin = False
                    while bin==False: 
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

def main():
    os.system("clear")
    pedido =[]
    dinero = [] 
    print('Este programa es para hacer tus compras\n')
    suma_productos(pedido, dinero )


main()
