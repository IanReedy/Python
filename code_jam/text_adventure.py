class Game:
    def __init__(self):
        self.current_room = 'entrance'
        self.inventory = []

    def start(self):
        print("Welcome to the Adventure Game!")
        while True:
            if self.current_room == 'entrance':
                self.entrance()
            elif self.current_room == 'hallway':
                self.hallway()
            elif self.current_room == 'treasure_room':
                self.treasure_room()
            elif self.current_room == 'library':
                self.library()
            elif self.current_room == 'dungeon':
                self.dungeon()

    def entrance(self):
        print("\nYou are at the entrance of a dark cave.")
        print("There are two paths: one leads to a hallway, and the other leads back home.")
        action = input("Type 'hallway' to go to the hallway or 'home' to go back: ").strip().lower()

        if action == 'hallway':
            self.current_room = 'hallway'
        elif action == 'home':
            print("You chose to go back home. Game over!")
            exit()
        else:
            print("Invalid choice. Try again.")

    def hallway(self):
        print("\nYou are in a dimly lit hallway.")
        print("There are doors to the left and right, and a staircase going up.")
        action = input("Type 'left' to go through the left door, 'right' for the right door, or 'up' for the staircase: ").strip().lower()

        if action == 'left':
            self.current_room = 'library'
        elif action == 'right':
            self.current_room = 'dungeon'
        elif action == 'up':
            print("You climb the staircase and find yourself in a different part of the cave.")
            print("You can go back down or explore further.")
            action = input("Type 'down' to go back down or 'explore' to continue: ").strip().lower()
            if action == 'down':
                self.current_room = 'entrance'
            elif action == 'explore':
                print("You found a hidden passage that leads to an exit. You escaped!")
                exit()
            else:
                print("Invalid choice. Try again.")
        else:
            print("Invalid choice. Try again.")

    def library(self):
        print("\nYou enter a dusty old library filled with ancient books.")
        print("There’s a mysterious book on a pedestal and a door back to the hallway.")
        action = input("Type 'read' to read the book or 'back' to return: ").strip().lower()

        if action == 'read':
            print("The book reveals the location of a hidden treasure! You've gained a clue!")
            self.inventory.append("treasure clue")
        elif action == 'back':
            self.current_room = 'hallway'
        else:
            print("Invalid choice. Try again.")

    def dungeon(self):
        print("\nYou find yourself in a dark, damp dungeon.")
        print("There are chains on the walls and a guard watching over a treasure chest.")
        if "treasure clue" in self.inventory:
            print("You can use the clue to distract the guard.")
            action = input("Type 'distract' to distract the guard or 'back' to return: ").strip().lower()

            if action == 'distract':
                print("You distract the guard with the clue and manage to open the chest!")
                print("You've found the treasure! You've won the game!")
                exit()
            elif action == 'back':
                self.current_room = 'hallway'
            else:
                print("Invalid choice. Try again.")
        else:
            action = input("Type 'back' to return: ").strip().lower()
            if action == 'back':
                self.current_room = 'hallway'
            else:
                print("Invalid choice. Try again.")

    def treasure_room(self):
        print("\nYou are in the treasure room, surrounded by gold and jewels.")
        print("You can go back to the hallway.")
        action = input("Type 'back' to return: ").strip().lower()

        if action == 'back':
            self.current_room = 'hallway'
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    game = Game()
    game.start()
