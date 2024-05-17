from .attack import attack
from .defence import defence 
from .utility import utility



class Workshop:
    def __init__(self):
        self.attack = WSAttack()
        self.defence = WSDefence()
        self.utility = WSUtility()


class WorkshopAttributes:
    ''' A superclass for workshop skills '''
    def __init__(self, branch:str, min:int, max:int, unit:str, name:str, description:str):
        self.branch = branch
        self.min = min 
        self.max = max
        self.unit = unit
        self.name = name
        self.description = description
        self._cur_level = 0

    def __str__(self):
        return f"""{self.name}: {self.description}\n Level: {self.current_level} of {self.max}\n Value: {self.value} {self.unit}"""
    
    def __repr__(self):
        return f"WSAttributes({self.branch}, {self.min}, {self.max}, {self.unit}, {self.name}, {self.description})"

    @property
    def current_level(self) -> int:
        return self._cur_level
    
    @current_level.setter
    def current_level(self, var:int) -> None: 
        if var >= self.min and var <= self.max:
            self._cur_level = var
        else:
            raise Exception(f"{var} is not with in the min and max range for {self.name}. Min: {self.min} Max:{self.max}")

    @property
    def value(self) -> int:
        ''' Get the value from the database based on currently set level'''
        val = 0
        return  val
    
    @value.setter
    def value(self, var:int) -> None:
        ''' Set the value of the attribute '''
        raise Exception("Cannot set value directly. Use current_level instead")

class WSAttack:
    def __init__(self):
        self.damage = WorkshopAttributes(**attack["damage"])
        self.attack_speed = WorkshopAttributes(**attack["attack_speed"])
        self.crit_chance = WorkshopAttributes(**attack["crit_chance"])
        self.crit_factor = WorkshopAttributes(**attack["crit_factor"])
        self.range = WorkshopAttributes(**attack["range"])
        self.dmg_per_meter = WorkshopAttributes(**attack["dmg_per_meter"])
        self.multishot_chance = WorkshopAttributes(**attack["multishot_chance"])
        self.multishot_targets = WorkshopAttributes(**attack["multishot_targets"])
        self.rapid_fire_chance = WorkshopAttributes(**attack["rapid_fire_chance"])
        self.rapid_fire_duration = WorkshopAttributes(**attack["rapid_fire_duration"])
        self.bounce_shot_chance = WorkshopAttributes(**attack["bounce_shot_chance"])
        self.bounce_shot_targets = WorkshopAttributes(**attack["bounce_shot_targets"])
        self.bounce_shot_range = WorkshopAttributes(**attack["bounce_shot_range"])
        self.super_crit_chance = WorkshopAttributes(**attack["super_crit_chance"])
        self.super_crit_mult = WorkshopAttributes(**attack["super_crit_mult"])
        self.rend_armor_chance = WorkshopAttributes(**attack["rend_armor_chance"])
        self.rend_armor_mult = WorkshopAttributes(**attack["rend_armor_mult"])

class WSDefence:
    def __init__(self):
        self.health = WorkshopAttributes(**defence["health"])
        self.health_regen = WorkshopAttributes(**defence["health_regen"])
        self.defence_perc = WorkshopAttributes(**defence["defence_perc"])
        self.defence_abs = WorkshopAttributes(**defence["defence_abs"])
        self.thorn_dmg = WorkshopAttributes(**defence["thorn_dmg"])
        self.lifesteal = WorkshopAttributes(**defence["lifesteal"])
        self.knockback_chance = WorkshopAttributes(**defence["knockback_chance"])
        self.knockback_force = WorkshopAttributes(**defence["knockback_force"])
        self.orb_speed = WorkshopAttributes(**defence["orb_speed"])
        self.orbs = WorkshopAttributes(**defence["orbs"])
        self.shockwave_size = WorkshopAttributes(**defence["shockwave_size"])
        self.shockwave_freq = WorkshopAttributes(**defence["shockwave_freq"])
        self.landmine_chance = WorkshopAttributes(**defence["landmine_chance"])
        self.landmine_dmg = WorkshopAttributes(**defence["landmine_dmg"])
        self.landmine_radius = WorkshopAttributes(**defence["landmine_radius"])
        self.death_defy = WorkshopAttributes(**defence["death_defy"])
        self.wall_health = WorkshopAttributes(**defence["wall_health"])   
        self.wall_rebuild = WorkshopAttributes(**defence["wall_rebuild"])

class WSUtility:
    def __init__(self):
        self.cash_bonus = WorkshopAttributes(**utility["cash_bonus"])
        self.cash_per_wave = WorkshopAttributes(**utility["cash_per_wave"])
        self.coin_per_kill = WorkshopAttributes(**utility["coin_per_kill"])
        self.coins_per_wave = WorkshopAttributes(**utility["coins_per_wave"])
        self.free_attack_upgrade = WorkshopAttributes(**utility["free_attack_upgrade"])
        self.free_defence_upgrade = WorkshopAttributes(**utility["free_defence_upgrade"])
        self.free_utility_upgrade = WorkshopAttributes(**utility["free_utility_upgrade"])
        self.interest_per_wave = WorkshopAttributes(**utility["interest_per_wave"])
        self.recovery_amount = WorkshopAttributes(**utility["recovery_amount"])
        self.max_recovery = WorkshopAttributes(**utility["max_recovery"])
        self.package_chance = WorkshopAttributes(**utility["package_chance"])
        self.enemy_attack_lvl_skip = WorkshopAttributes(**utility["enemy_attack_lvl_skip"])
        self.enemy_health_lvl_skip = WorkshopAttributes(**utility["enemy_health_lvl_skip"])


