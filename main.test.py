from src.classes.humanClass import Human

def test_humanclass():
    human = Human('John')
    if human.name == 'John' and human.coins == 10 and human.health == 100 and human.hunger == 0 and human.thirst == 0 and human.energy == 100 and human.foods_inventory == [] and human.items_inventory == []:
        print('Test #1 for attributes in humanClass success!')
    else:
        print('Test #1 for attributes in humanClass failed!')
test_humanclass()