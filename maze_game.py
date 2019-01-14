import pygame
pygame.init()

block_height = 7
block_width = 7

win_height = 84 * block_height
win_width = 83 * block_width

#Set window dimensions as per components
# def setWinSize(level):
#     win_height = block_height * len(level)
#     win_width = block_width * (len(level[0]) + )

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Game")

#Load images
char = pygame.image.load('./img/player.jpg')
wall = pygame.image.load('./img/wall.jpg')
black = pygame.image.load('./img/black.jpg')
victory = pygame.image.load('./img/victory.jpg')

#Load music
pygame.mixer.music.load('./music/music1.mp3')
pygame.mixer.music.play(-1)

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = block_width
        self.height = block_height
        self.vel_y = block_height
        self.vel_x = block_width
        self.prev_loc = {'x':x, 'y':y}

    def move(self, keys):
        new_x = self.x
        new_y = self.y
        self.prev_loc['x'] = self.x
        self.prev_loc['y'] = self.y

        if keys[pygame.K_LEFT] and self.x > self.vel_x:
            new_x = self.x - self.vel_x
    
        if keys[pygame.K_RIGHT] and self.x <= win_width - self.width - self.vel_x:
            new_x = self.x + self.vel_x

        if keys[pygame.K_UP] and self.y > self.vel_y:
            new_y = self.y - self.vel_y

        if keys[pygame.K_DOWN] and self.y <= win_height - self.height - self.vel_y:
            new_y = self.y + self.vel_y
        
        

        if (new_x, new_y) not in walls:
            self.x = new_x
            self.y = new_y

    def draw(self, win):
        win.blit(char, (self.x, self.y))    
        
def redrawGameWindow():
    #cover old spot
    win.blit(black, (player.prev_loc['x'], player.prev_loc['y']))        
    #draw on new spot
    player.draw(win)
    
    pygame.display.update()

#Read level from file
level_file = []
f = open('./img/maze.txt', 'r')
level_file =f.readlines()
f.close()

#Setup Maze
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]

            if character == 'x':
                win.blit(wall, (x * block_width, y * block_height))
                walls.append((x * block_width, y * block_height))
                
    pygame.display.update()
            

#When maze is cleared
def gameEnd():
    win.blit(victory, (0,0))            
    pygame.display.update()    
   
"""Setup Game
    Players, Maze, Game Loop"""
    
#Create player
player = Player(0, 40 * block_height)

#Walls array
walls = []

#Create Maze
setup_maze(level_file)
maze = wall

#Game Loop
run = True
canMove = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    keys = pygame.key.get_pressed()
    if canMove:
        player.move(keys)

    if (player.x, player.y) not in [(82 * block_width, 40 * block_height), (82 * block_width, 41 * block_height)]:
        redrawGameWindow() 
    else :
        gameEnd()
        canMove = False
            
pygame.quit()