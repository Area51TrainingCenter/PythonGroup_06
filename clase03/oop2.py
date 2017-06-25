class CuentaCorriente:
    def __init__(self, saldo):
        self.saldo = saldo

    def balance(self):
        print('S/. {}'.format(self.saldo))

    def depositar(self, cantidad):
        self.saldo += cantidad

    def transferir(self, otra_cuenta, cantidad):
        if cantidad > self.saldo:
            print('Saldo insuficiente')
        else:
            self.saldo -= cantidad
            otra_cuenta.depositar(cantidad)

cuenta_ag = CuentaCorriente(100)
cuenta_ag.depositar(10)
cuenta_ag.balance()  # => "S/. 110"

cuenta_ppk = CuentaCorriente(5)
cuenta_ag.transferir(cuenta_ppk, 500)  # => "No saldo"
cuenta_ag.transferir(cuenta_ppk, 5)
cuenta_ppk.balance()  # => "S/. 10"
