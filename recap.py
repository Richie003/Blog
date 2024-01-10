class Car:
    def __init__(self):
        self.name = "Chevrolet"
        self.color = "blue"
        self.length = "20m"
        self.height = "3fts"
        self.tires = 4
    
    
    def change_color(self, color):
        self.color = color
        notification = f"Your {self.name} is now {self.color}"
        return notification
    
    @property
    def move(self):
        move = "The car is moving at a speed 20km/hr"
        return move
    
    @property
    def park(self):
        park_statement = f"Your {self.name} is stationary or parked"
        return park_statement