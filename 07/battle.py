from ex0 import AquaFactory, FlameFactory

def test_factory(factory):
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def battle(factory1, factory2):
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()

    print(creature1.describe())
    print(" vs.")
    print(creature2.describe())
    print(" fight!")
    print(creature1.attack())
    print(creature2.attack())

if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    print("Testing factory")
    test_factory(flame_factory)
    print()
    print("Testing factory")
    test_factory(aqua_factory)
    print()
    battle(flame_factory, aqua_factory)