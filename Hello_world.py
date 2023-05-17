#1. TAREA: imprime "Hola, mundo"
print("Hola, mundo")

#2. imprime "Hola, Noelle" con el nombre en una variable
name = 'Noelle'
print('Hola', name)
print('Hola ' + name)

#3. imprimir "Hola 42!" con el número en una variable
name = 42
print('Hola', str(name),'!')
print('Hola ' + str(name) + '!')

#4. imprimir "Amo comer sushi y pizza" con las comidas en variables
fave_food1 = 'sushi'
fave_food2 = 'pizza'
print('Amo comer {} y {}'.format(fave_food1,fave_food2))
print(f"Amo comer {fave_food1} y {fave_food2}")

texto1 = 'Amo comer {} y {}'.format(fave_food1,fave_food2)
texto2 = f"Amo comer {fave_food1} y {fave_food2}"
texto2_2 = f"amo comer {fave_food1} y {fave_food2}"

#BONUS NINJA: 
print(texto1.lower())
print(texto2.upper())
print(texto2_2.capitalize())
print(texto1.title())
print(texto1.replace('a' and 'o', 'x'))

###
