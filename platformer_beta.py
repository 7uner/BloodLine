import pygame
import AI
import enemy_animation
import tkinter as tk
import random
from pygame.locals import *
import sys

#############
#Splash Page#
#############

root = tk.Tk()
# show no frame
root.overrideredirect(True)
width = 900
height = 550
root.geometry('%dx%d+%d+%d' % (width*0.8, height*0.8, width*0.1, height*0.1))
image_file = "Splash_Page.gif"
# use Tkinter's PhotoImage for .gif files
image = tk.PhotoImage(file=image_file)
canvas = tk.Canvas(root, height=height*0.8, width=width*0.8, bg="brown")
canvas.create_image(width*0.8/2, height*0.8/2, image=image)
canvas.pack()
# show the splash screen for 3000 milliseconds then destroy
root.after(3000, root.destroy)
root.mainloop()

#####################################################

current_level_no = 0 #start from level 1
reset = True    #game is starting from beginning
game_loop = True    #play the game

while game_loop == True:
    counter = 0
    
    # Global Constants
    global ground#the ground
    global player_image#the player
    global PLATFORM#the level
    global background#the background photo
    global direction
    global is_attacking
    global is_jumping
    global is_idle
    global is_running
    global atk_type
    global is_attacked
    global is_dead
    global animation_delay
    global boss_is_dead
    global boss_is_spawn
    global creep_is_spawn
    global random_atk_generated
    global danger_zone_counter
    global stun_counter
    global icon_1
    global icon_2
    global icon_3
    global icon_4
    global icon_5
    global boss_health_bar_list
    global boss_health_bar
    global potion_icon
    global scene_1_spawn
    global scene_2_spawn
    global scene_3_spawn
    global ai_dont_attack
    global explosion
    global animation_time
    global intro_counter
    
    # Colors
    BLACK    = (   0,   0,   0)
    WHITE    = ( 255, 255, 255)
    BLUE     = (   0,   0, 255)
    RED      = ( 255,   0,   0)
    GREEN    = (   0, 255,   0)

    #loads all the images for the background and platforms
    platform_1 = pygame.image.load("backgrounds/platform_1.png")
    background_1 = pygame.image.load("backgrounds/background_1.png")
    platform_2 = pygame.image.load("backgrounds/platform_2.png")
    background_2 = pygame.image.load("backgrounds/background_2.png")
    platform_3 = pygame.image.load("backgrounds/platform_3.png")
    background_3 = pygame.image.load("backgrounds/background_3.jpg")
    platform_4 = pygame.image.load("backgrounds/platform_4.png")
    background_4 = pygame.image.load("backgrounds/background_4.jpg")
    platform_5 = pygame.image.load("backgrounds/platform_5.png")
    background_5 = pygame.image.load("backgrounds/background_5.jpg")

    #loads all the pictures involed in the HUD
    boarder = pygame.image.load("backgrounds/HUD/HUD.png")
    boss_1_healthbar = pygame.image.load("backgrounds/HUD/desertsolider_bar.png")
    boss_2_healthbar = pygame.image.load("backgrounds/HUD/ripper_bar.png")
    boss_3_healthbar = pygame.image.load("backgrounds/HUD/crab_bar.png")
    boss_4_healthbar = pygame.image.load("backgrounds/HUD/gladiator_bar.png")
    boss_5_healthbar = pygame.image.load("backgrounds/HUD/alex_bar.png")

    skill_z_icon = pygame.image.load("backgrounds/HUD/SKILLICONS/poke.png")
    skill_z_icon_NA = pygame.image.load("backgrounds/HUD/SKILLICONS/pokeN.png")
    skill_x_icon = pygame.image.load("backgrounds/HUD/SKILLICONS/slash.png")
    skill_x_icon_NA = pygame.image.load("backgrounds/HUD/SKILLICONS/slashN.png")
    skill_a_icon = pygame.image.load("backgrounds/HUD/SKILLICONS/3poke.png")
    skill_a_icon_NA = pygame.image.load("backgrounds/HUD/SKILLICONS/3pokeN.png")
    skill_s_icon = pygame.image.load("backgrounds/HUD/SKILLICONS/spinslash.png")
    skill_s_icon_NA = pygame.image.load("backgrounds/HUD/SKILLICONS/spinslashN.png")
    skill_d_icon = pygame.image.load("backgrounds/HUD/SKILLICONS/jumpslash.png")
    skill_d_icon_NA = pygame.image.load("backgrounds/HUD/SKILLICONS/jumpslashN.png")

    icon_1 = skill_z_icon
    icon_2 = skill_x_icon
    icon_3 = skill_a_icon
    icon_4 = skill_s_icon
    icon_5 = skill_d_icon

    boss_health_bar_list = [boss_1_healthbar,boss_2_healthbar,boss_3_healthbar,boss_4_healthbar,boss_5_healthbar]

    potion_icon = pygame.image.load("backgrounds/HUD/health_pot.png")
    #assigns background and platform based on level
    platform_image_list = [platform_1,platform_2,platform_3,platform_4,platform_5]
    background_image_list = [background_1,background_2,background_3,background_4,background_5]
    PLATFORM = platform_image_list[0]
    background = background_image_list[0]
    player_image = pygame.image.load("player/idle1.png")
    blank = pygame.image.load("player/blank.png")

    #load intro pages
    intro_1 = pygame.image.load("intro lore pg1.jpg")
    intro_2 = pygame.image.load("intro lore pg2.jpg")
    intro_list = [intro_1,intro_2]
    # all constants needed
    cut_check = False
    ground = 550
    direction = 0
    is_attacking = 0
    is_jumping = 0
    is_idle = 0
    is_running = 0
    is_attacked = 0
    is_dead = 0
    previous_direction = 0
    boss_is_dead = 0
    boss_is_spawn = 0
    creep_is_spawn = 0
    direction_change = False
    random_atk_generated = 0#this variable is used to limit the amount of times the random atk is generated for the bosses to 1 each time
    atk_type = 0
    spawn_point_counter = 0
    danger_zone_counter = 0
    stun_counter = 0
    intro_counter = 0
    scene_1_spawn = 0
    scene_2_spawn = 0
    scene_3_spawn = 0
    ai_dont_attack = 0
    boss_health_bar = 0
    atk_frame_list = [0, 26, 18, 9, 8, 6, 10]
    # Screen dimensions
    SCREEN_WIDTH  = 900
    SCREEN_HEIGHT = 550
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

