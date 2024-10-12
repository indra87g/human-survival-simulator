from click.termui import clear, pause
from lib.classes.humanClass import Human
from lib.variables.main import intro, shop_menu, player_menu, game_menu, default_player


def display_intro():
    print(intro)


def display_status(player):
    print(
        f"""
        -====== STATUS
        {player.name} Level {player.level}
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
        -====== PLAYER MENU
        {player_menu}
        
        -====== INVENTORY
        {player.inventory}
        
        -====== GAME MENU
        {game_menu}
        """
    )


def shop(player):
    clear()
    print(shop_menu)
    item = str(input(f"{player.name} want to buy: "))
    player.shop(item)


def next_turn(player):
    player.check_survive()
    pause()
    main(player)


def handle_choice(choice, player):
    actions = {
        "1": player.search_food,
        "2": lambda: player.eat(str(input(f"{player.name} want to eat: "))),
        "3": player.drink,
        "4": lambda: player.sleep(int(input(f"How much time do {player.name} need for sleep: "))),
        "5": player.chop_tree,
        "6": lambda: shop(player),
        "7": player.show_inventory,
        "97": player.save_game,
        "98": player.load_game,
        "99": exit,
    }
    action = actions.get(choice)
    if action:
        action()
        next_turn(player)
    else:
        print("Invalid choice!")
        next_turn(player)


def main(player):
    clear()
    display_status(player)
    display_menu()
    choice = str(input("Enter your choice: "))
    handle_choice(choice, player)


if __name__ == "__main__":
    try:
        display_intro()
        player_name = str(input("Enter your name: "))
        if not player_name:
          player_name = default_player
          player = Human(player_name)
        else:
          player = Human(player_name)
        main(player)
    except KeyboardInterrupt:
        print("Program closed.")
