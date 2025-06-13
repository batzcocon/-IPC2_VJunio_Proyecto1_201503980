class Carta:
    def __init__(self, color: str, numero: int):
        self.color = color
        self.numero = numero
        
    def coincide(self, otra_carta):
        return self.color.lower() == otra_carta.color.lower() or self.numero == otra_carta.numero
    
    def __str__(self):
        return f'{self.numero} ({self.color})'
    
    