"""
Trabajando con clases y POO (programación orientada a objetos)
"""

class Thing:
    pass

thing = Thing()

class Fruit:
    def __init__(self):
        print('objeto fruta iniciado')

fruit = Fruit()

# argumentos del constructor
class Person:
    """ Estas es la documentación de la clase Person """
    COUNTER = 0

    def __init__(self, name):
        self.name = name
        self.knowledges = []
        Person.COUNTER +=1

    def __str__(self):
        return 'Me llamo {} y se: {}'.format(self.name, self.knowledges)

    def learn(self,what):
        self.knowledges.append(what)

p1 = Person('Mario')
p2 = Person('Mary')
p3 = Person('David')

p1.learn('python')
p2.learn('javascript')
p3.learn('c#')

print(p1)
print(p2)
print(p3)
print(Person.COUNTER)

