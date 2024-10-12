import random
import json
from lib.variables.main import foods, foods_energy, shop_items


class Human:
    def __init__(
        self, name, coins=10, health=100, hunger=0, thirst=0, energy=100, inventory=None
    ):
        self.name = name
        self.coins = coins
        self.health = health
        self.hunger = hunger
        self.thirst = thirst
        self.energy = energy
        self.inventory = inventory if inventory is not None else []
        self.xp = 0
        self.level = 1

    def search_food(self):
        food_found = random.choice([True, False])
        if food_found:
            food = random.choice(foods)
            print(f"{self.name} found some {food}.")
            self.energy -= random.randint(5, 15)
            self.hunger += random.randint(5, 15)
            self.thirst += random.randint(5, 15)
            self.health -= random.randint(5, 10)
            self.inventory.append(food)
            self.gain_xp(7)
        else:
            print(f"{self.name} found no food.")
            self.energy -= 10
            self.hunger += 10
            self.thirst += 10
            self.health -= random.randint(5, 10)

    def eat(self, food):
        food_energy = foods_energy
        if food in self.inventory:
            self.health = min(self.health + 5, 100)
            self.hunger = max(self.hunger - food_energy[food], 0)
            self.thirst = max(self.thirst - 3, 0)
            self.energy = min(self.energy + food_energy[food], 100)
            self.inventory.remove(food)
            print(f"{self.name} eats {food} and gains {food_energy[food]} energy.")
            self.gain_xp(5)
        else:
            print(f"{self.name} doesn't have any {food} to eat.")

    def drink(self):
        print(f"{self.name} drinks water.")
        self.health = min(self.health + 10, 100)
        self.thirst = max(self.thirst - 12, 0)
        self.energy = min(self.energy + 5, 100)
        self.gain_xp(3)

    def sleep(self, hours):
        if hours > 8:
            print(f"Caution! {self.name} sleep for >8 hours!")
            self.energy = min(self.energy + 10 * 3, 100)
            self.hunger += 15
            self.thirst += 21
        else:
          print(f"{self.name} sleep for {hours} hours.")
          self.energy = min(self.energy + hours * 3, 100)
          self.hunger += 5
          self.thirst += 7
          self.gain_xp(3 * hours)

    def shop(self, item):
        inventory = shop_items
        if item in inventory and self.coins >= inventory[item]:
            self.coins -= inventory[item]
            self.inventory.append(item)
            print(f"{self.name} bought {item} for {inventory[item]} coins.")
        else:
            print(f"{self.name} can't afford {item}.")

    def chop_tree(self):
        if "Axe" in self.inventory:
            print(f"{self.name} is chopping a tree...")
            self.energy -= 40
            self.hunger += 30
            self.thirst += 25
            self.coins += random.randint(1, 75)
            print(f"{self.name} chopped a tree and earned 1 - 75 coins.")
            self.gain_xp(10)
        else:
            print(f"{self.name} needs an Axe to chop a tree.")

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
            print(f"{self.name} is surviving.")

    def show_inventory(self):
        print(f"{self.name}'s inventory:\n {self.inventory}")

    def save_game(self, filename="savegame.json"):
        state = {
            "name": self.name,
            "coins": self.coins,
            "health": self.health,
            "hunger": self.hunger,
            "thirst": self.thirst,
            "energy": self.energy,
            "inventory": self.inventory,
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
        self.inventory = state["inventory"]
        self.xp = state["xp"]
        self.level = state["level"]
        print(f"Game loaded from {filename}")
