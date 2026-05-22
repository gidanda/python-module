from abc import ABC, abstractmethod
from typing import cast

from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class BattleStrategyError(Exception):
    def __init__(self, message: str = "Unknown battle strategy error") -> None:
        super().__init__(message)


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        print(creature.attack())

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise BattleStrategyError(
                f"Invalid Creature '{creature.name}' for this aggressive strategy"
            )

        transforming_creature = cast(TransformCapability, creature)
        print(transforming_creature.transform())
        print(creature.attack())
        print(transforming_creature.revert())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise BattleStrategyError(
                f"Invalid Creature '{creature.name}' for this defensive strategy"
            )

        healing_creature = cast(HealCapability, creature)
        print(creature.attack())
        print(healing_creature.heal())

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
