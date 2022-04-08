#numeroCuenta, Saldo
class Cuenta:
    def __init__(self,cedula, numero_cuenta, saldo):
        self.cedula_usuario=cedula
        self.numero_cuenta=numero_cuenta
        self.saldo=saldo
    
    def get_saldo(self):
        return self.saldo

    def get_numero(self):
        return self.numero_cuenta

    def get_celula(self):
        return self.celula


    def set_saldo(self,saldo):
        self.saldo=saldo

    def set_numero(self,numero):
        self.numero_cuenta=numero

    def set_celula(self,celula):
        self.celula=celula
    
