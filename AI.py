##import pygame, sys, time
##from pygame.locals import *
##pygame.init()
##
###colours
##BLACK    = (   0,   0,   0)
##WHITE    = ( 255, 255, 255)
##BLUE     = (   0,   0, 255)
##RED      = ( 255,   0,   0)
##GREEN    = (   0, 255,   0)
##
##SCREEN_WIDTH = 900
##SCREEN_HEIGHT = 550
##size = [SCREEN_WIDTH, SCREEN_HEIGHT]
##game_window = pygame.display.set_mode(size)
##
###Ball 1 features
##radius = 50
##outline = 0
##ballx = 50
##bally = 500
##ballcolour = RED
##
###ball 2 features
##speed = 0
##ballx2 = 800
##bally2 = 500
##ball2colour = GREEN
##
##attack = "no"

###########################################
#Functions#
###########################################

def ai(x,y,x2,y2,spawn_point, is_attacked, is_dead, ai_dont_attack):
    is_attacking = 0
    change_x = 0
    lst = [x,y,x2,y2,is_attacking,change_x]


####################################################
    #check for proximity for attack
####################################################
    if is_attacked == 0 and is_dead ==0:
        
        if abs(x2 - x) > 150:
                if (x2-spawn_point)>0:
                    lst[5] = -2
                if (x2 - spawn_point)<0:
                    lst[5] = 2
                if abs(x2 - spawn_point)==15:
                    lst[5] = 0
        if abs(lst[3]-lst[1])<=150:
            if (x2 - x) <= 250 and (x2 - x) > 25:                     #if they are within a certain distance (x-wise),
                lst[5] = -2
                        
                        
            if (x2 - x) >= -250 and (x2 - x) < -25:                 #same as above except for character being on the left of our character
                lst[5] = 2
        if ai_dont_attack==0:
            if abs(lst[2]-lst[0])<=35 and abs(lst[3]-lst[1])<=50:
                lst[5] = 0
                lst[4] = 1           
            if abs(x2 - x) > 550:
                if (x2-spawn_point)>0:
                    lst[5] = -6
                if (x2 - spawn_point)<0:
                    lst[5] = 6
                if abs(x2 - spawn_point)==30:
                    lst[5] = 0

    ####################################################
        #Following algorithem
    ####################################################


                
    ####################################################
        #"shuffling" movement when our character is far away
    ####################################################
            



    
    
    return lst

##def redraw_game_window():
##    game_window.fill(WHITE)
##    pygame.draw.circle(game_window, ballcolour, (ballx, bally), radius, outline)
##    pygame.draw.circle(game_window, ball2colour, (ballx2, bally2), radius, outline)
##    pygame.display.update()
##
###############################################
###Main Program#
###############################################
##
##
##exit_flag = False
##while exit_flag == False:
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            sys.exit()
##    if event.type == KEYDOWN:
##        if(event.key == K_RIGHT):
##            ballx += 10                                         #if right key is pressed, move "character" right
##        if(event.key == K_LEFT):
##            ballx -= 10                                         #if left key is pressed, move "character" left
##        if(event.key == K_SPACE):
##            bally -= 80
##            redraw_game_window()
##            pygame.time.delay(100)
##    ai_info = ai(ballx,bally,ballx2,bally2,ball2colour, speed)              #run ai function
##    
###elements of the list broken back up again into original variables
##    ballx = ai_info[0]
##    bally = ai_info[1]
##    ballx2 = ai_info[2]
##    bally2 = ai_info[3]
##    attack = ai_info[4]
##    speed = ai_info[5]
##    ballx2 = ballx2 + speed
##    print(attack)
##    redraw_game_window()
##    pygame.time.delay(20)
##pygame.quit()
