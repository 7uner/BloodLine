#########################################
# Programmer: Mr. G
# Date: 02/06/2014
# File Name: explosion_demo.py
# Description: Demonstrates how to implement animated sprites
#########################################
import pygame
pygame.init()

game_window = pygame.display.set_mode((800,600))
white = ( 0, 0, 0)

clock = pygame.time.Clock()

#---------------------------------------#
#   classes                             #
#---------------------------------------#
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, numImages = 1, x = 0, y = 0):
        pygame.sprite.Sprite.__init__(self)
        self.visible = False
        self.index = 0
        self.numImages = numImages
        
        self.sheet = blend_image(sprite_sheet)
        sheetrect = self.sheet.get_rect()     
        self.width,self.height = sheetrect.width, sheetrect.height
        self.width = self.width/numImages
        self.rect = pygame.Rect(x,y,self.width,self.height)
        self.update()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def load_next(self):
        self.index = (self.index + 1)%self.numImages
        self.update()

    def update(self):
        self.sheet.set_clip(self.width*self.index,0, self.width, self.height)
        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def spawn(self, x, y):
        self.rect = pygame.Rect(x,y,self.width,self.height)
        self.visible = True

    def redraw_game_window(self):
        game_window.fill(white)
        if explosion.visible:
            explosion.draw(game_window)
            explosion.load_next() 
            if explosion.index == 0:
                explosion.visible = False
        pygame.display.update()

    def blend_image(self, file_name):                 
        image_surface = pygame.image.load(file_name)
        image_surface = image_surface.convert() 
        colorkey = image_surface.get_at((0,0))  
        image_surface.set_colorkey(colorkey)    
        return image_surface                    

    def activate_sprite(self,x, y):
        explosion.spawn(x,y)
            
#---------------------------------------#
#   functions                           #
#---------------------------------------#
def redraw_game_window():
    game_window.fill(white)
    if explosion.visible:
        explosion.draw(game_window)
        explosion.load_next() 
        if explosion.index == 0:
            explosion.visible = False
    pygame.display.update()

def blend_image(file_name):                 
    image_surface = pygame.image.load(file_name)
    image_surface = image_surface.convert() 
    colorkey = image_surface.get_at((0,0))  
    image_surface.set_colorkey(colorkey)    
    return image_surface                    

def activat_sprite(x, y):
    explosion.spawn(x,y)
#---------------------------------------#
# main program starts here              #
#---------------------------------------#     


explosion = AnimatedSprite("images/atk2.png",26)
inPlay = True
print ("Cilck with the mouse inside the game window.")


    
while inPlay:               
                
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inPlay = False
            if event.key == pygame.K_z:
                explosion.spawn(200,200) 
                
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:       #when the user clicks on the left button
                x,y = pygame.mouse.get_pos()
                explosion.spawn(x,y)
                
    clock.tick(15)
    redraw_game_window()
    
pygame.quit()

  
