#nombre, apellido, cedula
class Cliente:
    def __init__(self, name, apellido, cedula):
        self.nombre=name
        self.apellido=apellido
        self.cedula=cedula
    
    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido
    
    def get_cedula(self):
        return self.cedula
    
    def set_nombre(self,nombre):
        self.nombre=nombre

    def set_apellido(self, apellido):
        self.apellido=apellido
    
    def set_cedula(self,cedula):
        self.cedula=cedula
    
    