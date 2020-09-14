import pygame

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