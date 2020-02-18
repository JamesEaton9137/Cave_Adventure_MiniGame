"""This script is used to create the keyboard actions for the adventure game"""
# Author: James Eaton
# Date: 2/17/20
# pylint: disable=C0301
# pylint: disable=R0903
from player import Player

class Action():
    """Class to initalize all the player actions"""
    def __init__(self, method, name, hotkey, **kwargs):
        """
        :param method: the function object to execute
        :param name: the name of the action
        :param hotkey: the keyboard button to be used for the action
        """
        self._method = method
        self._name = name
        self._hotkey = hotkey
        self._kwargs = kwargs

    def __str__(self):
        return "{}: {}".format(self._hotkey, self._name)


class MoveNorth(Action):
    """Class to move north using W"""
    def __init__(self):
        super().__init__(method=Player.move_north, name="Move North", hotkey='w')


class MoveSouth(Action):
    """Class to move south using S"""
    def __init__(self):
        super().__init__(method=Player.move_south, name="Move South", hotkey='s')


class MoveEast(Action):
    """Class to move east using D"""
    def __init__(self):
        super().__init__(method=Player.move_east, name="Move East", hotkey='d')


class MoveWest(Action):
    """Class to move west using A"""
    def __init__(self):
        super().__init__(method=Player.move_west, name="Move West", hotkey='a')


class ViewInventory(Action):
    """Class to view the player inventory"""
    def __init__(self):
        super().__init__(method=Player.print_inventory, name="View inventory\n", hotkey="i")


class Attack(Action):
    """Class to attack an enemy"""
    def __init__(self, enemy):
        super().__init__(method=Player.attack, name="Attack", hotkey="f", enemy=enemy)


class Flee(Action):
    """Class to flee from combat"""
    def __init__(self, tile):
        super().__init__(method=Player.flee, name="Flee", hotkey="q", tile=tile)
