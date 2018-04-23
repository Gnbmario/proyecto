"""
Ejemplo para pedir input de usuario y formatear la respuesta
"""

PREGUNTA = '¿Cómo te llamas? '
RESPUESTA = input(PREGUNTA)

print('Hola', RESPUESTA, '¿cómo estas?')

SALUDO = 'Bienvenido al curso de python'
RESPUESTA_FORMATEADA = 'Hola {}, {}'.format(RESPUESTA, SALUDO)

print(RESPUESTA_FORMATEADA)
