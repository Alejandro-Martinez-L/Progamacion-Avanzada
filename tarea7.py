class Grupo:
    def __init__(self, grupo):
        self.g = grupo

    def evaluacion(self, c):
        valor = self.g.get(c)
        return valor

    def elementos(self):
        y = set()
        for x in self.g.keys():
            y = y | set(x)
        return list(y)

    def asociatividad(self):
        a = 0
        for x in self.elementos():
            for y in self.elementos():
                for z in self.elementos():
                    if self.evaluacion(N(self.evaluacion(N(x) + N(y))) + N(z)) != self.evaluacion(
                            N(x) + N(self.evaluacion(N(y) + N(z)))):
                        a = 1
        if a == 0:
            print('La operación es asociativa.')
        else:
            print('La operación no es asociativa.')

    def neutro(self):
        b = len(self.elementos())
        a = 0  # número de elementos que no son identidad
        c = ''
        for x in self.elementos():
            for y in self.elementos():
                if self.evaluacion(N(x) + N(y)) != y:
                    a = a + 1
                    break
        if a < b:
            for x in self.elementos():
                for y in self.elementos():
                    if self.evaluacion(N(x) + N(y)) != y:
                        break
                    else:
                        c = x
            return c
        else:
            return False

    def valor_neutro(self):
        if self.neutro() is False:
            print('El conjunto no tiene identidad.')
        else:
            print('El conjunto tiene identidad y es', self.neutro())

    def inverso(self, c):
        if self.neutro() is False:
            return False
        else:
            for x in self.elementos():
                if self.evaluacion(N(x) + N(c)) == self.neutro():
                    return x

    def orden(self, c):
        a = 2
        b = c
        if self.neutro() is False:
            return False
        if c == self.neutro():
            return 1
        else:
            while self.evaluacion(N(b) + N(c)) != self.neutro():
                a = a + 1
                b = self.evaluacion(N(b) + N(c))
            return a

    def conmutatividad(self):
        a = 0
        for x in self.elementos():
            for y in self.elementos():
                if self.evaluacion(N(x) + N(y)) != self.evaluacion(N(y) + N(x)):
                    a = 1
                    break
        if a == 0:
            print('La operación es conmutativa.')
        else:
            print('La operación no es conmutativa.')


class N:
    def __init__(self, n):
        self.numero = n

    def __add__(self, otro):
        m = (self.numero, otro.numero)
        return m


g = Grupo({('0', '0'): '0', ('0', '1'): '1', ('1', '0'): '1', ('1', '1'): '0'})
h = Grupo({('0', '0'): 'b', ('0', 'b'): 'b', ('b', '0'): '0', ('b', 'b'): '0'})
i = Grupo({('0', '0'): '0', ('0', '1'): '1', ('0', '2'): '2', ('0', '3'): '3', ('0', '4'): '4', ('0', '5'): '5',
           ('1', '0'): '1', ('1', '1'): '2', ('1', '2'): '3', ('1', '3'): '4', ('1', '4'): '5', ('1', '5'): '0',
           ('2', '0'): '2', ('2', '1'): '3', ('2', '2'): '4', ('2', '3'): '5', ('2', '4'): '0', ('2', '5'): '1',
           ('3', '0'): '3', ('3', '1'): '4', ('3', '2'): '5', ('3', '3'): '0', ('3', '4'): '1', ('3', '5'): '2',
           ('4', '0'): '4', ('4', '1'): '5', ('4', '2'): '0', ('4', '3'): '1', ('4', '4'): '2', ('4', '5'): '3',
           ('5', '0'): '5', ('5', '1'): '0', ('5', '2'): '1', ('5', '3'): '2', ('5', '4'): '3', ('5', '5'): '4'})

# i.asociatividad()
# i.conmutatividad()
# i.valor_neutro()
# print('El orden de', '1', 'es', i.orden('1'))
# print('El inverso de', '4', 'es', i.inverso('4'))
# print('En el grupo 0+1-2','es', i.evaluacion(N(i.evaluacion(N('0')+N('1')))+N(i.inverso('2'))))
