"""
Text Adventure Game - Room Class

Learn about:
- Classes and objects
- Instance variables (attributes)
- Methods
- String representation
"""

# TODO: Create a class called 'Room'
# Type: class Room(
# Tab will suggest class syntax

class Room:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

    def add_exit(self, direction: str, room):
        self.exits[direction] = room

    def get_exits(self) -> list:
        return list(self.exits.keys())

    def __str__(self) -> str:
        exits_str = ", ".join(self.get_exits()) if self.exits else "none"
        return f"{self.name}\n{self.description}\nExits: {exits_str}"

# TODO: Add an __init__ method that takes name and description
# Type: def __init__(self,
# Tab will help complete the method signature
living_room = Room("Living Room", "A room with a couch and a TV")

# TODO: Add instance variables
# Type: self.name = 
# Tab will suggest based on parameter names
print(living_room)

# TODO: Create a dictionary to store exits (north, south, east, west)
# Type: self.exits = 
# Tab will suggest dictionary syntax
living_room.add_exit("north", bedroom)

# TODO: Create a list to store items in the room
# Type: self.items = 
# Tab will suggest list syntax
living_room.items.append(Item("TV", "A TV"))

# TODO: Add a method to add an exit
# Type: def add_exit(self,
# Tab will help with method syntax
living_room.add_exit("north", bedroom)

# TODO: Add a method to get available exits
# Type: def get_exits(self):
# Tab will suggest method patterns
print(living_room.get_exits())

# TODO: Add __str__ method for string representation
# Type: def __str__(self):
# Tab will suggest magic methods
print(living_room)

# Example structure (type this yourself!):
# class Room:
#     def __init__(self, name: str, description: str):
#         self.name = name
#         self.description = description
#         self.exits = {}  # Dictionary: direction -> Room object
#         self.items = []  # List of Item objects
#     
#     def add_exit(self, direction: str, room):
#         """Add an exit to another room"""
#         self.exits[direction] = room
#     
#     def get_exits(self) -> list:
#         """Return list of available exit directions"""
#         return list(self.exits.keys())
#     
#     def __str__(self) -> str:
#         """String representation of the room"""
#         exits_str = ", ".join(self.get_exits()) if self.exits else "none"
#         return f"{self.name}\n{self.description}\nExits: {exits_str}"

# TODO: Create a test room
# Type: living_room = Room(
# Tab will show you the constructor parameters
living_room = Room("Living Room", "A room with a couch and a TV")

# TODO: Print the room
# Type: print(
# Tab will suggest available variables
print(living_room)
bedroom = Room("Bedroom", "A room with a bed and a dresser")
living_room.add_exit("north", bedroom)
living_room.items.append(Item("TV", "A TV"))
print(living_room.get_exits())
print(living_room)
print(bedroom)

