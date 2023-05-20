#1. Actualizar valores en diccionarios y listas:
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [{'first_name':  'Michael', 'last_name' : 'Jordan'},{'first_name' : 'John', 'last_name' : 'Rosales'}]
directorio_deportes = {'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],'fútbol' : ['Messi', 'Ronaldo', 'Rooney']}
z = [ {'x': 10, 'y': 20} ]

#1.1-. Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)

#1.2-. Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes)

#1.3-. En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes['fútbol'][0] = 'Andres'
print(directorio_deportes)

#1.4-. Cambia el valor 20 en z a 30.
z[0]['y'] = 30
print(z)

#2. Iterar a través de una lista de diccionarios:
# Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, 
# la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado.
# Por ejemplo, dada la siguiente lista:
def iterateDictionary(lista):
    for dictionario in lista:
        linea  = ""
        for llave, valor in dictionario.items():
            linea += f"{llave} - {valor}, "
        print(linea) 
        

estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}]


iterateDictionary(estudiantes)

#3. Obtener valores de una lista de diccionarios:
# Crea una función iterateDictionary2(key_name, some_list)que,
# dada una lista de diccionarios y un nombre de clave, la función
# imprima el valor almacenado en esa clave para cada diccionario. 

# Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:
# Michael
# John
# Mark
# KB

# Y iterateDictionary2('last_name', estudiantes) debería generar:
# Jordan
# Rosales
# Guillen
# Tonel
estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}]

def iterateDictionary2(clave,lista):
    
    if clave == 'name':
        for dictionario in lista:
            print(dictionario['first_name'])
    elif clave == 'last_name':
        for dictionario in lista:
            print(dictionario['last_name'])
    else:
        print('Clave no existe')
        

iterateDictionary2('name',estudiantes)
iterateDictionary2('last_name',estudiantes)
iterateDictionary2('nombre',estudiantes)

#4. Iterar a través de un diccionarios con valores de lista
# Por ejemplo:
# Crea una función printInfo(some_dict)que, dado un diccionario cuyos
# valores son todos listas, imprima el nombre de cada clave junto con
# el tamaño de su lista, y luego imprima los valores asociados dentro 
# de la lista de cada clave. Por ejemplo:

# 7 UBICACIONES
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

def printInfo(some_dict):
    for key in some_dict:
        print(f"{len(some_dict[key])} {key.upper()}")
        for item in some_dict[key]:
            print(item)
        print("")
        
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)