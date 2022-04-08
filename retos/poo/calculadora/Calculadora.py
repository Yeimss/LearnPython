class Calculadora:
    def __init__(self,n1,n2):
        self.numero1=n1
        self.numero2=n2

    def suma(self):
        return self.numero1+self.numero2

    def resta(self):
        return self.numero1-self.numero2

    def multiplicacion(self):
        return self.numero1*self.numero2
    
    def division(self):
        return self.numero1/self.numero2