###################
#     Classes     #
###################
    
    ############
    #Animations#
    ############

    class AnimatedSprite(pygame.sprite.Sprite):
        def __init__(self, sprite_sheet, numImages = 1, x = 0, y = 0):
            pygame.sprite.Sprite.__init__(self)
            self.visible = False
            self.index = 0
            self.numImages = numImages
            self.x = x
            self.y = y
            
            self.sheet = blend_image(sprite_sheet)
            sheetrect = self.sheet.get_rect()     
            self.width,self.height = sheetrect.width, sheetrect.height
            self.width = self.width/numImages
            self.rect = pygame.Rect(x,y,self.width,self.height)
            self.update()

        def draw(self, surface):
            surface.blit(self.image, (self.x,self.y))

        def load_next(self):
            self.index = (self.index + 1)%self.numImages
            self.update()

        def update(self):
            self.sheet.set_clip(self.width*self.index,0, self.width, self.height)
            self.image = self.sheet.subsurface(self.sheet.get_clip())
            
        def spawn(self, x, y):
            self.x = x
            self.y = y
            self.visible = True

    #-------------------------------------------------------------
            
    class attack(pygame.sprite.Sprite):
        def __init__(self,width,height):

            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface([width, height])
            self.rect = self.image.get_rect()

    #-------------------------------------------------------------
            
    class Player(pygame.sprite.Sprite):
        """ This class represents the bar at the bottom that the player
            controls. """

        # -- Attributes
        # Set speed vector of player
        change_x = 0
        change_y = 0

        # List of sprites we can bump against
        level = None

        # -- Methods
        def __init__(self):
            """ Constructor function """
            global player_image
            # Call the parent's constructor
            pygame.sprite.Sprite.__init__(self)

            # Create an image of the block, and fill it with a color.
            # This could also be an image loaded from the disk.
            width = 25
            height = 40
            self.image = pygame.Surface([width, height])

            # Set a referance to the image rect.
            self.rect = self.image.get_rect()
            self.image_x = self.rect.x-13
            self.image_y = self.rect.y
            self.animation_x = self.rect.x
            self.animation_y = self.rect.y
            self.health = 100
            self.mana = 100
            self.potion_no = 0

        def update(self):
            """ Move the player. """
            global danger_zone_counter
            # Gravity
            self.calc_grav()

            # Move left/right
            self.rect.x += self.change_x

            # See if we hit anything
            block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            for block in block_hit_list:
                # If we are moving right,
                # set our right side to the left side of the item we hit
                if self.change_x > 0:
                    self.rect.right = block.rect.left
                elif self.change_x < 0:
                    # Otherwise if we are moving left, do the opposite.
                    self.rect.left = block.rect.right

            # Move up/down
            self.rect.y += self.change_y

            # Check and see if we hit anything
            block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            for block in block_hit_list:

                # Reset our position based on the top/bottom of the object.
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top
                elif self.change_y < 0:
                    self.rect.top = block.rect.bottom
                    
                # Stop our vertical movement
                self.change_y = 0

            #if the player collides with the death zone, the player dies instantly
            death_hit_list = pygame.sprite.spritecollide(self, self.level.zone_list, False)
            for death in death_hit_list:
                danger_zone_counter=danger_zone_counter+1
                if danger_zone_counter == 5:
                    self.health = 0
                    self.change_x = 0
                
            #if the player picks up a potion pot, add it to its inventory
            potion_hit_list = pygame.sprite.spritecollide(self, self.level.potion_list, True)
            for potion in potion_hit_list:
                self.potion_no +=1
            #coordinates for animation and images based on state
            if direction == 0:
                if is_jumping == 0:
                    self.image_x=self.rect.x-38
                    self.image_y=self.rect.y
                if is_jumping == 1:
                    self.image_x=self.rect.x-45
                    self.image_y=self.rect.y-8
                if atk_type == 1:
                    self.animation_x = self.rect.x-120
                    self.animation_y = self.rect.y-7
                if atk_type == 2:
                    self.animation_x = self.rect.x-120
                    self.animation_y = self.rect.y-7
                if atk_type == 3:
                    self.animation_x = self.rect.x-123
                    self.animation_y = self.rect.y-10
                if atk_type == 4:
                    self.animation_x = self.rect.x-120
                    self.animation_y = self.rect.y-6
                if atk_type == 5:
                    self.animation_x = self.rect.x-120
                    self.animation_y = self.rect.y-9
                if atk_type == 6:
                    self.animation_x = self.rect.x-115
                    self.animation_y = self.rect.y-105
            if direction == 1:
                if is_jumping == 0:
                    self.image_x=self.rect.x-13
                    self.image_y=self.rect.y
                if is_jumping == 1:
                    self.image_x=self.rect.x-15
                    self.image_y=self.rect.y-8            
                if atk_type == 1:
                    self.animation_x = self.rect.x-10
                    self.animation_y = self.rect.y-7
                if atk_type == 2:
                    self.animation_x = self.rect.x-10
                    self.animation_y = self.rect.y-7
                if atk_type == 3:
                    self.animation_x = self.rect.x-60
                    self.animation_y = self.rect.y-15
                if atk_type == 4:
                    self.animation_x = self.rect.x-10
                    self.animation_y = self.rect.y-6
                if atk_type == 5:
                    self.animation_x = self.rect.x-10
                    self.animation_y = self.rect.y-9
                if atk_type == 6:
                    self.animation_x = self.rect.x-10
                    self.animation_y = self.rect.y-105
        #coordinates for death and got hit pictures
            if is_attacked == 1:
                player.image_y=player.rect.y-7
                if direction == 1:
                    player.image_x=player.rect.x-20
        def calc_grav(self):
            """ Calculate effect of gravity. """
            if self.change_y == 0:
                self.change_y = 1
            else:
                self.change_y += .76

            # See if we are on the ground.
            if self.rect.y >= ground-self.rect.height and self.change_y >= 0:
                self.change_y = 0
                self.rect.y = ground-self.rect.height

        def jump(self):
            """ Called when user hits 'jump' button. """

            # move down a bit and see if there is a platform below us.
            # Move down 2 pixels because it doesn't work well if we only move down 1
            # when working with a platform moving down.
            self.rect.y += 2
            platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
            self.rect.y -= 2

            # If it is ok to jump, set our speed upwards
            if len(platform_hit_list) > 0 or self.rect.bottom > ground-self.rect.height:
                self.change_y = -12
                
                

        # Player-controlled movement:
        def go_left(self):
            """ Called when the user hits the left arrow. """
            self.change_x = -6
            self.image_x=self.rect.x-13

        def go_right(self):
            """ Called when the user hits the right arrow. """
            self.change_x = 6
            self.image_x=self.rect.x+40
        def stop(self):
            """ Called when the user lets off the keyboard. """
            self.change_x = 0

    #----------------------------------------------------------------
            
    class Platform(pygame.sprite.Sprite):
        """ Platform the user can jump on """

        def __init__(self, width, height):
            """ Platform constructor. Assumes constructed with user passing in
                an array of 5 numbers like what's defined at the top of this
                code. """

            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface([width, height])
            self.rect = self.image.get_rect()

    #----------------------------------------------------------------
            
    class Death_zone(pygame.sprite.Sprite):
        """ Platform that results in instant death if collided with """

        def __init__(self, width, height):
            """ Platform constructor. Assumes constructed with user passing in
                an array of 5 numbers like what's defined at the top of this
                code. """

            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface([width, height])
            self.rect = self.image.get_rect()

    #----------------------------------------------------------------
            
    class Potion(pygame.sprite.Sprite):
        """ Platform that results in instant death if collided with """

        def __init__(self, width, height):
            """ Platform constructor. Assumes constructed with user passing in
                an array of 5 numbers like what's defined at the top of this
                code. """

            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface([width, height])
            self.rect = self.image.get_rect()
            
    #----------------------------------------------------------------
            
    class Enemy(pygame.sprite.Sprite):
        """ Platform the user can jump on """

        def __init__(self, width, height):
            """ Platform constructor. Assumes constructed with user passing in
                an array of 5 numbers like what's defined at the top of this
                code. """

            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface([width, height])
            self.rect = self.image.get_rect()
            self.change_x = 0
            self.change_y = 0
            self.is_attacked = 0
            self.is_attacking = 0
            self.is_dead = 0
            self.direction = 0
            self.still_image = None
            self.sprite_sheet = None
            self.animation = None
            self.move_timer = 0
            self.attack_timer = 0
            self.spawn_point = 0
            self.image_x = 0
            self.image_y = 0
            self.health = 100
            self.damage_taken = 0
            self.death_timer = 0
            self.death_animation_spawn = 0
            self.creep_type = None
            self.frame_rate = None
            self.atk_type = 1
            self.num = 0
            self.gravity = 0.75
            
    #############
    #Level Stuff#
    #############
            
    class Level(object):
        """ This is a generic super-class used to define a level.
            Create a child class for each level with level-specific
            info. """

        # Lists of sprites used in all levels. Add or remove
        # lists as needed for your game.
        platform_list = None
        enemy_list = None
        zone_list = None
        potion_list = None
        # Background image
        background = None

        world_shift = 0

        def __init__(self, player):
            """ Constructor. Pass in a handle to player. Needed for when moving platforms
                collide with the player. """
            self.platform_list = pygame.sprite.Group()
            self.enemy_list = pygame.sprite.Group()
            self.zone_list = pygame.sprite.Group()
            self.potion_list = pygame.sprite.Group()
            self.player = player

        # Update everythign on this level
        def update(self):
            """ Update everything in this level."""
            self.platform_list.update()
            self.enemy_list.update()
            self.zone_list.update()
            self.potion_list.update()
            
        def draw(self, screen,bk_x,Bk_y):
            """ Draw everything on this level. """        # Draw all the sprite lists that we have

            
            # Draw the background
            screen.blit(background, (0,0))
            screen.blit(PLATFORM, (bk_x,bk_y))

        def shift_world(self, shift_x, bk_x):
            """ When the user moves left/right and we need to scroll everything: """
     
            # Keep track of the shift amount
            self.world_shift += shift_x
            bk_x+= shift_x
            # Go through all the sprite lists and shift
            for platform in self.platform_list:
                platform.rect.x += shift_x
     
            for enemy in self.enemy_list:
                enemy.rect.x += shift_x

            for zone in self.zone_list:
                zone.rect.x += shift_x

            for potion in self.potion_list:
                potion.rect.x += shift_x
            return bk_x

