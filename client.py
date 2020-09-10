# importing few things
import pygame
from network import Network

# width and height for game window
width = 500
height = 500
# seting up window
win = pygame.display.set_mode((width,height))
# seting window title to be "client"
pygame.display.set_caption("client")

# variable that stores clients no.
clientnumber = 0

# player class
class Player():

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.val = 1
    
    # function to create a box on the screen
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    # function to set movement of box
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.val
            
        if keys[pygame.K_RIGHT]:
            self.x += self.val

        if keys[pygame.K_UP]:
            self.y -= self.val

        if keys[pygame.K_DOWN]:
            self.y += self.val

        self.update()

    def update(self):
        # changing box's x,y axis a box again
        self.rect = (self.x, self.y, self.width, self.height)

# function that convert positon string into a tuple
# for example "23,24" to (23,24)
def read_pos(str):
    # spliting the string from ","
    str = str.split(",")
    # returning tuple
    return int(str[0]), int(str[1])

# function to convert position tuple into a string
# reverse of read_pos()
def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

# function to draw box on screen and update the screen
def redrawwindow(win,player,player2):
    # filling the screen with white color
    win.fill((255,255,255))
    # drawing an box on window
    player.draw(win)
    player2.draw(win)
    # updating the display
    pygame.display.update()

# main function
def main():
    # setting run variable True
    run = True
    # creating a Network class object
    n = Network()
    # converting and storing the pos. tuple in startpos variable
    startpos = read_pos(n.getpos())
    print(startpos)
    # creating 1st player
    p = Player(startpos[0],startpos[1],100,100,(0,255,0))
    # creating 2nd player
    p2 = Player(0,0,100,100,(0,255,0))
    print(p.x,p.y)
    # game loop
    while run:
        # sending player1's position and recieving player2's position in tuple
        p2pos = read_pos(n.send(make_pos((p.x,p.y))))
        # assigning player2's x cordinate
        p2.x = p2pos[0]
        # assigning player2's y cordinate
        p2.y = p2pos[1]
        #
        p2.update()

        # checking for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # setting the run variable False
                run = False
                pygame.quit()
        # calling move methode from player class
        p.move()
        # redrawing box and updating screen
        redrawwindow(win,p,p2)

# calling the main function
main()