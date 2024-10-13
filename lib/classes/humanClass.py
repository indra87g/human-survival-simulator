import random, json, sqlite3
from lib.variables.main import foods, foods_energy, shop_items


class Human:
    def __init__(
        self, name, coins=10, health=100, hunger=0, thirst=0, energy=100, foods_inventory=None, items_inventory=None
    ):
        self.name = name
        self.coins = coins
        self.health = health
        self.hunger = hunger
        self.thirst = thirst
        self.energy = energy
        self.foods_inventory = foods_inventory if foods_inventory is not None else []
        self.items_inventory = items_inventory if items_inventory is not None else []
        self.xp = 0
        self.level = 1

    def search_food(self):
        food_found = random.choice([True, False])
        if food_found:
            food = random.choice(foods)
            print(f"{self.name} found some {food}.")
            self.foods_inventory.append(food)
            self.gain_xp(7)
        else:
            print(f"{self.name} found no food.")
            self.update_stats('bad', random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))

    def eat(self, food):
        food_energy = foods_energy
        if food in self.foods_inventory:
            self.foods_inventory.remove(food)
            self.update_stats('good', min(self.health + 5, 100), max(self.hunger - food_energy[food], 0), max(self.thirst - 3, 0), min(self.energy + food_energy[food], 100))
            self.gain_xp(5)
            print(f"{self.name} eats {food} and gains {food_energy[food]} energy.")
        else:
            print(f"{self.name} doesn't have any {food} to eat.")

    def drink(self):
        print(f"{self.name} drinks water.")
        self.update_stats('good', 5, 5, 15, 10)
        self.gain_xp(2)

    def sleep(self, hours):
        if hours > 8:
            print(f"Caution! {self.name} sleep for >8 hours!")
            self.update_stats('neutral', 10, random.randint(5, 15), random.randint(5, 20), 25 )
            self.gain_xp(3 * 10)
        else:
          print(f"{self.name} sleep for {hours} hours.")
          self.update_stats('neutral', 5, random.randint(1, 10), random.randint(5, 10), hours * 3)
          self.gain_xp(3 * hours)

    def shop(self, item):
        items = shop_items
        if item in items and self.coins >= items[item]:
            self.items_inventory.append(item)
            self.coins -= items[item]
            print(f"{self.name} bought {item} for {items[item]} coins.")
        else:
            print(f"{self.name} can't afford {item}.")

    def chop_tree(self):
        if "Axe" in self.items_inventory:
            found_gapple = random.choice([True, False])
            print(f"{self.name} is chopping a tree...")
            if found_gapple:
                print(f"Lucky! {self.name} found 1 Golden Apple when chopping a tree!")
                self.foods_inventory.append('Golden Apple')
            else:
                print(f"{self.name} chopped a tree and earned some coins.")
            self.update_stats('bad', 5, random.randint(5, 30), random.randint(5, 25), 40)
            self.coins += random.randint(1, 75)
            self.gain_xp(10)
        else:
            print(f"{self.name} needs an Axe to chop a tree.")
            
    def mining(self):
        if "Pickaxe" in self.items_inventory:
            found_diamond = random.choice([True, False])
            print(f"{self.name} is mining...")
            if found_diamond:
                self.update_stats('bad', random.randint(5, 50), random.randint(5, 25), random.randint(5, 25), random.randint(5, 50))
                self.coins += 150
                print(f"Lucky! {self.name} found diamond and earned 150 coin!")
            else:
                self.update_stats('bad', random.randint(1, 25), random.randint(1, 15), random.randint(1, 15), random.randint(1, 25))
                self.coins += random.randint(10, 100)
                print(f"{self.name} mined and earned some coins.")
        else:
            print(f"{self.name} needs a Pickaxe to mine.")

    def update_stats(self, mode, health, hunger, thirst, energy):
        if mode == 'good':
            self.health += health
            self.hunger -= hunger
            self.thirst -= thirst
            self.energy += energy
        elif mode == 'bad':
            self.health -= health
            self.hunger += hunger
            self.thirst += thirst
            self.energy -= energy
        elif mode == 'neutral':
            self.health += health
            self.hunger += hunger
            self.thirst += thirst
            self.energy += energy

    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.level * 100:
            self.xp -= self.level * 100
            self.level += 1
            print(f"{self.name} leveled up to level {self.level}!")

    def check_survive(self):
        if self.health < 1:
            print(f"{self.name} has died.")
            exit()
        elif self.thirst > 99:
            print(f"{self.name} has died.")
            exit()
        elif self.hunger > 99:
            print(f"{self.name} has died.")
            exit()
        elif self.energy < 1:
            print(f"{self.name} has died")
            exit()
        else:
            if self.hunger < 1:
                self.hunger = 25
            elif self.thirst < 1:
                self.thirst = 30
            print(f"{self.name} is surviving.")
            
    def save_game(self, filename="savegame.json"):
        state = {
            "name": self.name,
            "coins": self.coins,
            "health": self.health,
            "hunger": self.hunger,
            "thirst": self.thirst,
            "energy": self.energy,
            "foods_inventory": self.foods_inventory,
            "items_inventory": self.items_inventory,
            "xp": self.xp,
            "level": self.level,
        }
        with open(filename, "w") as f:
            json.dump(state, f)
        print(f"Game saved to {filename}.")

    def load_game(self, filename="savegame.json"):
        with open(filename, "r") as f:
            state = json.load(f)
        self.name = state["name"]
        self.coins = state["coins"]
        self.health = state["health"]
        self.hunger = state["hunger"]
        self.thirst = state["thirst"]
        self.energy = state["energy"]
        self.foods_inventory = state["foods_inventory"]
        self.items_inventory = state["items_inventory"]
        self.xp = state["xp"]
        self.level = state["level"]
        print(f"Game loaded from {filename}")


    """
    TODO: improve this
    
    def lucky_box(self):
        print("Opening lucky box with 10 coins...")
        self.coins -= 10
        win = random.choice([True, False])
        if win:
            print("Nice, You win!")
            self.health = min(self.health + 25, 100)
            self.hunger = 0
        else:
            print("Loser. You lose everything, including your life :)")
            self.health = 0
    """