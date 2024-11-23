intro = """
        -====== Human Survival Simulator CLI ======-
        Author: indra87g
        Version: v0.2.0 BETA
        License: CC BY-NC-SA 3.0
        Github: https://github.com/indra87g/human-survival-simulator
        Bug Report: https://github.com/indra87g/human-survival-simulator/issues
        Documentation: https://indra87g.github.io/human-survival-simulator
        
        * Recomended terminal window size is 120*34 !
        -==========================================-
        """

shop_menu = """
        -====== Shop ======-    
        Foods:
          Golden Apple (100c)
          
        Items:
          Axe (10c)
          Pickaxe (15c)
          
        Rare Items:
          Totem of Undying (1000c)
        -====================-
        """

player_menu = """
        1. Search Food     2. Eat Foods
        3. Drink Water     4. Sleep
        5. Chop Tree       6. Shop
        7. Mining
        """

game_menu = """
        97. Save     98. Load     99. Exit
        """

foods = ["Berries", "Apple", "Chicken", "Rabbit"]
foods_energy = {
    "Berries": 5,
    "Apple": 7,
    "Chicken": 15,
    "Rabbit": 10,
    "Golden Apple": 20,
}
items_durability = {"Axe": 100, "Pickaxe": 100, "Sword": 100}
shop_items = {"Axe": 10, "Pickaxe": 15, "Golden Apple": 100, "Totem of Undying": 1000}
