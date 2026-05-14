from ex0.factory import CreatureFactory
from .creature import Sproutling, Bloomelle, Shiftling, Morphagon

class HealingCreatureFactory(CreatureFactory):
    def create_base(self):
        return Sproutling()
    
    def create_evolved(self):
        return Bloomelle()

class TransformCreatureFactory(CreatureFactory):
    def create_base(self):
        return Shiftling()
    
    def create_evolved(self):
        return Morphagon()