#1.  Básico: imprime todos los números enteros del 0 al 150:
for i in range(151):
    print(i)

#2.  Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000:
mult5 = 5
for i in range(5,1005):
    if i % mult5 == 0:
        print(i , 'es multiplo de 5')
    else:
        continue

#3.  Contar, a la manera del Dojo: imprime números enteros del 1 al 100. Si es divisible por 5, 
mult5 = 5
mult10 = 10
for i in range(1,51):
    if i % mult10 == 0:
        print('Coding Dojo')
    elif i % mult5 == 0:
        print('Coding')
    else:
        print(i)

#4.  Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.
suma = 0

for i in range(500001):
    if i % 2 != 0:
        suma = i + suma

print(suma)

#5.  Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
for i in range(40,-4,-4):
    print(i)

#6.  Contador flexible: establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult. Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). 
lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum,highNum + 1,1):
    if i % mult == 0:
        print(i)