#------------------------------------------------------------------------------------
        
    class Level_01(Level):
        """ Definition for level 1. """
        def __init__(self, player):
            """ Create level 1. """
            global spawn_point_counter
            # Call the parent constructor
            Level.__init__(self, player)

            self.level_limit = -2751
            self.boss_spawn = 2242
            # Array with width, height, x, and y of platform
            level =[[23, 82, 0, 470],
                    [26, 112, 24, 441],
                    [27, 86, 56, 468],
                    [17, 61, 75, 494],
                    [76, 20, 98, 530],
                    [77, 50, 175, 504],
                    [72, 74, 254, 473],
                    [111, 50, 332, 504],
                    [34, 18, 459, 533],
                    [21, 73, 490, 482],
                    [18, 95, 547, 459],
                    [18, 119, 601, 437],
                    [149, 164, 655, 386],
                    [37, 34, 713, 354],
                    [95, 95, 809, 462],
                    [148, 166, 907, 386],
                    [80, 86, 1056, 465],
                    [27, 54, 1272, 501],
                    [26, 26, 1442, 517],
                    [27, 51, 1466, 501],
                    [76, 32, 1590, 517],
                    [72, 59, 1672, 497],
                    [77, 84, 1748, 467],
                    [123, 54, 1837, 497],
                    [564, 16, 1960, 535],
                    [94, 58, 2511, 493],
                    [152, 114, 2600, 439],
                    [46, 37, 129, 349],
                    [46, 37, 220, 307],
                    [46, 37, 308, 272],
                    [111, 26, 440, 275],
                    [117, 20, 1128, 348],
                    [76, 22, 1318, 298],
                    [113, 23, 1477, 254],
                    [21, 125, 1771, 206]]
            enemy = [[30,40,274,432],
                     [30,40,376,463],
                     [30,40,861,421],
                     [30,40,1764,424],
                     [30,40,1893,454],
                     [30,40,2090,493],
                     [30,40,2200,493],
                     [30,40,2432,493],
                     [30,40,2549,451]]
            death_zone = [[31,14,513,535],
                          [30,15,567,536],
                          [30,14,620,535],
                          [123,15,1140,535],
                          [123,15,1307,535],
                          [79,15,1500,535],
                          [12,115,1748,213]]
            potion_list = [[12,13,489,252],
                           [12,13,1088,438],
                           [12,13,1472,477],
                           [12,13,1772,183],
                           [12,13,2672,418]]
            # Go through the array above and add platforms
            for platform in level:
                block = Platform(platform[0], platform[1])
                block.rect.x = platform[2]
                block.rect.y = platform[3]
                block.player = self.player
                self.platform_list.add(block)
            spawn_point_list_1 = [274,376,861,1764,1893,2090,2200,2432,2549]
            for enemies in enemy:
                creep = Enemy(enemies[0], enemies[1])
                creep.rect.x = enemies[2]
                creep.rect.y = enemies[3]
                creep.player = self.player
                creep.spawn_point = spawn_point_list_1[spawn_point_counter]
                spawn_point_counter+=1
                self.enemy_list.add(creep)
            for platform in death_zone:
                zones = Death_zone(platform[0], platform[1])
                zones.rect.x = platform[2]
                zones.rect.y = platform[3]
                zones.player = self.player
                zones.image.fill(RED)
                self.zone_list.add(zones)
            for pot in potion_list:
                potion = Potion(pot[0], pot[1])
                potion.rect.x = pot[2]
                potion.rect.y = pot[3]
                potion.player = self.player
                potion.image.fill(BLUE)
                self.potion_list.add(potion)
                
    #-----------------------------------------------------------------
                
    class Level_02(Level):
        """ Definition for level 2. """
     
        def __init__(self, player):
            """ Create level 2. """
            global spawn_point_counter
            # Call the parent constructor
            Level.__init__(self, player)
     
            self.level_limit = -2751
            self.boss_spawn = 2546
            # Array with type of platform, and x, y location of the platform.
            level = [[49,156,0,330],
                     [267,65,0,485],
                     [69,50,373,411],
                     [283,65,545,490],
                     [155,190,608,366],
                     [160,56,872,482],
                    #width,height,x,y
                     [147,50,977,255], #7th
                     [155,48,1025,410],
                     [150,48,1165,332],
                     [49,120,1270,230], # vertcal tall
                     [150,48,1210,188], # horozontal
                     [310,46,1367,510], #bottom left ground
                     [48,136,1630,420],
                     [287,54,1472,0],
                     [155,181,1538,0],
                     [46,130,1624,182], #vertical beam
                     [95,35,1624,264], #little dot
                     [55,168,1759,388], #right pillar
                     [550,50,1759,505],  #bottom right ground
                     [105,35,1772,230],  #little edge                 #
                     [55,35,1820,200],  #bump edge                    #
                     [155,188,1882,200], #big blub #2                 #
                     [86,180,1950,114], #big blub #1                  #
                     [305,62,1882,326], #2nd floor gound
                     [61,52,2244,463],   #
                     [61,49,2275,418],   # stairs
                     [61,49,2310,373],   #
                     [65,52,2251,242],     # middle block
                     [65,30,2115,208],
                     [65,52,2055,134],
                     [396,51,2356,308]]
            
            enemy = [[30,40,1219,289],
                     [30,40,1582,465],
                     [30,40,1943,461],
                     [30,40,2118,461],
                     [30,40,2277,374],
                     [30,40,2047,282],
                     [30,40,1899,153],
                     [30,40,2267,204],
                     [30,40,2569,264]]
                          
            death_zone = [[268,8,268,542],
                          [533,8,826,542],
                          [7,108,1676,429],
                          [10,134,1745,394],
                          [72,7,1678,542]]

            potion_list = [[12,13,395,389],
                           [12,13,1287,165],
                           [12,13,1776,363],
                           [12,13,1689,239],
                           [12,13,1984,94]]
     
            # Go through the array above and add platforms
            for platform in level:
                block = Platform(platform[0], platform[1])
                block.rect.x = platform[2]
                block.rect.y = platform[3]
                block.player = self.player
                self.platform_list.add(block)
            spawn_point_counter = 0
            spawn_point_list_2 = [1219,1582,1899,1943,2047,2118,2267,2277,2569]
            for enemies in enemy:
                creep = Enemy(enemies[0], enemies[1])
                creep.rect.x = enemies[2]
                creep.rect.y = enemies[3]
                creep.player = self.player
                creep.spawn_point = spawn_point_list_2[spawn_point_counter]
                spawn_point_counter+=1
                self.enemy_list.add(creep)
            for platform in death_zone:
                zones = Death_zone(platform[0], platform[1])
                zones.rect.x = platform[2]
                zones.rect.y = platform[3]
                zones.player = self.player
                zones.image.fill(RED)
                self.zone_list.add(zones)
            for pot in potion_list:
                potion = Potion(pot[0], pot[1])
                potion.rect.x = pot[2]
                potion.rect.y = pot[3]
                potion.player = self.player
                potion.image.fill(BLUE)
                self.potion_list.add(potion)
                
    #-----------------------------------------------------------------
                
    class Level_03(Level):
        """ Definition for level 3. """
        def __init__(self, player):
            global spawn_point_counter
            """ Create level 3. """
     
            # Call the parent constructor
            Level.__init__(self, player)
     
            self.level_limit = -2751
            self.boss_spawn = 2476
            # Array with type of platform, and x, y location of the platform.
            level = [[272,20,0,391],
                     [95,27,228,191],
                     [378,27,335,232], #second floor ground
                     [584,26,399,121],
                     [193,20,349,419],
                     [135,48,460,455], # getting up block
                     [135,48,616,354],
                     [135,48,783,276],
                     [51,430,933,121], #big wall
                     [251,150,933,402], # big blob #1
                     [768,35,933,517], # trap floor
                     [51,294,1088,0], #second floor wall
                     [609,74,1088,134],
                     [440,159,1094,135],
                     [124,161,1286,135],
                     [191,116,1511,435],
                     [113,197,1589,354],
                     [31,218,1671,333],
                     [91,20,1700,146],
                     [91,20,1701,333],
                     [91,20,1790,269],
                     [179,22,1880,203],  
                     [11,348,2048,203],
                     [706,18,2048,534],
                     [91,20,2173,423],
                     [91,20,2350,362],
                     [125,99,1284,298]]
            
            enemy = [[30,40,709,79],
                     [30,40,1130,360],
                     [30,40,1299,474],
                     [30,40,1443,474],
                     [30,40,1540,393],
                     [30,40,1638,312],
                     [30,40,1336,92],
                     [30,40,1579,92],
                     [30,40,2313,492],
                     [30,40,2463,492]]

            death_zone = [[12,145,1073,7],
                          [193,13,1087,298],
                          [111,14,1290,401],
                          [114,33,1412,300],
                          [158,15,1527,207],
                          [340,17,1703,530],
                          [391,49,1140,2],
                          [323,29,1699,1],
                          [36,319,2714,71]]

            potion_list = [[12,13,267,169],
                           [12,13,1016,376],
                           [12,13,1158,108],
                           [12,13,1830,245],
                           [12,13,2385,337]]
            # Go through the array above and add platforms
            for platform in level:
                block = Platform(platform[0], platform[1])
                block.rect.x = platform[2]
                block.rect.y = platform[3]
                block.player = self.player
                self.platform_list.add(block)
            spawn_point_counter=0
            spawn_point_list_3 = [709,1130,1299,1336,1443,1540,1579,1638,2313,2463]
            for enemies in enemy:
                creep = Enemy(enemies[0], enemies[1])
                creep.rect.x = enemies[2]
                creep.rect.y = enemies[3]
                creep.spawn_point = spawn_point_list_3[spawn_point_counter]
                spawn_point_counter+=1
                creep.player = self.player
                self.enemy_list.add(creep)
            for platform in death_zone:
                zones = Death_zone(platform[0], platform[1])
                zones.rect.x = platform[2]
                zones.rect.y = platform[3]
                zones.player = self.player
                zones.image.fill(RED)
                self.zone_list.add(zones)
            for pot in potion_list:
                potion = Potion(pot[0], pot[1])
                potion.rect.x = pot[2]
                potion.rect.y = pot[3]
                potion.player = self.player
                potion.image.fill(BLUE)
                self.potion_list.add(potion)
    #-----------------------------------------------------------------
    class Level_04(Level):
        """ Definition for level 4. """ 
        def __init__(self, player):
            global spawn_point_counter
            """ Create level 4. """
     
            # Call the parent constructor
            Level.__init__(self, player)
     
            self.level_limit = -2751
            self.boss_spawn = 2252
            # Array with type of platform, and x, y location of the platform.
            level = [[95,303,0,249],
                     [249,76,0,350],
                     [333,37,232,331], # bridge 1
                     [255,21,407,235], # higher bridge 1
                     [290,88,404,0],  # useless blob
                     [171,234,550,331], # after bridge 1 blob
                     [121,125,720,427], # after previous blob
                     [136,38,758,180], # stairs to high 1
                     [300,38,841,457], # lvl1 bridge 2
                     [48,46,1102,155],# brick to bridge 2
                     [53,53,985,244], # middle brick
                     [40,52,1120,375], #toe steper
                     [180,246,1152,305], # blob1
                     [130,37,1312,396], #
                     [37,155,1406,396], # trap area
                     [292,37,1511,395], #
                     [39,64,1511,395],  #
                     [380,88,1183,0], # useless blob 2
                     
                     [500,21,1110,168], #bridge 2
                     [123,341,1610,91], #blub2
                     [1053,43,1457,516], #bottom ground
                     [319,194,2432,368], # last block
                     [139,36,2036,286],
                     [141,33,1835,138],
                     [100,50,2402,464]]
            
            enemy = [[30,40,445,289],
                     [30,40,532,192],
                     [30,40,754,385],
                     [30,40,993,413],
                     [30,40,1290,127],
                     [30,40,1468,127],
                     [30,40,1751,354],
                     [30,40,1546,354],
                     [30,40,2012,470],
                     [30,40,2240,470],
                     [30,40,1228,263]]
            potion_list = [[12,13,551,309],
                           [12,13,1130,350],
                           [12,13,1119,132],
                           [12,13,1467,489],
                           [12,13,1664,69],
                           [12,13,2411,442]]
            # Go through the array above and add platforms
            for platform in level:
                block = Platform(platform[0], platform[1])
                block.rect.x = platform[2]
                block.rect.y = platform[3]
                block.player = self.player
                self.platform_list.add(block)
            spawn_point_counter=0
            spawn_point_list_4 = [445,532,754,993,1228,1290,1468,1546,1751,2012,2240]
            for enemies in enemy:
                creep = Enemy(enemies[0], enemies[1])
                creep.rect.x = enemies[2]
                creep.rect.y = enemies[3]
                creep.player = self.player
                creep.spawn_point = spawn_point_list_4[spawn_point_counter]
                spawn_point_counter+=1
                self.enemy_list.add(creep)
            for pot in potion_list:
                potion = Potion(pot[0], pot[1])
                potion.rect.x = pot[2]
                potion.rect.y = pot[3]
                potion.player = self.player
                potion.image.fill(BLUE)
                self.potion_list.add(potion)
    #-----------------------------------------------------------------
    class Level_05(Level):
        """ Definition for level 5. """ 
        def __init__(self, player):
            global spawn_point_counter
            """ Create level 5. """
     
            # Call the parent constructor
            Level.__init__(self, player)
     
            self.level_limit = -2751
            self.boss_spawn = 2317
            # Array with type of platform, and x, y location of the platform.
            level = [[1120,90,0,494],
                     [35,43,135,373], #
                     [35,43,234,373], #
                     [35,43,328,375], #
                     [35,43,426,375], #
                     [35,43,525,373], #
                     [35,43,623,373], #  second floor
                     [35,43,716,375], #
                     [35,43,815,375], #
                     [35,43,908,375], #
                     [35,43,1006,375],#
                     [35,42,1280,430],     #
                     [35,42,1475,372],     #
                     [35,42,1566,414],     #
                     [35,42,1815,491],     #
                     [35,42,1892,417],     # jump throught tunnel
                     [37,60,1954,317],     #
                     [64,172,1927,374],  #
                     [760,62,1991,482]]  # box
                     
            enemy = [[30,40,138,331],
                     [30,40,237,331],
                     [30,40,331,332],
                     [30,40,429,332],
                     [30,40,527,332],
                     [30,40,624,333],
                     [30,40,720,334],
                     [30,40,817,334],
                     [30,40,909,335],
                     [30,40,1009,335],
                     [30,40,1994,439],
                     [30,40,2621,439]]
            death_zone = [[800,11,1121,545]]

            potion_list = [[12,13,1486,349],
                           [12,13,1826,470]]
            # Go through the array above and add platforms
            for platform in level:
                block = Platform(platform[0], platform[1])
                block.rect.x = platform[2]
                block.rect.y = platform[3]
                block.player = self.player
                self.platform_list.add(block)
            spawn_point_counter=0
            spawn_point_list_5 = [138,237,331,429,527,624,720,817,909,1009,1994,2621]
            for enemies in enemy:
                creep = Enemy(enemies[0], enemies[1])
                creep.rect.x = enemies[2]
                creep.rect.y = enemies[3]
                creep.player = self.player
                creep.spawn_point = spawn_point_list_5[spawn_point_counter]
                spawn_point_counter+=1
                self.enemy_list.add(creep)
            for platform in death_zone:
                zones = Death_zone(platform[0], platform[1])
                zones.rect.x = platform[2]
                zones.rect.y = platform[3]
                zones.player = self.player
                zones.image.fill(RED)
                self.zone_list.add(zones)
            for pot in potion_list:
                potion = Potion(pot[0], pot[1])
                potion.rect.x = pot[2]
                potion.rect.y = pot[3]
                potion.player = self.player
                potion.image.fill(BLUE)
                self.potion_list.add(potion)

