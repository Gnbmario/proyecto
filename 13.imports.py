"""
Ejemplos de cómo importar módulos y funciones en python
"""

import utils #importa todo el módulo o archivo

utils.sumar(6, 8)
utils.restar(10,4)

from utils import sumar #importa solo lo que indiquemos

sumar(2, 2)

from libs import bombing
bombing.where_are_the_bombs()

from libs.bombing import where_are_the_bombs, explosion
explosion()

from libs.bombing import*
explosion()
