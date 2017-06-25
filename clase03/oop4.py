class FiguraGeometrica:
    def __init__(self, *lados):
        self.lados = lados

    def area(self):
        raise NotImplementedError


class Rectangulo(FiguraGeometrica):
    def area(self):
        # base = self.lados[0]
        # altura = self.lados[1]
        base, altura = self.lados
        area = base * altura
        print(area)


class Cuadrado(FiguraGeometrica):
    def area(self):
        lado = self.lados[0]
        area = lado * lado
        print(area)


class Circulo(FiguraGeometrica):
    def area(self):
        radio = self.lados[0]
        area = 3.14 * radio * radio
        print(area)


rect = Rectangulo(5, 6)
rect.area()  # => 30

cuadrado = Cuadrado(5)
cuadrado.area()  # => 25

circulo = Circulo(1)
circulo.area()  # => 3.14