#########################
#       Functions       #
#########################

    ############
    #Animations#
    ############

    def blend_image(file_name):                 
        image_surface = pygame.image.load(file_name)
        image_surface = image_surface.convert() 
        colorkey = image_surface.get_at((0,0))  
        image_surface.set_colorkey(colorkey)    
        return image_surface

    #----------------------------------------------------------------------

    def redraw_game_window(bk_x):
        global boss_health_bar, current_level_no
        screen.fill(WHITE)
        current_level.draw(screen,bk_x,0)
        screen.blit(player_image, (player.image_x,player.image_y))   
        if explosion.visible:
            if is_running == 1:
                if direction == 0:
                    explosion.spawn(player.rect.x-47, player.rect.y-5)
                if direction == 1:
                    explosion.spawn(player.rect.x-10, player.rect.y-5)
            if is_attacking == 1:
                explosion.spawn(player.animation_x,player.animation_y)
            explosion.draw(screen)
            explosion.load_next()
            if explosion.index == 0:
                explosion.visible = False
        for creep in current_level.enemy_list:
            if creep.change_x!=0 or creep.is_attacking == 1 or creep.is_dead == 1:
                if creep.change_x!=0:
                    creep.animation.spawn(creep.image_x, creep.image_y)
                if creep.is_dead==1:
                    creep.animation.spawn(creep.image_x, creep.image_y)
                if creep.animation.visible:
                    creep.animation.draw(screen)
                    creep.animation.load_next() 
                if creep.animation.index == 0:
                    creep.animation.visible = False
            screen.blit(creep.still_image, (creep.image_x, creep.image_y))
            #draws small health bars above enemy minions
            health_bar = 0.3*creep.health
            boss_health_bar = 0.5666*creep.health
            if creep.creep_type==5:
                boss_health_bar = 1.13*creep.health
            if health_bar<0:
                health_bar=0
            if boss_is_spawn == 0:
                pygame.draw.rect(screen,RED,(creep.rect.x,creep.rect.y-20,30,5),0)
                if creep.health>0:
                    pygame.draw.rect(screen,GREEN,(creep.rect.x,creep.rect.y-20,health_bar,5),0)
            if boss_is_spawn == 1:
                pygame.draw.rect(screen,RED,(78,163,170,16),0)
                if creep.health>0:
                    pygame.draw.rect(screen,GREEN,(78,163,boss_health_bar,16),0)
                screen.blit(boss_health_bar_list[current_level_no], (0,125))
        #drawing health bars
        pygame.draw.rect(screen,RED,(90,43,300,14),0)
        pygame.draw.rect(screen,GREEN,(90,43,3*player.health,14),0)
        pygame.draw.rect(screen,RED,(90,60,300,7),0)
        pygame.draw.rect(screen,BLUE,(90,60,3*player.mana,7),0)
        #drawing the boarders and skill icons
        screen.blit(boarder, (0,0))
        screen.blit(icon_1, (95,70))
        screen.blit(icon_2, (140,70))
        screen.blit(icon_3, (185,70))
        screen.blit(icon_4, (230,70))
        screen.blit(icon_5, (275,70))
        #draw health pots in inventory
        if player.potion_no>6:
            player.potion_no=6
        for i in range(player.potion_no):
            screen.blit(potion_icon, (200+i*15,22))
        #draw potions on map
        for potion in current_level.potion_list:
            screen.blit(potion_icon, (potion.rect.x,potion.rect.y))
        #draw intro scenes
        if 0<=intro_counter<=1 and current_level_no==0:
            screen.blit(intro_list[intro_counter],(0,0))
        #update the screen
        pygame.display.update()

    #-----------------------------------------------------------------------------------
        
    background_welcome = pygame.image.load("Title_Page.png")#title page picture
    def redraw_welcome_window():
        screen.blit(background_welcome, (0,0)) #this will be the background photo

    #-----------------------------------------------------------------------------------
        
