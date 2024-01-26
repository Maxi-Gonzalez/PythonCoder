from typing import List

class Cliente :
    # Atributos de la clase
    nombre: str
    mail: str
    edad: int
    intereses: List[str]

    #Constructor
    def __init__(self,nombre: str, mail: str, edad: int, intereses: List[str]):
        self.nombre=nombre
        self.mail=mail
        self.edad=edad
        self.intereses=intereses

    def __str__(self):
        return f"Se ha creado correctamente al cliente {self.nombre}"

    # Método de la clase
    def comprar(self,itemComprado:str , lugarDeCompra:str):
        print(f"El cliente {self.nombre} ha comprado {itemComprado} en la tienda {lugarDeCompra}.\nSe le ha mandado un correo con su factura a {self.mail}")