import random
import time
import sys
import os

from setup import initalize_game, show_intro, show_help
from classes import Player
from classes import Neighbor
from classes import Room
from classes import Mission
from utils import clear_screen, slow_print

SLOW_PRINT_SPEED = 0.01
def main():
   
    show_intro()
    player, neighbor, rooms, missions = initalize_game()
#player starts the game in the living room
    current_room = rooms ["Living Room"]
    player.current_room = current_room.name
#this is the main game functions and loop
    game_running = True
    game_over = False
    turn = 0
    missions_completed = 0
    failed_missions = 0
#the neighbor moves through the house during game
    while game_running:
        turn += 1
        player.turn_count = turn
        move_neighbor(neighbor, rooms)
        display_location(player, current_room, neighbor, rooms, missions)
#this checks if the player got caught by the neighbor
        if neighbor.current_room == player.current_room:
            game_over = True
            show_game_over("You have been caught by your neighbor", False)
            break
#the game is over when 5 sabotages are completed
        if missions_completed >= 5:
            game_over = True
            show_game_over("You have completed 5 sabotage missions, your neighbor is now having a terrible day", True)
            break
#if you fail 3 missions you lose the game
        if failed_missions >= 3:
            game_over = True
            show_game_over("you have failed 3 missions, your neigbor's day went too good", False)
            break

        command = input("\nWhat do you want to do? ").strip().lower()

        if command.startswith("move to "):
            destination = command[8:].title()
            if destination in current_room.conected_rooms:
                current_room = rooms[destination]
                player.current_room = current_room.name
                slow_print(f"Moving to {destination}", SLOW_PRINT_SPEED)
                time.sleep(1)
            else:
                slow_print(f"The location you selected isn't connected to your current location", SLOW_PRINT_SPEED)
                input("press Enter to continue")
#this checks if there are any available sabotages in the current room
        elif command == "sabotage":
            available_missions = [m for m in missions if m.room == current_room.name and not m.completed]
            if available_missions:
                mission = random.choice(available_missions)
                slow_print (f"Mission: {mission.description}", SLOW_PRINT_SPEED)
#this gives a math problem in order to complete the sabotage
                if solve_math_problem():
                    slow_print("congrats you have sabotaged your neighbor", SLOW_PRINT_SPEED)
                    mission.completed = True
                    missions_completed += 1
                    slow_print(f"Missions completed: {missions_completed}/5", SLOW_PRINT_SPEED)
                else:
                    slow_print("You failed to sabotage your neighbor", SLOW_PRINT_SPEED)
                    failed_missions += 1
                    slow_print(f"Missions failed: {failed_missions}/3", SLOW_PRINT_SPEED)
                    neighbor_gets_closer(neighbor, player, rooms)
            else:
                slow_print("No available sabotage missions in this room.", SLOW_PRINT_SPEED)
            input("Press Enter to continue")
#the neighbor gets close when a sabotage mission is failed
        elif command == "listen":
            listen_for_neighbor(player, neighbor,rooms)
            input("Press Enter to continue")

        elif command == "status":
            show_status(player, neighbor, missions_completed, failed_missions)
            input("Press Enter to continue")
        
        elif command == "help":
            show_help()
            input("Press Enter to continue")

        else:
            slow_print("invalid command, type 'help for list of commands.", SLOW_PRINT_SPEED)
            input("Press Enter to continue")

    if not game_over:
        slow_print("Thank you for playing Sabotage Your Neighbor", 0.03)

def move_neighbor(neighbor, rooms):
    current_room = rooms[neighbor.current_room]
    neighbor.current_room = random.choice(current_room.conected_rooms)
    
    neighbor.move_count += 1

    if neighbor.move_count % 3 == 0:
        next_room = rooms[neighbor.current_room]
        neighbor.current_room = random.choice(next_room.conected_rooms)

def display_location(player, room, neighbor, rooms, missions):
    clear_screen()
    slow_print(f"You are in the {room.name}.", SLOW_PRINT_SPEED)
    slow_print(f"Turn: {player.turn_count}", SLOW_PRINT_SPEED)

    connected = ", ".join(room.conected_rooms)
    slow_print(f"Connected rooms: {connected}", SLOW_PRINT_SPEED)
    connected = ",".join(room.conected_rooms)
    slow_print(f"Connected rooms: {connected}", SLOW_PRINT_SPEED)
