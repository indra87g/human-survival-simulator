import random
from click.termui import clear, pause
from lib.behavior import Human


def display_intro():
    print(
        """
        -====== Human Survival Simulator CLI ======-
        Version: v0.1.0 BETA
        Github: https://github.com/indra87g/human-survival-simulator
        Documentation: https://asterixdocs.github.io/human-survival-simulator
        -==========================================-
        """
    )


def get_player_name():
    player_name = input("Enter your name: ")
    if not player_name:
        print("Player name can't be empty!")
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
        
        Hunger: {player.hunger}
        Thirst: {player.thirst}
        Coins: {player.coins}
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
        5. Open Lucky Box
        6. Shop
        7. Inventory
        
        -====== INVENTORY
        {player.inventory}
        
        -====== GAME
        97. Save
        98. Load
        99. Exit
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
    display_intro()
    player_name = get_player_name()
    player = Human(player_name)
    main(player)