#############################
#       Main Program        #
#############################

    animation_time=0
    pygame.init()

    #Background dimensions, must be the same
    # Set the height and width of the screen

    pygame.display.set_caption("DHWD Games")

    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))
    level_list.append(Level_03(player))
    level_list.append(Level_04(player))
    level_list.append(Level_05(player))

    # Set the current level
    if reset == True:
        current_level_no = 0
    elif reset == False:
        current_level_no = current_level_no
    current_level = level_list[current_level_no]
        
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player_x_spawn_list=[340,12,55,30,25]
    player_y_spawn_list=[225,280,340,200,450]
    player.rect.x = player_x_spawn_list[current_level_no]
    player.rect.y = player_y_spawn_list[current_level_no]
    active_sprite_list.add(player)
    #Loop until the user clicks the close button.
    done = False
    #Some ofthe variables needed to do things
    bk_x=0
    bk_y=0
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    #attacking hitbox
    atk_list=[[0,0],[40,20],[40,20],[165,40],[40,20],[150,50],[50,100]]
    atk_list2=[[0,0],[40,20],[40,20],[165,40],[40,20],[150,50],[50,100]]
    atk = attack(atk_list[atk_type][0], atk_list[atk_type][1])
    atk.rect.x = player.rect.x
    atk.rect.y = player.rect.y
    atk_x_list = [0,player.rect.x-110,player.rect.x-110,player.rect.x-110,player.rect.x-110,player.rect.x-110]
    atk_y_list = [0,player.rect.y+10,player.rect.y+10,player.rect.y+10,player.rect.y+10,player.rect.y+10]
    attack_list = pygame.sprite.Group()
    attack_hit_list = pygame.sprite.spritecollide(atk, current_level.enemy_list, False)

    #spawn location for boss
    boss_spawn_y = 250
    #idle animation timer
    idle_timer = 0
    #move_timer
    move_timer = 0
    #animation delay timer
    animation_delay = 0
    #-----------------------

    ###################
    #Main Program Loop#
    ###################
    
    explosion = AnimatedSprite("player/akame/left/autoatk2(8).png",8)
    pause = True#game isn't paused
    check = True    #game can only start if check = True
    finished = False  #game starts when this is True
    while not done:
        while finished == False:
            if reset == True:

                ################
                #Welcome Screen#
                ################
                
                redraw_welcome_window()

                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE and check == True:
                            finished = True #start the game
                        elif(event.key == K_RIGHT):#if right key is pressed,
                            check = False   #can't exit into game from this screen
                            background_welcome = pygame.image.load("Controls.png") #instructions screen
                        elif(event.key == K_LEFT): #if left key is pressed,
                            check = True    #welcome screen can be exited from into the game
                            background_welcome = pygame.image.load("Title_Page.png") #show welcome page
                    elif event.type == pygame.QUIT: # If user clicked close
                        finished = True               #quit the welcome screen loop
                        done = True                 #exit the game
                        game_loop = False
                pygame.display.flip()

