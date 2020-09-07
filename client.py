import pygame
from network import Network

width = 500
height = 500
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("client")

clientnumber = 0

class Player():

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.val = 1

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

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

        self.rect = (self.x, self.y, self.width, self.height)

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str(1))

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def redrawwindow(win,player):

    win.fill((255,255,255))
    player.draw(win)
    pygame.display.update()

def main():
    run = True
    n = Network()
    startpos = read_pos(n.getpos())
    p = Player(startpos[0],startpos[1],100,100,(0,255,0))
    p2 = Player(0,0,100,100,(0,255,0))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawwindow(win,p)

main()