#this checks for available sabotages in the current room    
    available_missions = [m for m in missions if m.room == room.name and not m.completed]
    if available_missions:
        slow_print("There are available sabotages in this room (use 'sabotage')", SLOW_PRINT_SPEED)
#these are all the available actions 
    slow_print("\nAvailable actions:", SLOW_PRINT_SPEED)
    slow_print("- move to [room name]", SLOW_PRINT_SPEED)
    slow_print("- listen (for neighbor)", SLOW_PRINT_SPEED)
    slow_print("- Status", SLOW_PRINT_SPEED)
    slow_print("- help", SLOW_PRINT_SPEED)
    if available_missions:
        slow_print("- sabotage", SLOW_PRINT_SPEED)
#generates random math problems for the player to solve   
def solve_math_problem():
    num1 = random.radint(1, 20)
    num2 = random.radint(1, 20)
    operation = random.choice(["+", "-", "*"])
    if operation == "+":
        answer = num1 + num2
        problem = f"What is {num1} + {num2}?"
    elif operation == "-":
        if num1 < num2:
            num1, num2 = num2, num1

        answer = num1 - num2
        problem = f"what is {num1} * {num2}?"
    else:
        num1 = random.radint(1, 10)
        num2 = random.radint(1, 10)
        answer = num1 * num2
        problem = f"What is {num1} * {num2}?"

    slow_print("\nAnswer math problem to complete sabotage:", SLOW_PRINT_SPEED)
    slow_print(problem, SLOW_PRINT_SPEED)

    try:
        user_answer = int(input("Your answer: ").strip())
        return user_answer == answer
    except ValueError:
        slow_print("answer not valid", SLOW_PRINT_SPEED)
        return False
#this moves the neighbor one step closer to the player
def neighbor_gets_closer(neighbor, player, rooms):
    path = find_path_to_player(neighbor.current_room, player.current_room, rooms)
    if len(path) > 1:
        neighbor.current_room = path[1]
        slow_print("You just heard your neighbor get closer, careful", SLOW_PRINT_SPEED)

def find_path_to_player(start_room, target_room, rooms):
    queue = [[start_room]]
    visited = set([start_room])

    while queue:
        path = queue.pop(0)
        current = path [-1]

        if current == target_room:
            return path
        
        for next_room in rooms[current].conected_rooms:
            if next_room not in visited:
                visited.add(next_room)
                new_path = list(path)
                new_path.append(next_room)
                queue.append(new_path)
    return [start_room]

def listen_for_neighbor(player, neighbor, rooms):
    distance = len(find_path_to_player(player.current_room, neighbor.current_room, rooms)) - 1
#these are hints to where the neighbor is
    if distance == 0:
        slow_print("Run!!! your neighbor is in this room!!!", SLOW_PRINT_SPEED)
    elif distance == 1:
        slow_print("You just heard your neighbor in a connected room careful", SLOW_PRINT_SPEED)
    elif distance == 2:
        slow_print("Your neighbor's footsteps are not too far away watch out", SLOW_PRINT_SPEED)
    else:
        slow_print("You hear your neighbor upstairs so you are good for now", SLOW_PRINT_SPEED)

    slow_print(f"Your neighbor is in the {neighbor.current_room}", SLOW_PRINT_SPEED)

def show_status(player, neihgbor, missions_completed, failed_missions):
    clear_screen()
    slow_print("== STATUS ==", SLOW_PRINT_SPEED)
    slow_print(f"Current room: {player.current_room}", SLOW_PRINT_SPEED)
    slow_print(f"Missions completed: {missions_completed}/5", SLOW_PRINT_SPEED)
    slow_print(f"Missions failed: {failed_missions}/3", SLOW_PRINT_SPEED)
    slow_print(f"Turns played: {player.turn_count}", SLOW_PRINT_SPEED)

def show_game_over(message, success):
    clear_screen()
    if success:
        slow_print("== VICTORY ==", 0.03)
    else:
        slow_print("== GAME OVER", 0.03)

    slow_print(message, 0.03)
    input("\nPress Enter to exit game")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGame ended by user")
    except Exception as e:
        print(f"An error has occurred: {e}")
            