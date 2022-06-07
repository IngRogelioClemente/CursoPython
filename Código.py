#Programa que imprime el producto de un numero aleatorio del 1 al 10 por un número generado por el usuario.
import random #Se importa la libreria de random que contiene diferentes metodos para interactuar con valores aleatorios.

print("Introduzca un numero")

num = int(input("Numero: "))
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rand = random.choice(lista)

#Función def que realiza la operación de producto; se le deben asginar dos valores tipo int al instanciarla.
def operacion(num_user, num_random): 
    producto = num_user * num_random
    return producto
    
resultado_final = operacion(num, rand) #Instanciamos la funcion def operacion().
print("Su número", num, "multplicado por el numero aleatorio", rand, "da como resultado:", resultado_final)

input() #Línea que permite probar correctamente la aplicacion de consola.