"""
Text Adventure Game - Player Class

Learn about:
- State management
- Collections (lists, dictionaries)
- Methods that modify state
"""

# TODO: Create a Player class
# Type: class Player(
# Tab will suggest class syntax

# TODO: Add __init__ with name and starting room
# Type: def __init__(self, name: str, current_room):
# Tab will help with parameters

# TODO: Create inventory list
# Type: self.inventory = 
# Tab will suggest list syntax

# TODO: Add health attribute (default 100)
# Type: self.health = 
# Tab will suggest assignment

# TODO: Create method to move to a room
# Type: def move(self,
# Tab will suggest method syntax

# TODO: Create method to pick up item
# Type: def take_item(self,
# Tab will suggest method patterns

# TODO: Create method to drop item
# Type: def drop_item(self,
# Tab will suggest similar patterns

# TODO: Create method to show inventory
# Type: def show_inventory(self):
# Tab will suggest method patterns

# Example (type this yourself):
# class Player:
#     def __init__(self, name: str, current_room):
#         self.name = name
#         self.current_room = current_room
#         self.inventory = []  # List of Item objects
#         self.health = 100
#     
#     def move(self, direction: str) -> bool:
#         """Move player to a new room. Returns True if successful."""
#         if direction in self.current_room.exits:
#             self.current_room = self.current_room.exits[direction]
#             return True
#         return False
#     
#     def take_item(self, item_name: str) -> bool:
#         """Take an item from current room. Returns True if successful."""
#         for item in self.current_room.items:
#             if item.name.lower() == item_name.lower():
#                 self.current_room.items.remove(item)
#                 self.inventory.append(item)
#                 return True
#         return False
#     
#     def drop_item(self, item_name: str) -> bool:
#         """Drop an item in current room. Returns True if successful."""
#         for item in self.inventory:
#             if item.name.lower() == item_name.lower():
#                 self.inventory.remove(item)
#                 self.current_room.items.append(item)
#                 return True
#         return False
#     
#     def show_inventory(self) -> str:
#         """Return formatted inventory list"""
#         if not self.inventory:
#             return "Your inventory is empty."
#         items = [item.name for item in self.inventory]
#         return f"Inventory: {', '.join(items)}"
#     
#     def get_status(self) -> str:
#         """Return player status"""
#         return f"Health: {self.health}% | Location: {self.current_room.name}"

# TODO: Test player creation
# Type: player = Player(
# Tab will show constructor parameters


