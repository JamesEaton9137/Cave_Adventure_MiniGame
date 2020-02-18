"""This script is used to create the tiles that will be used to make the world"""
# __author__ = James Eaton
# __date__ = 2/16/20
# pylint: disable=C0301
# pylint: disable=R0903

import enemies, items, actions, world

class MapTile:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    # The following methods warn us if we create a map tile from this abstract class.
    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        moves = []
        if world.tile_exists(self._x, self._y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self._x, self._y + 1):
            moves.append(actions.MoveSouth())
        if world.tile_exists(self._x + 1, self._y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self._x - 1, self._y):
            moves.append(actions.MoveWest())
        return moves

    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves


class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You find yourself in a dark cave with a single torch flickering on the wall behind you.
        You can make out four different paths that each look equally dark and eerie.
        """

    def modify_player(self, player):
        # This room doesn't affect the player
        pass


class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Yet another empty room. Best to keep moving
        """

    def modify_player(self, player):
        # No action is taken against the player
        pass


class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        A bit of light shines in this room. That's sunlight!
        You did it! You defeated the dragon and found your way out of the cave.
        """

    def modify_player(self, player):
        player._victory = True


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self._enemy = enemy
        super().__init__(x, y)

    def modify_player(self, player):
        if self._enemy.is_alive():
            player._health_points = player._health_points - self._enemy._damage
            print("The {} attacks! You take {} damage. You now have {} health remaining.".format(self._enemy._name, self._enemy._damage, player._health_points))

    def available_actions(self):
        if self._enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self._enemy)]
        else:
            return self.adjacent_moves()


class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())

    def intro_text(self):
        if self._enemy.is_alive():
            return """
            A giant spider drops from the ceiling.
            It's massive fangs look like they can penerate deep.
            Defend yourself!
            """
        else:
            return """
            A giant spider corpse lies rotting.
            Best to keep moving to find a way out.
            """


class CaveBatRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.CaveBat())

    def intro_text(self):
        if self._enemy.is_alive():
            return """
            A huge cave bat flies into the room.
            It looks as if it hasn't eaten in days.
            Defend yourself!
            """
        else:
            return """
            A cave bat corpse lies rotting.
            Best to keep moving to find a way out.
            """


class BanditRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Bandit())

    def intro_text(self):
        if self._enemy.is_alive():
            return """
            A menacing looking man walks up to you with a torch in one hand and a dagger in the other.
            It looks like he was eating supper, and you just interrupted him.
            Defend yourself!
            """
        else:
            return """
            A man's corpse lies rotting.
            Best to keep moving to find a way out.
            """


class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ogre())

    def intro_text(self):
        if self._enemy.is_alive():
            return """
            An ogre! We aren't in a swamp, but he still looks like he means business.
            He may look a little dumb, but the wood log that he wields looks like it can bash in your skull.
            Defend yourself!
            """
        else:
            return """
            An ogre corpse lies rotting.
            Best to keep moving to find a way out.
            """


class CaveDragonRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.CaveDragon())

    def intro_text(self):
        if self._enemy.is_alive():
            return """
            HOLY CRAP, IT'S A DRAGON.
            The exit to the cave is right behind it, but it doesn't look like it's going to let you pass for free.
            Defend yourself!
            """
        else:
            return """
            You feel victorious as you see the dragon that you've slain rotting on the ground.
            The cave exit is near!
            """

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self._item = item
        super().__init__(x, y)

    def add_loot(self, player):
        if self._item._name in player.get_items() and not self._item._name == "Gold" and self._item._looted == False:
            print("You're already carrying one of these items. No point in carrying more than one.")
        elif self._item._name not in player.get_items() or self._item._name == "Gold":
            player._inventory.append(self._item)

        self._item._looted = True

    def modify_player(self, player):
        self.add_loot(player)


class FindGoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(5))

    def intro_text(self):
        if not self._item._looted:
            self._item._looted = True
            return """
            Looks like you've stumbled across some gold!
            You take the money off of the dead corpse that it was near.
            This person isn't going to need it anymore...
            """

        else:
            return """
            Looks like this room as been looted.
            Best to keep moving to find a way out.
            """


class FindHealthPotion(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Health_Potion(10))

    def intro_text(self):
        if not self._item._looted:
            return "Looks like you've found a health potion!\nYou drink it to restore some health to your player."

        else:
            return """
            Looks like this room as been looted.
            Best to keep moving to find a way out.
            """

    def modify_player(self, player):
        if not self._item._looted:
            player._health_points = player._health_points + self._item._heal_amount
            self._item._looted = True
            print("You now have {} health!".format(player._health_points))


class FindRockRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Rock())

    def intro_text(self):
        if not self._item._looted:
            #self._item._looted = True
            return """
            You've found a rock...
            It's big enough to bash some heads, but it's just a rock.
            Good luck.
            """

        else:
            return """
            Looks like this room as been looted.
            Best to keep moving to find a way out.
            """


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        if not self._item._looted:
            self._item._looted = True
            return """
            You've found a worn dagger!
            It looks like it's still sharp enough to poke through enemies.
            Hopefully...
            """

        else:
            return """
            Looks like this room as been looted.
            Best to keep moving to find a way out.
            """


class FindShortSwordRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.ShortSword())

    def intro_text(self):
        if not self._item._looted:
            self._item._looted = True
            return """
            You've found a short sword!
            The blade still has an edge, but just barely. It can slice through enemies with ease.
            """

        else:
            return """
            Looks like this room as been looted.
            Best to keep moving to find a way out.
            """


class FindBroadSwordRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.BroadSword())

    def intro_text(self):
        if not self._item._looted:
            self._item._looted = True
            return """
            You've found a broad sword!
            This two-handed weapon is very heavy, but it can deal massive amounts of damage.
            """

        else:
            return """
            Looks like this room as been looted.
            Best to keep moving to find a way out.
            """


class FindDiamondSwordRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.DiamondSword())

    def intro_text(self):
        if not self._item._looted:
            self._item._looted = True
            return """
            You've found the legendary Diamond Sword!
            This weapon is only talked about in myths and legends.
            It's strong enough to slay a dragon in a singular hit. Lucky you...
            """

        else:
            return """
            Looks like this room as been looted.
            Best to keep moving to find a way out.
            """
