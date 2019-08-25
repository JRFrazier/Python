class Batman:
    def __init__(self):
        self.wealth = "Rich"
        self.armor = "Batsuite"
        self.lives = "Gotham"


class IronMan(Batman):
    def __init__(self):
        super().__init__()
        self.armor = "IronMan Suit"
        self.lives = "Malibu"
