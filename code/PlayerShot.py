from code.Entity import Entity
from code.Const import ENTITY_SPEED

class PlayerShot(Entity):
    
    def __init__(self, name, position):
        super().__init__(name, position)
        
    def move(self):
        self.rect.centerx += ENTITY_SPEED['PlayerShoot']
    