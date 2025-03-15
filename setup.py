#this is the abilities file
#commit test 
#input()
#print (abilities)
from classes import Player 
from classes import Neighbor 
from classes import Room
from classes import Mission
from utils import clear_screen, slow_print
SLOW_PRINT_SPEED = 0.01
def initalize_game():
    "Set up the game environment and all game objects."

    rooms={
        "Living Room": Room ("Living Room", ["Kitchen", "Hallway"]),
        "Kitchen" : Room ("Kitchen",["Living Room", "Backyard"]),
        "Hallway": Room ("Hallway", ["Living Room", "Bedroom", "Bathroom"]),
        "Bedroom": Room ("Bedroom", ["Hallway","Office"]),
        "Bathroom": Room ("Bathroom", ["Hallway"]),
        "Office": Room ("Office", ["Bedroom"]),
        "Backyard": Room ("Backyard", ["Kitchen"]),
    }

    missions = [
        Mission ("Hide the TV remote under the couch cushions", "Living Room"),
        Mission ("Switch the sugar with the salt", "Kitchen"),
        Mission ("Set all the clocks to diffrent times","Living Room"),
        Mission ("Unplug the WiFi router", "Office"),
        Mission ("Move your neighbor's car keys", "Hallway"),
        Mission ("Turn off the hot water in the shower", "Bathroom"),
        Mission ("Hide important papers in the wrong folders", "Office"),
        Mission ("Rearrange items in the refrigerator", "Kitchen"),
        Mission ("Change the thermostat settings","Hallway"),
        Mission ("Replace regular coffee with decaf", "Kitchen"),
        Mission ("Put plastic wrap on the toilet seat", "Bathroom"),
        Mission ("Take all the pens from the desk", "Office"),
        Mission ("Turn alarms off on your neighbor's phone", "Bedroom"),
        Mission ("Slightly move furniture so they stub their toe", "Living Room"),
        Mission ("Leave the tap dripping slightly", "Bathroom"),
    ]

    player = Player ("Sabatager")

    neighbor = Neighbor ("Mr.Powers")

    return player,neighbor, rooms, missions

def show_intro():
    "Display the game introduction"
    clear_screen()
    slow_print("NEIGHBOR SABOTAGE", SLOW_PRINT_SPEED)
    slow_print("================", SLOW_PRINT_SPEED)
    slow_print("\nYour neighvor has been annoying you for months with loud music and parties.", SLOW_PRINT_SPEED)
    slow_print("It's time for revenge ! Sneak ibto their house and sabotage their daily routine.", SLOW_PRINT_SPEED)
    slow_print("Complete 5 sabotage missions before you get caught or faail 3 times.", SLOW_PRINT_SPEED)
    slow_print("Your neighbor is moving around the house - listen for their location and avoid them!", SLOW_PRINT_SPEED)
    slow_print("\nCommands:", SLOW_PRINT_SPEED)
    slow_print("- move to [room name]: Go to a connected room", SLOW_PRINT_SPEED)
    slow_print("- sabotage: Attempt to complete a sabotage mission in the current room", SLOW_PRINT_SPEED)
    slow_print("- listen: Try to hear where your neighbor is", SLOW_PRINT_SPEED)
    slow_print("- ststus: Check your progress", SLOW_PRINT_SPEED)
    slow_print("- help: Show availbe commands", SLOW_PRINT_SPEED)
    slow_print("- quit: Exit the game", SLOW_PRINT_SPEED)
    slow_print("\nTo Complete a sabotage, you'll need to anwser a math questoion correctly.", SLOW_PRINT_SPEED)
    slow_print("If you get it wrong, the neighhbor will move closer to your location!", SLOW_PRINT_SPEED)
    slow_print("\nGood luck, and don't get caught!", SLOW_PRINT_SPEED)
    input("\nPress Enter to start the game")

def show_help():
    "Display available commands."
    slow_print("\nCommands:", SLOW_PRINT_SPEED)
    slow_print("- move to [room nam]: Go to a connected room", SLOW_PRINT_SPEED)
    slow_print("- sabotage: Attempt to complete a sabotage mission in the current room", SLOW_PRINT_SPEED)
    slow_print("- status: Check your progress", SLOW_PRINT_SPEED)
    slow_print("- help: Show available commands", SLOW_PRINT_SPEED)
    slow_print("- quit: Exit the game", SLOW_PRINT_SPEED)
