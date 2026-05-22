from ex0.creature import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    is_evolved: bool

    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self.is_evolved = False

    def attack(self) -> str:
        if not self.is_evolved:
            return "Shiftling attacks normally."
        return "Shiftling performs a boosted strike!"

    def transform(self) -> str:
        self.is_evolved = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        self.is_evolved = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    is_evolved: bool

    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        self.is_evolved = False

    def attack(self) -> str:
        if not self.is_evolved:
            return "Morphagon attacks normally."
        return "Morphagon unleashes a devastating morph strike!"

    def transform(self) -> str:
        self.is_evolved = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_evolved = False
        return "Morphagon stabilizes its form."
