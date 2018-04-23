"""
Ejemplos de funciones
"""

def saludar():
    print('hola')

saludar()

def hi(name):
    print('hola',name)

hi('Mario')

def add_name(the_list, name):
    the_list.append(name)
    print(the_list)

L = ['Mario','Marito']
add_name(L, 'Gnbmario')
add_name(L, 'muroglobal')

def say(word):
    word ='cambio'
    print(word)

say('hola jefe mario')