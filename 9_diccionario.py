"""
Ejemplos para trabajar con diccionarios
"""
ALUMNO = {
    'nombre': 'Mario',
    'edad': 22,
    'clase': 'python'
}

print(ALUMNO)
print(ALUMNO['nombre'])
print(ALUMNO['edad'])

ALUMNO['edad'] = 19
print(ALUMNO)

ALUMNO['sexo'] = 'masculino'
print(ALUMNO)

del ALUMNO['sexo']
print(ALUMNO)

ALUMNO.clear()
print(ALUMNO)