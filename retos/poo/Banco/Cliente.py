#nombre, apellido, celula
class Cliente:
    def __init__(self, name, apellido, celula):
        self.nombre=name
        self.apellido=apellido
        self.celula=celula
    
    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido
    
    def get_celula(self):
        return self.celula
    
    def set_nombre(self,nombre):
        self.nombre=nombre

    def set_apellido(self, apellido):
        self.apellido=apellido
    
    def set_celula(self,celula):
        self.celula=celula
    
    