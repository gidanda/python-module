from abc import ABC, abstractmethod

from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class BattleStrategyError(Exception):
    def __init__(self, message = "Unknown battle strategy error"):
        super().__init__(message)


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass
    
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature):
        print(creature.attack())

    def is_valid(self, creature: Creature):
        return True
    

class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature):
        if not self.is_valid(creature):
            raise BattleStrategyError(
                f"Invalid Creature '{creature.name}' for this aggressive strategy"
                )
        
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())

    def is_valid(self, creature):
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature):
        if not self.is_valid(creature):
            raise BattleStrategyError(
                f"Invalid Creature '{creature.name}' for this defensive strategy"
                )
        
        print(creature.attack())
        print(creature.heal())

    def is_valid(self, creature):
        return isinstance(creature, HealCapability)

    
