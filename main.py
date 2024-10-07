import random
from click.termui import clear, pause
from lib.classes.humanClass import Human


def display_intro():
    print(
        """
        -====== Human Survival Simulator CLI ======-
        Author: indra87g
        Version: v0.1.1 BETA
        License: CC BY-NC-SA 3.0
        Github: https://github.com/indra87g/human-survival-simulator
        Bug Report: https://github.com/indra87g/human-survival-simulator/issues
        Documentation: https://indra87g.github.io/human-survival-simulator
        
        * What's new in v0.1.1 ?
        - Refactoring code
        - Adding docs (powered by mkdocs)
        - Gameplay rebalancing
        - UI Improvement
        -==========================================-
        """
    )


def get_player_name():
    player_name = input("Enter your name: ")
    if not player_name:
        print("Player name cannot be empty!")
        exit()
    return player_name


def display_status(player):
    print(
        f"""
        -====== STATUS
        {player.name} Level {player.level}
        XP: {player.xp}/100
        HP: {player.health}
        EP: {player.energy}
        Coins: {player.coins}
        
        Hunger: {player.hunger}
        Thirst: {player.thirst}
        -====================-
        """
    )


def display_menu():
    print(
        f"""
        -====== MENU
        1. Search Food
        2. Eat Foods
        3. Drink Water
        4. Rest
        5. Shop
        6. Inventory
        
        -====== INVENTORY
        {player.inventory}
        
        -====== GAME
        97. Save     98. Load     99. Exit
        """
    )


def shop(player):
    clear()
    print(
        """
        -====== Shop ======-
        Tools:
        Axe (10c)
        Pickaxe (15c)
        
        Foods:
        Golden Apple (100c)
        
        Potions:
        Healing Potion
        -====================-
        """
    )
    item = input("Enter item name: ")
    player.shop(item)


def what_next(player):
    player.check_survive()
    pause()
    main(player)


def handle_choice(choice, player):
    actions = {
        "1": player.search_food,
        "2": lambda: player.eat(input("Enter the food name: ")),
        "3": player.drink,
        "4": lambda: player.rest(random.randint(1, 5)),
        "5": player.lucky_box,
        "6": lambda: shop(player),
        "7": player.show_inventory,
        "97": player.save_game,
        "98": player.load_game,
        "99": exit,
    }
    action = actions.get(choice)
    if action:
        action()
        what_next(player)
    else:
        print("Invalid choice!")
        pause()


def main(player):
    clear()
    display_status(player)
    display_menu()
    choice = input("Enter your choice: ")
    handle_choice(choice, player)


if __name__ == "__main__":
    try:
      display_intro()
      player_name = get_player_name()
      player = Human(player_name)
      main(player)
    except KeyboardInterrupt:
        print("Program closed.")
