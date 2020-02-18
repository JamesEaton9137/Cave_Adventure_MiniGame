"""This script is the main script to be able to play the game. The game continues until the player wins, dies, or quits"""
# Author: James Eaton
# Date: 2/17/20
# pylint: disable=C0301
# pylint: disable=R0903

import time
import world
from player import Player

def play():
    """Base script for playing the game"""
    world.load_tiles()
    player = Player()

    room  = world.tile_exists(player._location_x, player._location_y)
    print(room.intro_text())

    while player.is_alive() and not player._victory:
        room = world.tile_exists(player._location_x, player._location_y)
        room.modify_player(player)

        if player.is_alive() and not player._victory:
            print("\nChoose an action: \n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input("Actions: ")
            for action in available_actions:
                if action_input == action._hotkey:
                    player.do_action(action, **action._kwargs)
                    break

    if player.is_alive() == False:
        print("You have been slain. Your legacy ends here... And you've dropped all of your gold.")

    time.sleep(10)


if __name__ == "__main__":
    play()