#############################################################################################

            else:
                finished = True #don't show the title screen if player is just restarting from within current level 
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
                game_loop = False
            if is_dead == 0 and is_attacked == 0:
                if event.type == pygame.KEYDOWN:

            ####################
            #Character Controls#
            ####################
                    
                    if event.key == pygame.K_a:#if "a" key is pressed, do designated attack
                        if is_attacking == 0 and player.mana>=50:
                            atk_type = 1
                            if direction == 0:
                                explosion.visible = False
                                explosion = AnimatedSprite("player/akame/left/superatk1(26).png",26)
                            if direction == 1:
                                explosion.visible = False
                                explosion = AnimatedSprite("player/akame/right/superatk1(26)right.png",26)
                            explosion.spawn(player.animation_x ,player.animation_y)
                            is_attacking = 1
                            atk = attack(atk_list[atk_type][0],atk_list[atk_type][1])
                            attack_list.add(atk)
                            player.mana-=50

                    if event.key == pygame.K_s:#if "s" key is pressed, do designated attack
                        if is_attacking == 0 and player.mana>=30:
                            atk_type = 3
                            if direction == 0:
                                explosion.visible = False
                                explosion = AnimatedSprite("player/akame/left/atk1(9).png",9)
                            if direction == 1:
                                explosion.visible = False
                                explosion = AnimatedSprite("player/akame/right/atk1(9)right.png",9)
                            explosion.spawn(player.animation_x ,player.animation_y)
                            is_attacking = 1
                            atk = attack(atk_list[atk_type][0],atk_list[atk_type][1])
                            attack_list.add(atk)
                            player.mana-=30
                            
                    if event.key == pygame.K_z:#if "z" key is pressed, do designated attack
                        if is_attacking == 0 and player.mana>=10:
                            atk_type = 4
                            if direction == 0:
                                explosion.visible = False
                                explosion = AnimatedSprite("player/akame/left/autoatk2(8).png",8)
                            if direction == 1:
                                explosion.visible = False
                                explosion = AnimatedSprite("player/akame/right/autoatk2(8)right.png",8)
                            explosion.spawn(player.animation_x ,player.animation_y)
                            is_attacking = 1
                            atk = attack(atk_list[atk_type][0],atk_list[atk_type][1])
                            attack_list.add(atk)
                            player.mana-=10
                            
                    if event.key == pygame.K_x:#if "x" key is pressed, do designated attack
                        if is_attacking == 0 and player.mana>=5:
                            atk_type = 5
                            if direction == 0:
                                explosion.visible = False
                                explosion = AnimatedSprite("player/akame/left/autoatk1(6).png",6)
                            if direction == 1:
                                explosion.visible = False
                                explosion = AnimatedSprite("player/akame/right/autoatk1(6)right.png",6)
                            explosion.spawn(player.animation_x ,player.animation_y)
                            is_attacking = 1
                            atk = attack(atk_list[atk_type][0],atk_list[atk_type][1])
                            attack_list.add(atk)
                            player.mana-=5
                                
                    if event.key == pygame.K_d:#if "c" key is pressed, use potion if in character's possesion
                        if is_attacking == 0 and player.mana>=30:
                            atk_type = 6
                            if direction == 0:
                                explosion.visible = False
                                explosion = AnimatedSprite("player/akame/left/atk2(10).png",10)
                            if direction == 1:
                                explosion.visible = False
                                explosion = AnimatedSprite("player/akame/right/atk2(10)right.png",10)
                            explosion.spawn(player.animation_x,player.animation_y)
                            is_attacking = 1
                            atk = attack(atk_list[atk_type][0],atk_list[atk_type][1])
                            attack_list.add(atk)
                            player.mana-=30

                    if event.key == pygame.K_LEFT:#if left key is pressed, move left
                        player.go_left()
                        if is_attacking == 0:
                            direction = 0
                        if is_attacking == 1:
                            if direction == 0:
                                direction = 0
                            if direction == 1:
                                direction = 1

                        
                    if event.key == pygame.K_RIGHT:#if right key is pressed, move right

                        player.go_right()
                        if is_attacking == 0:
                            direction = 1
                        if is_attacking == 1:
                            if direction == 0:
                                direction = 0
                            if direction == 1:
                                direction = 1


                    if event.key == pygame.K_UP:
                        player.jump()
                    if intro_counter<=1:
                        if event.key == pygame.K_SPACE:
                            intro_counter +=1

        #################
        #Check for pause#
        #################
                    if event.key == pygame.K_p: #if p is pressed
                        pause = False           #pauses the game

                    #chug potions
                    if event.key == pygame.K_c:
                        if player.potion_no>0:
                            player.potion_no-=1
                            player.health+=30
                    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and player.change_x < 0:
                        player.stop()
                        is_running = 0
                    if event.key == pygame.K_RIGHT and player.change_x > 0:
                        player.stop()

        #####################
        #Code for Cut Scenes#
        #####################
                        
        cut_scene = False
        end_of_game = False
        index = 0
        cut_scene_list = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png"]#list of first cut-scene photos
        end_of_game_list = ["1A.png", "2A.png", "3A.png", "4A.png", "5A.png", "6A.png", "7A.png", "8A.png", "9A.png", "10A.png", "11A.png", "Credits.jpg"]#end of game cutscene photos

        if current_level_no == 4 and boss_is_spawn == 1 and cut_check == False:#if "boss" in last level spawns,
            cut_scene = True
            
        while cut_scene == True:
            cut_check = True
            cut_scene_background = pygame.image.load(cut_scene_list[index])#show the first cutscene
            screen.blit(cut_scene_background, (0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:#go through the list of different cutscenes
                        index += 1
            if index >= 6:
                cut_scene = False

        if current_level_no == 4 and boss_is_dead == 1:#when the boss dies
            counter += 1
            index = 0
            end_of_game = True

        while end_of_game == True and counter >= 50:#counter to delay to acount for death animation of boss
            end_of_game_background = pygame.image.load(end_of_game_list[index])#draw first end of game cutscene
            screen.blit(end_of_game_background, (0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:#switch through the list of them
                        index += 1
            if index >= 12:#when the last scene is done,
                end_of_game = False#cutscenes are done
                done = True#exit out of program loop
                reset = True#go back to title menu

        #################################################################


    ############
    #Pause Loop#
    ############
                    
        pause_screen = pygame.image.load("Pause_Screen.png")    #display pause screen
        check = True #check to exit pause menu (permission)             
        while pause == False:   #while game is paused
            screen.blit(pause_screen,(0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pause = True                                #leave pause loop
                    done = True                                 #exit game loop
                    game_loop = False                           #don't reset the game
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p and check == True:             #if "p" is pressed while paused and permission to exit is true
                       pause = True                         #unpause game
                    elif event.key == pygame.K_RIGHT:
                        check = False   #can't exit from control menu
                        pause_screen = pygame.image.load("Controls_Pause.png")    #show controls page
                    elif event.key == pygame.K_LEFT:
                        check = True    #can now exit again from pause screen
                        pause_screen = pygame.image.load("Pause_Screen.png")    #display pause screen
                    elif event.key == K_ESCAPE: #if escape key is hit,
                        done = True             #restart the game
                        pause = True            #get out of pause loop
                        reset = True            #reset from level 1
                        game_loop = True        #but restart the game, don't exit out of it
                    elif event.key == K_RETURN: #restart the game from within current level
                        done = True
                        pause = True
                        reset = False
                            
        #############################################################

        
        #Generate player's mana at 5 per second
        if player.mana<100:
            player.mana+=0.45
        #limit the player's health to 100
        if player.health>100:
            player.health=100
        #change colours of skill icons when not enough mana
        if player.mana<10:
            icon_1 = skill_z_icon_NA
        if player.mana<5:
            icon_2 = skill_x_icon_NA
        if player.mana<50:
            icon_3 = skill_a_icon_NA
        if player.mana<30:
            icon_4 = skill_s_icon_NA
        if player.mana<30:
            icon_5 = skill_d_icon_NA
        if player.mana>=10:
            icon_1 = skill_z_icon
        if player.mana>=5:
            icon_2 = skill_x_icon
        if player.mana>=50:
            icon_3 = skill_a_icon
        if player.mana>=30:
            icon_4 = skill_s_icon
        if player.mana>=30:
            icon_5 = skill_d_icon
        #limit potion numbers to 6
        if player.potion_no>6:
            player.potion_no=6
        #idle animation state
        if player.change_x ==0 and is_jumping==0 and is_attacking == 0 and is_dead == 0 and is_attacked == 0:
            is_idle = 1
            player_image=pygame.image.load("player/blank.png")
            if idle_timer == 0:
                if direction == 0:
                    explosion.visible = False
                    explosion = AnimatedSprite("player/akame/left/idle(12).png",12)
                    explosion.spawn(player.rect.x-45 ,player.rect.y-10)
                if direction == 1:
                    explosion.visible = False
                    explosion = AnimatedSprite("player/akame/right/idle(12)right.png",12)
                    explosion.spawn(player.rect.x-17 ,player.rect.y-10)
            idle_timer+=1
            if idle_timer >12:
                idle_timer = 0
                if direction == 0:
                    explosion.visible = False
                    explosion = AnimatedSprite("player/akame/left/idle(12).png",12)
                    explosion.spawn(player.rect.x-45 ,player.rect.y-10)
                if direction == 1:
                    explosion.visible = False
                    explosion = AnimatedSprite("player/akame/right/idle(12)right.png",12)
                    explosion.spawn(player.rect.x-17 ,player.rect.y-10)
        if player.change_x !=0 or is_jumping !=0 or is_attacking != 0:
            idle_timer=0
            is_idle = 0
        #This indicates if there were a change in direction
        if direction == 0:
            if previous_direction == 0:
                direction_change = False
            if  previous_direction == 1:
                direction_change = True
                previous_direction = 0
        if direction == 1:
            if  previous_direction == 1:
                direction_change = False
            if  previous_direction == 0:
                direction_change = True
                previous_direction = 1
        #Running animation state
        if is_attacking == 0 and is_jumping == 0 and is_idle==0 and is_dead == 0 and is_attacked == 0:
            is_running = 1
            player_image=pygame.image.load("player/blank.png")
            if move_timer == 0:
                if direction == 0:
                    explosion.visible = False
                    explosion = AnimatedSprite("player/akame/left/run(10).png",10)
                    explosion.spawn(player.rect.x-47 ,player.rect.y-5)
                if direction == 1:
                    explosion.visible = False
                    explosion = AnimatedSprite("player/akame/right/run(10)right.png",10)
                    explosion.spawn(player.rect.x-10 ,player.rect.y-5)
            move_timer+=1
            if move_timer>0 and move_timer<=10 and direction_change:
                if direction == 0:
                    explosion.visible = False
                    explosion = AnimatedSprite("player/akame/left/run(10).png",10)
                    explosion.spawn(player.rect.x-47 ,player.rect.y-5)
                if direction == 1:
                    explosion.visible = False
                    explosion = AnimatedSprite("player/akame/right/run(10)right.png",10)
                    explosion.spawn(player.rect.x-10 ,player.rect.y-5)
                move_timer =0
            if move_timer >10:
                move_timer =0
                if direction == 0:
                    explosion.visible = False
                    explosion = AnimatedSprite("player/akame/left/run(10).png",10)
                    explosion.spawn(player.rect.x-47 ,player.rect.y-5)
                if direction == 1:
                    explosion.visible = False
                    explosion = AnimatedSprite("player/akame/right/run(10)right.png",10)
                    explosion.spawn(player.rect.x-10 ,player.rect.y-5)
        if is_attacking!=0 or is_jumping!=0 or player.change_x ==0:
            move_timer = 0
            is_running = 0
        #jumping and running animation bug handling
        if is_jumping == 1 and is_attacking == 0:
            explosion.visible = False
            explosion = AnimatedSprite("player/blank.png",10)
            explosion.spawn(player.rect.x ,player.rect.y)
        #check to see if there are anything above the player, so the jumping image won't change
        #when the player's head bumps onto something
        player.rect.y -= 1
        platform_hit_list = pygame.sprite.spritecollide(player, player.level.platform_list, False)
        player.rect.y += 1
        #check if in air
        if player.change_y == 0 and len(platform_hit_list)==0:
            is_jumping = 0
        if player.change_y != 0:
            is_jumping = 1
        if is_jumping == 1:
            if direction == 0:
                player_image=pygame.image.load("player/akame/left/jump(left).png")
            if direction == 1:
                player_image=pygame.image.load("player/akame/right/jump(right).png")
        #handles attacking animation timing
        if is_attacking == 1:
            animation_time+=1
            player_image=pygame.image.load("player/blank.png")
            attack_hit_list = pygame.sprite.spritecollide(atk, current_level.enemy_list, False)
            for hits in attack_hit_list:
                hits.image.fill(WHITE)
                hits.is_attacked = 1
                if hits.damage_taken ==0:  #attack damage
                    if atk_type == 1:
                        hits.health-=101
                    if atk_type == 3:
                        hits.health-=40
                    if atk_type == 4:
                        hits.health-=21
                    if atk_type == 5:
                        hits.health-=11
                    if atk_type == 6:
                        hits.health-=30
                    hits.damage_taken =1
        if animation_time == atk_frame_list[atk_type]:
            animation_time = 0
            is_attacking = 0
            atk_type = 0
            attack_list.empty()
            for hits in current_level.enemy_list:#This code must be changed later with the enemy_is_hit state, to make sure only when collide, will they take damage
                hits.is_attacked = 0
                hits.damage_taken = 0
                hits.image.fill(BLACK)
            for hits in attack_hit_list:
                attack_hit_list.remove(hits)
        #sometime the player may get stuck and not able to move, this timer fixes it
        if is_attacked == 0:
            stun_counter = 0
        if is_attacked == 1:
            explosion.visible = False
            stun_counter+=1
            if direction == 0:
                player_image=pygame.image.load("player/akame/left/gothit.png")
                
            if direction == 1:
                player_image=pygame.image.load("player/akame/right/gothit_right.png")
        if stun_counter >3:
            is_attacked == 0
        #checking if any minions are dead
        for creep in current_level.enemy_list:
            if creep.health<0:
                creep.is_dead =1
                creep.death_timer+=1
                if creep.death_timer ==30:
                    current_level.enemy_list.remove(creep)

        # Update the player.
        active_sprite_list.update()
        attack_list.update()
        # Update items in the level
        current_level.update()
        #checking if the player is dead, if yes, deny all events
        if player.health<=0:
            is_dead =1
            done = True     #exit out of game loop
            game_over = True #don't restart
            death_animation_count = 0#show character death animation count
            if direction ==0:
                player_image=pygame.image.load("player/akame/left/death.png")
                player.image_y = player.rect.y-20
                player.image_x = player.rect.x-10
            if direction == 1:
                player_image=pygame.image.load("player/akame/right/death_right.png")
                player.image_y = player.rect.y-20
                player.image_x = player.rect.x-25

            while game_over == True:
                
                while death_animation_count < 60:
                    death_animation_count += 1
                    redraw_game_window(bk_x)
                   
                game_over_screen = pygame.image.load("Game_Over_Screen.png")
                screen.blit(game_over_screen, (0,0))
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            game_loop = True #restart the game
                            reset = True    #reset to level 1
                            game_over = False #exit game-over screen
                        elif event.key == K_RETURN:
                            game_loop = True    #restart the game
                            reset = False   #reset game at current level
                            game_over = False #exit game-over screen

                    elif event.type == pygame.QUIT:
                        game_loop = False #exit out of the game
                        game_over = False #exit out of the game-over screen

        # Update the positions of the attack hit box
        if direction == 0:
            if atk_type==1:
                atk.rect.x = player.rect.x-110
                atk.rect.y = player.rect.y+10
            if atk_type==2:
                atk.rect.x = player.rect.x-100
                atk.rect.y = player.rect.y-10
            if atk_type==3:
                atk.rect.x = player.rect.x-100
                atk.rect.y = player.rect.y-10
            if atk_type==4:
                atk.rect.x = player.rect.x-110
                atk.rect.y = player.rect.y+10
            if atk_type==5:
                atk.rect.x = player.rect.x-120
                atk.rect.y = player.rect.y-10
            if atk_type==6:
                atk.rect.x = player.rect.x-110
                atk.rect.y = player.rect.y-60
        if direction == 1:
            if atk_type==1:
                atk.rect.x = player.rect.x+100
                atk.rect.y = player.rect.y+10
            if atk_type==2:
                atk.rect.x = player.rect.x+100
                atk.rect.y = player.rect.y-10
            if atk_type==3:
                atk.rect.x = player.rect.x-30
                atk.rect.y = player.rect.y-10
            if atk_type==4:
                atk.rect.x = player.rect.x+100
                atk.rect.y = player.rect.y+10
            if atk_type==5:
                atk.rect.x = player.rect.x+20
                atk.rect.y = player.rect.y-10
            if atk_type==6:
                atk.rect.x = player.rect.x+90
                atk.rect.y = player.rect.y-60

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.left < 0:
            player.rect.left = 0
        # If the player gets near the right side, shift the world left (-x)
        if bk_x>-1851:
            if player.rect.right >= 500:
                diff = player.rect.right - 500
                player.rect.right = 500
                bk_x = current_level.shift_world(-diff, bk_x)            
                for creep in current_level.enemy_list:
                    creep.spawn_point-=diff
                current_level.boss_spawn-=diff
                    
        # If the player gets near the left side, shift the world right (+x)
        if bk_x<0:
            if player.rect.left <= 350:
                diff = 350 - player.rect.left
                player.rect.left = 350
                bk_x = current_level.shift_world(diff, bk_x)
                for creep in current_level.enemy_list:
                    creep.spawn_point+=diff
                current_level.boss_spawn+=diff

        #if the boss is not killed, the player cant go to next level
        if boss_is_dead == 0:
            if player.rect.x>875:
                player.rect.x = 875
        # If the player gets to the end of the level, go to the next level
        if boss_is_dead == 1:
            if current_level.world_shift<-1850:
                if player.rect.x>875:
                    creep_is_spawn = 0
                    spawn_point_counter = 0
                    boss_is_dead = 0
                    boss_is_spawn = 0
                    if current_level_no < len(level_list)-1:
                        current_level_no += 1
                        current_level = level_list[current_level_no]
                        player.level = current_level
                        bk_x=0
                    player.rect.x = player_x_spawn_list[current_level_no]#change player spawn points for each level here
                    player.rect.y = player_y_spawn_list[current_level_no]
           #changes for the new level
        background = background_image_list[current_level_no]
        PLATFORM = platform_image_list [current_level_no]
        #random generator for creep type
        if creep_is_spawn == 0:
            creep_is_spawn = 1
            for creep in current_level.enemy_list:
                creep.creep_type = random.randint(1,4)

                
        #adds boss when needed
        if boss_is_spawn == 0 and len(current_level.enemy_list) == 0:
            boss_is_spawn =1
            boss = Enemy(30, 40)
            boss.creep_type = current_level_no+5
            boss.rect.x = current_level.boss_spawn
            boss.rect.y = boss_spawn_y
            if boss.creep_type == 5:  #boss health
                boss.health=150
            if boss.creep_type == 6:  
                boss.health=300
            if boss.creep_type == 7:
                boss = Enemy(30, 70)
                boss.rect.x = current_level.boss_spawn
                boss.rect.y = boss_spawn_y-30
                boss.health=300
            if boss.creep_type == 8:  
                boss.health=300
            if boss.creep_type == 9:  
                boss.health=300
            current_level.enemy_list.add(boss)
        boss_type=current_level_no+5
        #Artificial intellegence
        for creep in current_level.enemy_list:
            if boss_is_spawn == 0:
                ai_list = AI.ai(player.rect.x, player.rect.y,creep.rect.x, creep.rect.y, creep.spawn_point, creep.is_attacked, creep.is_dead, ai_dont_attack)
            if boss_is_spawn == 1:
                ai_list = AI.ai(player.rect.x, player.rect.y,creep.rect.x, creep.rect.y, current_level.boss_spawn, creep.is_attacked, creep.is_dead, ai_dont_attack)
            creep.change_y = 2.9
            creep.is_attacking = ai_list[4]
            if creep.change_x>0:
                creep.direction = 1
            if creep.change_x<0:
                creep.direction = 0
            #checks if on the ground
            if creep.rect.y >= ground-40 and creep.change_y >= 0:
                creep.change_y = 0
                creep.rect.y = ground-40
            
            #checks if the creep bumps into any other platforms
            block_hit_list = pygame.sprite.spritecollide(creep, player.level.platform_list, False)
            for block in block_hit_list:
                if creep.change_x > 0:
                    creep.rect.right = block.rect.left
                if creep.change_x < 0:
                    creep.rect.left = block.rect.right

            #checks if we are on a platform
            creep.rect.y += 2
            platform_hit_list = pygame.sprite.spritecollide(creep, player.level.platform_list, False)#                     Here IS THE PROBLEM!!
            creep.rect.y -= 2

            if len(platform_hit_list) > 0 :
                creep.change_y = 0
            if len(platform_hit_list) > 0 and creep.change_y==0 and creep.rect.y > ground-40:
                creep.change_y = 2.9
            #move the creeps left and right
            creep.change_x=ai_list[5]
            creep.rect.x+=ai_list[5]
            creep.rect.y+=creep.change_y
            #gives the boss his creep type number when boss is spawned
            if random_atk_generated == 0:
                creep.atk_type = random.randint(1,2)
                if creep.creep_type == 9:
                    creep.atk_type = random.randint(1,4)
                random_atk_generated = 1
            #gives each enemy their current image, based on their state
            if boss_is_spawn == 0:
                sprite_list = enemy_animation.enemy_animation(creep.direction, creep.creep_type, creep.change_x, creep.rect.x, creep.rect.y, creep.is_attacking, creep.is_attacked, creep.is_dead, 0, 1)
            if boss_is_spawn == 1:          
                sprite_list = enemy_animation.enemy_animation(creep.direction, boss_type, creep.change_x, creep.rect.x, creep.rect.y, creep.is_attacking, creep.is_attacked, creep.is_dead, 0, creep.atk_type)
            creep.sprite_sheet = sprite_list[0]
            creep.still_image = sprite_list[1]
            creep.image_x = sprite_list[2]
            creep.image_y = sprite_list[3]
            if creep.change_x!=0 and creep.is_attacking == 0:
                if creep.move_timer == 0:
                    creep.animation=AnimatedSprite(creep.sprite_sheet, sprite_list[4])
                    creep.animation.spawn(creep.image_x, creep.image_y)
                creep.move_timer+=1
                if creep.move_timer >4:
                    creep.animation.visible = False
                    creep.animation=AnimatedSprite(creep.sprite_sheet, sprite_list[4])
                    creep.animation.spawn(creep.image_x, creep.image_y)
                    creep.move_timer = 0
            if creep.is_attacking == 1:
                if creep.attack_timer == 0:
                    creep.animation=AnimatedSprite(creep.sprite_sheet, sprite_list[4])
                if creep.attack_timer == 1 :
                    creep.animation.spawn(creep.image_x, creep.image_y)
                if creep.attack_timer ==5: #minion attack damage
                    if boss_is_spawn == 0:
                        player.health-=10
                    if boss_is_spawn == 1 and creep.creep_type !=9:
                        player.health-=20
                    if boss_is_spawn == 1 and creep.creep_type ==9:
                        player.health-=30
                    is_attacked = 1
                    player.change_x = 0
                if creep.attack_timer ==8:
                    is_attacked = 0
                creep.attack_timer+=1
                if creep.attack_timer>sprite_list[4]:
                    creep.animation.visible = False
                    creep.animation=AnimatedSprite(creep.sprite_sheet, sprite_list[4])
                    creep.animation.spawn(creep.image_x, creep.image_y)
                    creep.attack_timer = 0
                    random_atk_generated = 0
            if creep.change_x == 0 and creep.is_attacking == 0 or creep.change_x !=0 and creep.is_attacking ==0:
                creep.attack_timer = 0
            if boss_is_spawn ==1:
                if creep.health<0:
                    boss_is_dead = 1
            if creep.health<0:
                creep.is_dead =1
                creep.death_timer+=1
                if creep.death_animation_spawn == 0:
                    creep.death_animation_spawn = 1
                    creep.animation=AnimatedSprite(creep.sprite_sheet, sprite_list[4])
                if boss_is_spawn == 0:
                    if creep.death_timer ==50:
                        current_level.enemy_list.remove(creep)
                if creep.death_timer ==100:
                    current_level.enemy_list.remove(creep)
            
        # Limit to 60 frames per second
        clock.tick(30)

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
        redraw_game_window(bk_x)

    pygame.quit()
