class BonusableValue(object):
    def __init__(self,
                 base=0,
                 modifiers={},
                 deltas={},
                 multipliers={},
                 dividers={}):
        self.base = base
        self.modifiers = modifiers
        self.multipliers = multipliers
        self.deltas = deltas
        self.dividers = dividers

    def __str__(self):
        return f"""
        base = {self.base}
        modifiers = {self.modifiers}
        multipliers = {self.multipliers}
        deltas = {self.deltas}
        dividers = {self.dividers}"""


class WeaponModule(object):
    def __init__(self,
                 name="",
                 cost=BonusableValue(),
                 crew=BonusableValue(),
                 weight=BonusableValue(),
                 pierce=BonusableValue(),
                 blast=BonusableValue(),
                 direct=BonusableValue(),
                 radius=BonusableValue(),
                 pellets=BonusableValue(),
                 clip=BonusableValue(),
                 ammo=BonusableValue(),
                 reload=BonusableValue(),
                 clip_reload=BonusableValue()):
        self.name = name
        self.cost = cost
        self.crew = crew
        self.weight = weight
        self.pierce = pierce
        self.blast = blast
        self.direct = direct
        self.radius = radius
        self.pellets = pellets
        self.clip = clip
        self.ammo = ammo
        self.reload = reload
        self.clip_reload = clip_reload

    def __str__(self):
        return f"""
            name = {self.name}
            cost = {self.cost}
            crew = {self.crew}
            weight = {self.weight}
            pierce = {self.pierce}
            blast = {self.blast}
            direct = {self.direct}
            radius = {self.radius}
            pellets = {self.pellets}
            clip = {self.clip}
            ammo = {self.ammo}
            reload = {self.reload}
            clip_reload = {self.clip_reload}"""
