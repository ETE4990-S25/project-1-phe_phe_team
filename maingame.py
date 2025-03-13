import random
import time
import sys
import os

from game_setup import iniialize_game, show_intro, show_help
from player import Player
from neighbor import Neighbor
from room import Room
from mission import Mission
from game_utils import clear_screen, slow_print

def main():
    show_intro()
    player, neighbor, rooms, missions = initialize_game()

    current_room = rooms ["Living Room"]
    player.current_room = current_room.name

    game_running = True
    game_over = False
    turn = 0
    missions_completed = 0
    failed_missions = 0

    while game_running:
        turn += 1
        player.turn_count = turn
        move_neighbor(neighbor, rooms)
        display_location(player, current_room, neighbor, rooms, missions)

        if neighbor.current_room == player.current_room:
            game_over = True
            show_game_over("You have been caught by your neighbor", False)
            break

        if missions_completed >= 5:
            game_over = True
            show_game_over("You have completed 5 sabotage missions, your neighbor is now having a terrible day", True)
            break

        if failed_missions >= 3:
            game_over = True
            show_game_over("you have failed 3 missions, your neigbor's day went too good", False)
            break

        command = input("\nWhat do you want to do? ").strip().lower()

        if command.startswith("move to "):
            destination = command[8:].title()
            if destination in current_room.connected_rooms:
                current_room = rooms[destination]
                player.current_room = current_room.name
                slow_print(f"Moving to {destination}", 0.02)
                time.sleep(1)
            else:
                slow_print(f"The location you selected isn't connected to your current location", 0.02)
                input("press Enter to continue")

        elif command == "sabotage":
            available_missions = [m for m in missions if m.room == current_room.name and not m.completed]
            if available_missions:
                mission = random.choice(available_missions)
                slow_print (f"Mission: {mission.description}", 0.02)

                if solve_math_problem():
                    slow_print("congrats you have sabotaged your neighbor", 0.02)
                    mission.completed = True
                    missions_completed += 1
                    slow_print(f"Missions completed: {missions_completed}/5", 0.02)
                else:
                    slow_print("You failed to sabotage your neighbor", 0.02)
                    failed_missions += 1
                    slow_print(f"Missions failed: {failed_missions}/3", 0.02)
                    neighbor_gets_closer(nighbor, player, rooms)
            else:
                slow_print("No available sabotage missions in this room.", 0.02)
            input("Press Enter to continue")

        elif command == "listen":
            listen_for_neighbor(player, neighbor,rooms)
            input("Press Enter to continue")

        elif command == "status":
            show_status(player, neighbor, missions_completed, failed_missions)
            input("Press Enter to continue")
            