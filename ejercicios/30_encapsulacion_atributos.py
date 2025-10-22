class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, nuevo_saldo):
        self.__saldo = nuevo_saldo

    @saldo.deleter
    def saldo(self):
        delattr(self, '_CuentaBancaria__saldo')
    
cuenta = CuentaBancaria(1000)
print(cuenta.saldo)
cuenta.saldo=2000
print(cuenta.saldo)
print(cuenta.__dict__)
delattr(cuenta, 'saldo')
print(cuenta.__dict__)