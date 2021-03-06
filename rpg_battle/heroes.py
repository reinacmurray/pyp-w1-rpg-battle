from .exceptions import *

class Hero(object):
    BASE_STATS = {'strength': 6,
                  'intelligence': 6,
                  'speed': 6,
                  'constitution': 6}
    BASE_HP = 100
    BASE_MP = 50

    
    def __init__(self, level=1):
        """
        Sets stats up and levels up hero if necessary.
        """
        pass


    def _level_up(self):
        """
        Helper method to handle levelling up
        """
        pass

    def xp_for_next_level(self):
        """
        Returns the number of xp at which the next level is gained.
        By default this should be 10 times current level, so 10 for
        level 1, 20 for level 2, etc.
        """
        pass

    def fight(self, target):
        """
        Attacks target, dealing damage equal to the user's strength.
        """
        pass

    def gain_xp(self, xp):
        """
        Increases current xp total, triggers level up if necessary,
        rolling over any excess xp. Example: If a level 1 hero received
        enough xp to increase its total to 12 xp it would level up and
        then have an xp total of 2.
        """
        pass

    def take_damage(self, damage):
        """
        Reduce hp by damage taken.
        """
        pass

    def heal_damage(self, healing):
        """
        Increase hp by healing but not exceeding maxhp
        """
        pass

    def is_dead(self):
        """
        Returns True if out of hp
        """
        pass


class Warrior(Hero):
    """
    Stat modifiers:
    strength +1
    intelligence -2
    constitution +2
    speed -1
    """
    MODIFIERS = {'strength': 1,
                 'intelligence': -2,
                 'constitution': 2,
                 'speed': -1}

    abilities = ('fight', 'shield_slam', 'reckless_charge')

    
    def shield_slam(self, target):
        """
        cost: 5 mp
        damage: 1.5 * strength
        """
        pass


    def reckless_charge(self, target):
        """
        cost: 4 hp
        damage: 2 * strength
        """
        pass


class Mage(Hero):
    """
    Stat modifiers
    strength -2
    inteligence +3
    constitution -2
    """

    MODIFIERS = {'strength': -2,
                 'intelligence': 3,
                 'constitution': -2}

    abilities = ('fight', 'fireball', 'frostbolt')


    def fireball(self, target):
        """
        cost: 8 mp
        damage: 6 + (0.5 * intelligence)
        """
        pass


    def frostbolt(self, target):
        """
        cost: 3 mp
        damage: 3 + level
        """
        pass


class Cleric(Hero):
    """
    Stat modifiers:
    speed -1
    constitution +1
    """
    MODIFIERS = {'speed': -1,
                 'constitution': 1}

    abilities = ('fight', 'heal', 'smite')


    def heal(self, target):
        """
        cost: 4 mp
        healing: 3 * constitution
        """
        pass


    def smite(self, target):
        """
        cost: 7 mp
        damage: 4 + (0.5 * (intelligence + constitution))
        """
        pass


class Rogue(Hero):
    """
    Stat modifiers:
    speed +2
    strength +1
    intelligence -1
    constitution -2
    """
    MODIFIERS = {'speed': 2,
                 'strength': 1,
                 'intelligence': -1,
                 'constitution': -2}

    abilities = ('fight', 'backstab', 'rapid_strike')


    def backstab(self, target):
        """
        cost: None
        restriction: target must be undamaged, else raise InvalidTarget
        damage: 2 * strength
        """
        pass


    def rapid_strike(self, target):
        """
        cost: 5 mp
        damage: 4 + speed
        """
        pass


