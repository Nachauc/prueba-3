
from funciones import *

from herramientas import *




menu = load_items('menu.csv')
# user = {
#   'nombre':nombre,
#   'comida_favorita': comida_favorita,
#   'alergias': alergias


# }
print("BIENVENIDO!!")
nombre = input("Por favor digame su nombre : ")
comida_favorita = input("Por favor digame su comida favorita: ")
alergias = input("Padece de alergia a algo : ")

def menu(): 

   while (True):
    print("Bienvenido a el Restaurant")
    print("Escoja una opcion!")
    print("1.Revisar menu")
    print("2.Revisar carrito")
    print("3.Pagar")
    print("4.buscar item")
    print("5.salir")
    opcion = int(input("Ingresa la opcion escojida!: "))

    if opcion == "1":
     carrito(menu,carrito)
     print(carrito)
    pass
   
    elif opcion == "2":
    mostrar_carrito()
    pass

    elif opcion == "3":
    pagar_carrito()
    pass

    elif opcion == "4":
    
    buscar_item()
   

    elif opcion == "5":
        break
      
       


  
def carrito(items:(list)):
   for i in items:
    contador = 0
    contador += 1
    print(i)

def mostrar_carrito():
  print(carrito)


def pagar_carrito():
  if len(carrito):
    print()



def buscar_item():
  
  print("Ingrese la palabra a buscar!")
  palabra_clave = input("ingrese palabra")
  with open ("./menu.csv",'r', encoding= 'uft-8')as filetemp:
    return filetemp.readline()

for palabra_clave in menu:
  print(menu)
    












menu()