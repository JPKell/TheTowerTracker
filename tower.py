''' This represents the tower itself and is responsible for tallying the attributes '''
from workshop import Workshop


class Tower:
    def __init__(self):
        self.workshop = Workshop()


tower = Tower()

print(tower.workshop.attack.damage)