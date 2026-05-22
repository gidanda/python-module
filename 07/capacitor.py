from ex1 import HealingCreatureFactory, TransformCreatureFactory

def test_healing_factory(factory):
    print("Testing Creature with healing capability")
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())

def test_transform_factory(factory):
    print("Testing Creature with  transform capability")
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())
    
if __name__ == "__main__":
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()
    test_healing_factory(healing_factory)
    print()
    test_transform_factory(transform_factory)