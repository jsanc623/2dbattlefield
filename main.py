STATE_OK = 1
STATE_POISONED = 0
STATE_DEAD = -1

MAX_HEALTH = 100

INCREMENT = 1
DECREMENT = -1

class Fighter:
    def __init__(self, position):
        self.state = STATE_OK
        self.health = MAX_HEALTH
        self.position = position
    
    def state(self, state):
        self.state = state
    
    def health(self, amount, op=INCREMENT):
        if op == INCREMENT:
            self.health += amount
        elif op == DECREMENT:
            self.health -= amount
        
        if self.health <= 0:
            self.state(STATE_DEAD)
    
    def move(self, position):
        self.position = position

class Board:
    def __init__(self):
        pass
    
    def create(self, x=50, y=50):
        self.x = x
        self.y = y
        self.board = [[0 for x in range(self.x)] for x in range(self.y)]

class Game():
    def __init__(self, max_x, max_y):
        self.board = Board()
        self.board.create(max_x, max_y)
        
        self.player_one = Fighter([0,0])
        self.player_two = Fighter([max_x,max_y])
    
    def run(self):
        pass

Game = Game(50, 50)
Game.run()
