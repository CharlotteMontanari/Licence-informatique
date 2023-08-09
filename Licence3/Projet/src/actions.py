class Action:
    cost = {
        "MI": 10,
        "DD": 5,
        "AL": 1,
        "PS": 4,
        "FT": 4,
        "IN": 20,
        "TV": 3,
        "TH": 3,
        "TT": 4,
    }

    damage = {"MI": 200, "TV": 20, "TH": 20}

    def __init__(self, instruction: str) -> None:
        self.move: str = instruction

    def get_cost(self) -> int:
        """get cost of an action"""
        return self.cost[self.move.split(" ")[0]]

    def get_damage(self) -> int:
        """get damage"""
        return self.damage[self.move]

    def get_move(self) -> str:
        """get robot's move"""
        return self.move
