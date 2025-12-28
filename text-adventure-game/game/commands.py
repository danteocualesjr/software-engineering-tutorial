"""
Text Adventure Game - Command Parser

Learn about:
- String manipulation
- Parsing user input
- Command pattern
- Error handling
"""

# TODO: Create a function to parse user command
# Type: def parse_command(command: str):
# Tab will help with function syntax

# TODO: Split command into words
# Type: words = command.
# Tab will suggest string methods like .split()

# TODO: Return command and arguments
# Type: return 
# Tab will suggest return patterns

# Example (type this yourself):
# def parse_command(command: str) -> tuple:
#     """Parse user command into action and arguments"""
#     words = command.strip().lower().split()
#     if not words:
#         return None, []
#     action = words[0]
#     args = words[1:] if len(words) > 1 else []
#     return action, args

# TODO: Create a function to handle commands
# Type: def handle_command(action: str, args: list, player):
# Tab will help with function signature

# Example command handler (type this yourself):
# def handle_command(action: str, args: list, player) -> str:
#     """Handle player commands and return response"""
#     if action == "go" or action == "move":
#         if args:
#             direction = args[0]
#             if player.move(direction):
#                 return f"You go {direction}.\n{player.current_room}"
#             else:
#                 return f"You can't go {direction}!"
#         else:
#             return "Go where? (north, south, east, west)"
#     elif action == "look":
#         return str(player.current_room)
#     elif action == "inventory" or action == "inv":
#         return player.show_inventory()
#     elif action == "take" or action == "get":
#         if args:
#             item_name = " ".join(args)
#             if player.take_item(item_name):
#                 return f"You take the {item_name}."
#             else:
#                 return f"There is no {item_name} here."
#         else:
#             return "Take what?"
#     elif action == "drop":
#         if args:
#             item_name = " ".join(args)
#             if player.drop_item(item_name):
#                 return f"You drop the {item_name}."
#             else:
#                 return f"You don't have a {item_name}."
#         else:
#             return "Drop what?"
#     elif action == "status":
#         return player.get_status()
#     elif action == "help":
#         return """Available commands:
# - go [direction]: Move north, south, east, or west
# - look: Look around the current room
# - take [item]: Pick up an item
# - drop [item]: Drop an item
# - inventory: Show your inventory
# - status: Show your health and location
# - quit: Exit the game"""
#     elif action == "quit" or action == "exit":
#         return "quit"
#     else:
#         return f"I don't understand '{action}'. Type 'help' for commands."

# TODO: Test command parsing
# Type: action, args = parse_command(
# Tab will show function signature


