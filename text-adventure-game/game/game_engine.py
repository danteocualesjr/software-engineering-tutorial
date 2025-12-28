"""
Text Adventure Game - Game Engine

Learn about:
- Game loops
- Control flow
- Error handling
- Program structure
"""

from .player import Player
from .room import Room
from .item import Item
from .commands import parse_command, handle_command

# TODO: Create a function to initialize the game world
# Type: def create_world():
# Tab will suggest function syntax

# TODO: Create rooms
# Type: living_room = Room(
# Tab will show constructor

# TODO: Connect rooms with exits
# Type: living_room.add_exit(
# Tab will show method signature

# Example (type this yourself):
# def create_world():
#     """Create and connect all rooms in the game"""
#     # Create rooms
#     living_room = Room(
#         "Living Room",
#         "A cozy living room with a fireplace. There's a door to the north."
#     )
#     
#     kitchen = Room(
#         "Kitchen",
#         "A modern kitchen with stainless steel appliances. A door leads south."
#     )
#     
#     bedroom = Room(
#         "Bedroom",
#         "A comfortable bedroom with a large window. The door is to the south."
#     )
#     
#     # Connect rooms
#     living_room.add_exit("north", bedroom)
#     living_room.add_exit("south", kitchen)
#     bedroom.add_exit("south", living_room)
#     kitchen.add_exit("north", living_room)
#     
#     # Add items
#     key = Item("key", "A shiny golden key", 0.1)
#     sword = Item("sword", "A sharp steel sword", 2.5)
#     book = Item("book", "An old leather-bound book", 0.8)
#     
#     living_room.items.append(key)
#     bedroom.items.append(sword)
#     kitchen.items.append(book)
#     
#     return living_room

# TODO: Create main game loop function
# Type: def run_game():
# Tab will suggest function syntax

# TODO: Create player
# Type: player = Player(
# Tab will show constructor

# TODO: Create game loop with while True
# Type: while True:
# Tab will suggest loop syntax

# TODO: Get user input
# Type: command = input(
# Tab will suggest input() function

# TODO: Parse and handle command
# Type: action, args = parse_command(
# Tab will show function signature

# Example game loop (type this yourself):
# def run_game():
#     """Main game loop"""
#     print("Welcome to the Text Adventure Game!")
#     print("Type 'help' for commands.\n")
#     
#     start_room = create_world()
#     player = Player("Adventurer", start_room)
#     
#     print(f"You are in the {player.current_room.name}")
#     print(player.current_room.description)
#     
#     while True:
#         try:
#             command = input("\n> ").strip()
#             
#             if not command:
#                 continue
#             
#             action, args = parse_command(command)
#             response = handle_command(action, args, player)
#             
#             if response == "quit":
#                 print("Thanks for playing!")
#                 break
#             
#             print(response)
#             
#         except KeyboardInterrupt:
#             print("\n\nGame interrupted. Goodbye!")
#             break
#         except Exception as e:
#             print(f"An error occurred: {e}")
#             print("Please try again.")

# TODO: Add error handling with try/except
# Type: try:
# Tab will suggest try/except syntax


