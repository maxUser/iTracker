class Combatant:
    initiative = 0
    initiative_bonus = 0
    roll_off = 0 # used for 2 or 3 person combats when initiative and initiative_bonus are tied
    name = 'noname'
    pc = False
    swap = False
    def __str__(self):
        return self.name
