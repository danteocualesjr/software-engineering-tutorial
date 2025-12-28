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


# Test the Room class
if __name__ == "__main__":
    # Create rooms first (before using them!)
    living_room = Room("Living Room", "A room with a couch and a TV")
    bedroom = Room("Bedroom", "A room with a bed and a dresser")
    
    # Now connect them
    living_room.add_exit("north", bedroom)
    bedroom.add_exit("south", living_room)
    
    # Test printing
    print("=== Testing Room Class ===\n")
    print(living_room)
    print("\n" + "="*30 + "\n")
    print(bedroom)
    print("\nExits from living room:", living_room.get_exits())
    print("Exits from bedroom:", bedroom.get_exits())
    
    # For now, use strings instead of Item objects (until you create Item class)
    living_room.items.append("TV")
    print("\nItems in living room:", living_room.items)

