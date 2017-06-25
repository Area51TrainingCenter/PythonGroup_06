class Reloj:
    def __init__(self, horas, minutos):
        self.horas = horas
        self.minutos = minutos

    def mostrar_hora(self):
        print('{:02d}:{:02d}'.format(self.horas, self.minutos))

    def agregar_hora(self):
        self.horas += 1
        if self.horas > 23:
            self.horas = 0

    def agregar_minuto(self):
        self.minutos += 1
        if self.minutos > 59:
            self.minutos = 0
            self.agregar_hora()


reloj = Reloj(horas=23, minutos=59)
reloj.mostrar_hora()
reloj.agregar_minuto()
reloj.mostrar_hora()
reloj.agregar_hora()
reloj.mostrar_hora()
