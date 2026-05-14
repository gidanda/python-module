from .capabilities import HealCapability, TransformCapability
from ex0.creature import Creature

class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__("Sproutling", "Grass")

    def attack(self):
        return "Sproutling uses Vine Whip!"
    
    def heal(self):
        return "Sproutling heals itself for a small amount"
        

class Bloomelle(Creature, HealCapability):
    def __init__(self):
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self):
        return "Bloomelle uses Petal Dance!"
    
    def heal(self):
        return "Bloomelle heals itself and others for a large amount"

class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Shiftling", "Normal")
        self.is_evolved = False

    def attack(self):
        if self.is_evolved == False:
            return "Shiftling attacks normally."
        else:
            return "Shiftling performs a boosted strike!"
        
    def transform(self):
        self.is_evolved = True
        return "Shiftling shifts into a sharper form!"
    
    def revert(self):
        self.is_evolved = False
        return "Shiftling returns to normal."

class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon", "Normal/Dragon")
        self.is_evolved = False

    def attack(self):
        if self.is_evolved == False:
            return "Morphagon attacks normally."
        else:
            return "Morphagon unleashes a devastating morph strike!"
        
    def transform(self):
        self.is_evolved = True
        return "Morphagon morphs into a dragonic battle form!"
    
    def revert(self):
        self.is_evolved = False
        return "Morphagon stabilizes its form."