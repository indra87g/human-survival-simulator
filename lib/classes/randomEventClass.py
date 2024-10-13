import random

class RandomEvent:
    def trigger_event(self, player):
        isHappened = random.choice([True, False])
        if isHappened == True:
            event_type = random.choice(["find_item", "enemy_attack"])
            # TODO: improve this
            