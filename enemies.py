"""This script is used to create the enemies in the game"""
# __author__ = James Eaton
# __date__ = 2/16/20
# pylint: disable=C0301
# pylint: disable=R0903


class Enemies():
    def __init__(self, name, health_points, damage):
        self._name = name
        self._health_points = health_points
        self._damage = damage

    def is_alive(self):
        return self._health_points > 0


class GiantSpider(Enemies):
    def __init__(self):
        super().__init__(name="Giant Spider",
                         health_points=10,
                         damage=2)


class CaveBat(Enemies):
    def __init__(self):
        super().__init__(name="Cave Bat",
                         health_points=10,
                         damage=3)


class Bandit(Enemies):
    def __init__(self):
        super().__init__(name="Bandit",
                         health_points=15,
                         damage=7)


class Ogre(Enemies):
    def __init__(self):
        super().__init__(name="Ogre",
                         health_points=30,
                         damage=15)


# Dungeon Boss
class CaveDragon(Enemies):
    def __init__(self):
        super().__init__(name="Cave Dragon",
                         health_points=100,
                         damage=40)
