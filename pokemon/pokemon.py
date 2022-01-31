class Pokemon:
    def __init__(self, name, type, level=5):
        self.name = name
        self.level = level
        self.health = level * 5
        self.max_health = level * 5
        self.type = type
        self.is_knocked_out = False

