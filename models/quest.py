class Quest:
    """
    Represents a quest for the player to complete.
    """
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def complete(self, player):
        if not self.completed:
            print(f"Quest Completed: {self.title}!")
            self.completed = True
        else:
            print(f"Quest already completed!")
