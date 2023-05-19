#1. Cuenta regresiva: crea una función que acepte un número como entrada. Devuelve una lista nueva que cuente de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento). 
#   Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]
import random

def cuentaRegresiva(numero):
    lista_cuenta_regresiva = []
    x = numero
    print('#2',x)
    while x >= 0:
        lista_cuenta_regresiva.append(x)
        x-=1
    return lista_cuenta_regresiva
    
        
numero = random.randint(0,20)
print('#1',numero)
print(cuentaRegresiva(numero))

#2. Imprimir y devolver: crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo. 
# Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2

import random

def print_N_return(lista1):
    print(lista1[0])
    return lista1[1]

a = random.randint(1,30)
b = random.randint(1,30)
lista1 = [a,b]

print(lista1)
print(print_N_return(lista1))

#3. Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista. 
# Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)    
import random

def primero_con_todos(lista2):
    suma = lista2[0] + len(lista2)
    return suma
    

lenLista = random.randint(1,10)
print(lenLista)
lista2 = []

for i in range(0,lenLista,1):
    x = random.randint(1,10)
    lista2.append(x)
print(lista2)

print(primero_con_todos(lista2))

#4. Valores mayores que el segundo: escribe una función que acepte una lista y cree una nueva que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprime cuántos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 2 elementos, has que la función devuelva False
# Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
# Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False

def mayor_que_segundo(lista3):
    if len(lista3) < 2:
        return False
    
    lista4 = []
    for i in range(0,len(lista3)):
        if lista3[i] > lista3[1]:
            lista4.append(lista3[i])
    return lista4


print(mayor_que_segundo([5,2,3,2,1,4]))
print(mayor_que_segundo([4]))



#5. Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado.
# Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
# Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]
import random

longitud = random.randint(1,10)
valor = random.randint(1,10)

def long_val(longitud,valor):
    listaXY = []
    for i in range(0,longitud):
        listaXY.append(valor)
        
    return listaXY 

print(longitud,valor)
print(long_val(longitud,valor))
