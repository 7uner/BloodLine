import pygame
blank = pygame.image.load("player/blank.png")
blank_animation = "player/blank.png"
#for different types of creeps
creep_1_walk_left="player/creeps/armor/left/walk(4).png"
creep_2_walk_left="player/creeps/goblin/left/walk(4).png"
creep_3_walk_left="player/creeps/lizard/left/walk(4).png"
creep_4_walk_left="player/creeps/spear/left/walk(4).png"
creep_5_walk_left="player/creeps/sword/left/walk(4).png"
creep_6_walk_left="player/bosses/desertsoldier/left/run.png"
creep_7_walk_left="player/bosses/ripper/left/run.png"
creep_8_walk_left="player/bosses/crab/left/walk(6).png"
creep_9_walk_left="player/bosses/gladiator/left/run.png"
creep_10_walk_left="player/bosses/alex/left/run(3).png"

creep_1_walk_right="player/creeps/armor/right/walk(4)right.png"
creep_2_walk_right="player/creeps/goblin/right/walk(4)right.png"
creep_3_walk_right="player/creeps/lizard/right/walk(4)right.png"
creep_4_walk_right="player/creeps/spear/right/walk(4)right.png"
creep_5_walk_right="player/creeps/sword/right/walk(4)right.png"
creep_6_walk_right="player/bosses/desertsoldier/right/run_right.png"
creep_7_walk_right="player/bosses/ripper/right/run_right.png"
creep_8_walk_right="player/bosses/crab/right/walk(6)right.png"
creep_9_walk_right="player/bosses/gladiator/right/run_right.png"
creep_10_walk_right="player/bosses/alex/right/run(3)right.png"

creep_1_attack_left="player/creeps/armor/left/atk(12).png"
creep_2_attack_left="player/creeps/goblin/left/atk(12).png"
creep_3_attack_left="player/creeps/lizard/left/atk(7).png"
creep_4_attack_left="player/creeps/spear/left/atk(12).png"
creep_5_attack_left="player/creeps/sword/left/atk(12).png"
creep_6_attack_left_1="player/bosses/desertsoldier/left/atk1(12).png"
creep_6_attack_left_2="player/bosses/desertsoldier/left/atk2(12).png"
creep_7_attack_left_1="player/bosses/ripper/left/atk1(14).png"
creep_7_attack_left_2="player/bosses/ripper/left/atk2(16).png"
creep_8_attack_left_1="player/bosses/crab/left/atk1(8).png"
creep_8_attack_left_2="player/bosses/crab/left/atk2(10).png"
creep_9_attack_left_1="player/bosses/gladiator/left/atk1(10).png"
creep_9_attack_left_2="player/bosses/gladiator/left/atk2(8).png"
creep_10_attack_left_1="player/bosses/alex/left/atk1(15).png"
creep_10_attack_left_2="player/bosses/alex/left/atk2(14).png"
creep_10_attack_left_3="player/bosses/alex/left/atk3(16).png"
creep_10_attack_left_4="player/bosses/alex/left/atk4(17).png"
creep_10_attack_left_5="player/bosses/alex/left/SPECIAL(44).png"

creep_1_attack_right="player/creeps/armor/right/atk(12)right.png"
creep_2_attack_right="player/creeps/goblin/right/atk(12)right.png"
creep_3_attack_right="player/creeps/lizard/right/atk(7)right.png"
creep_4_attack_right="player/creeps/spear/right/atk(12)right.png"
creep_5_attack_right="player/creeps/sword/right/atk(12)right.png"
creep_6_attack_right_1="player/bosses/desertsoldier/right/atk1(12)right.png"
creep_6_attack_right_2="player/bosses/desertsoldier/right/atk2(12)right.png"
creep_7_attack_right_1="player/bosses/ripper/right/atk1(14)right.png"
creep_7_attack_right_2="player/bosses/ripper/right/atk2(16)right.png"
creep_8_attack_right_1="player/bosses/crab/right/atk1(8)right.png"
creep_8_attack_right_2="player/bosses/crab/right/atk2(10)right.png"
creep_9_attack_right_1="player/bosses/gladiator/right/atk1(10)right.png"
creep_9_attack_right_2="player/bosses/gladiator/right/atk2(8)right.png"
creep_10_attack_right_1="player/bosses/alex/right/atk1(15)right.png"
creep_10_attack_right_2="player/bosses/alex/right/atk2(14)right.png"
creep_10_attack_right_3="player/bosses/alex/right/atk3(16)right.png"
creep_10_attack_right_4="player/bosses/alex/right/atk4(17)right.png"
creep_10_attack_right_5="player/bosses/alex/right/SPECIAL(44)right.png"

creep_1_gothit_left=pygame.image.load("player/creeps/armor/left/gothit.png")
creep_2_gothit_left=pygame.image.load("player/creeps/goblin/left/gothit.png")
creep_3_gothit_left=pygame.image.load("player/creeps/lizard/left/gothit(6).png")
creep_4_gothit_left=pygame.image.load("player/creeps/spear/left/gothit.png")
creep_5_gothit_left=pygame.image.load("player/creeps/sword/left/gothit.png")
creep_6_gothit_left=pygame.image.load("player/bosses/desertsoldier/left/gothit.png")
creep_7_gothit_left=pygame.image.load("player/bosses/ripper/left/gothit.png")
creep_8_gothit_left=pygame.image.load("player/bosses/crab/left/gothit.png")
creep_9_gothit_left=pygame.image.load("player/bosses/gladiator/left/gothit.png")
creep_10_gothit_left=pygame.image.load("player/bosses/alex/left/gothit.png")

creep_1_gothit_right=pygame.image.load("player/creeps/armor/right/gothit_right.png")
creep_2_gothit_right=pygame.image.load("player/creeps/goblin/right/gothit_right.png")
creep_3_gothit_right=pygame.image.load("player/creeps/lizard/right/gothit(6)right.png")
creep_4_gothit_right=pygame.image.load("player/creeps/spear/right/gothit_right.png")
creep_5_gothit_right=pygame.image.load("player/creeps/sword/right/gothit_right.png")
creep_6_gothit_right=pygame.image.load("player/bosses/desertsoldier/right/gothit_right.png")
creep_7_gothit_right=pygame.image.load("player/bosses/ripper/right/gothit_right.png")
creep_8_gothit_right=pygame.image.load("player/bosses/crab/right/gothit_right.png")
creep_9_gothit_right=pygame.image.load("player/bosses/gladiator/right/gothit_right.png")
creep_10_gothit_right=pygame.image.load("player/bosses/alex/right/gothit_right.png")

creep_1_death_left="player/creeps/armor/left/death(24).png"
creep_2_death_left="player/creeps/goblin/left/death(24).png"
creep_3_death_left="player/creeps/lizard/left/death(12).png"
creep_4_death_left="player/creeps/spear/left/death(24).png"
creep_5_death_left="player/creeps/sword/left/death(24).png"
creep_6_death_left="player/bosses/desertsoldier/left/death(48).png"
creep_7_death_left="player/bosses/ripper/left/death(48).png"
creep_8_death_left="player/bosses/crab/left/death(49).png"
creep_9_death_left="player/bosses/gladiator/left/death(50).png"
creep_10_death_left="player/bosses/alex/left/death(48).png"


creep_1_death_right="player/creeps/armor/right/death(24)right.png"
creep_2_death_right="player/creeps/goblin/right/death(24)right.png"
creep_3_death_right="player/creeps/lizard/right/death(12)right.png"
creep_4_death_right="player/creeps/spear/right/death(24)right.png"
creep_5_death_right="player/creeps/sword/right/death(24)right.png"
creep_6_death_right="player/bosses/desertsoldier/right/death(48)right.png"
creep_7_death_right="player/bosses/ripper/right/death(48)right.png"
creep_8_death_right="player/bosses/crab/right/death(49)right.png"
creep_9_death_right="player/bosses/gladiator/right/death(50)right.png"
creep_10_death_right="player/bosses/alex/right/death(48)right.png"

creep_1_idle_left=pygame.image.load("player/creeps/armor/left/idle.png")
creep_2_idle_left=pygame.image.load("player/creeps/goblin/left/idle.png")
creep_3_idle_left=pygame.image.load("player/creeps/lizard/left/idle.png")
creep_4_idle_left=pygame.image.load("player/creeps/spear/left/idle.png")
creep_5_idle_left=pygame.image.load("player/creeps/sword/left/idle.png")
creep_6_idle_left=pygame.image.load("player/bosses/desertsoldier/left/idle.png")
creep_7_idle_left=pygame.image.load("player/bosses/ripper/left/idle.png")
creep_8_idle_left=pygame.image.load("player/bosses/crab/left/idle.png")
creep_9_idle_left=pygame.image.load("player/bosses/gladiator/left/idle.png")
creep_10_idle_left=pygame.image.load("player/bosses/alex/left/idle.png")

creep_1_idle_right=pygame.image.load("player/creeps/armor/right/idle_right.png")
creep_2_idle_right=pygame.image.load("player/creeps/goblin/right/idle_right.png")
creep_3_idle_right=pygame.image.load("player/creeps/lizard/right/idle_right.png")
creep_4_idle_right=pygame.image.load("player/creeps/spear/right/idle_right.png")
creep_5_idle_right=pygame.image.load("player/creeps/sword/right/idle_right.png")
creep_6_idle_right=pygame.image.load("player/bosses/desertsoldier/right/idle_right.png")
creep_7_idle_right=pygame.image.load("player/bosses/ripper/right/idle_right.png")
creep_8_idle_right=pygame.image.load("player/bosses/crab/right/idle_right.png")
creep_9_idle_right=pygame.image.load("player/bosses/gladiator/right/idle_right.png")
creep_10_idle_right=pygame.image.load("player/bosses/alex/right/idle_right.png")

global creep_animation_list

creep_animation_list=[[creep_1_walk_left,creep_2_walk_left,creep_3_walk_left,creep_4_walk_left,creep_5_walk_left,creep_6_walk_left,creep_7_walk_left,creep_8_walk_left,creep_9_walk_left,creep_10_walk_left],
                      [creep_1_walk_right,creep_2_walk_right,creep_3_walk_right,creep_4_walk_right,creep_5_walk_right,creep_6_walk_right,creep_7_walk_right,creep_8_walk_right,creep_9_walk_right,creep_10_walk_right],
                      [creep_1_attack_left,creep_2_attack_left,creep_3_attack_left,creep_4_attack_left,creep_5_attack_left,creep_6_attack_left_1,creep_6_attack_left_2,creep_7_attack_left_1,creep_7_attack_left_2,creep_8_attack_left_1,creep_8_attack_left_2,creep_9_attack_left_1,creep_9_attack_left_2,creep_10_attack_left_1,creep_10_attack_left_2,creep_10_attack_left_3,creep_10_attack_left_4,creep_10_attack_left_5],
                      [creep_1_attack_right,creep_2_attack_right,creep_3_attack_right,creep_4_attack_right,creep_5_attack_right,creep_6_attack_right_1,creep_6_attack_right_2,creep_7_attack_right_1,creep_7_attack_right_2,creep_8_attack_right_1,creep_8_attack_right_2,creep_9_attack_right_1,creep_9_attack_right_2,creep_10_attack_right_1,creep_10_attack_right_2,creep_10_attack_right_3,creep_10_attack_right_4,creep_10_attack_right_5],
                      [creep_1_gothit_left,creep_2_gothit_left,creep_3_gothit_left,creep_4_gothit_left,creep_5_gothit_left,creep_6_gothit_left,creep_7_gothit_left,creep_8_gothit_left,creep_9_gothit_left,creep_10_gothit_left],
                      [creep_1_gothit_right,creep_2_gothit_right,creep_3_gothit_right,creep_4_gothit_right,creep_5_gothit_right,creep_6_gothit_right,creep_7_gothit_right,creep_8_gothit_right,creep_9_gothit_right,creep_10_gothit_right],
                      [creep_1_death_left,creep_2_death_left,creep_3_death_left,creep_4_death_left,creep_5_death_left,creep_6_death_left,creep_7_death_left,creep_8_death_left,creep_9_death_left,creep_10_death_left],
                      [creep_1_death_right,creep_2_death_right,creep_3_death_right,creep_4_death_right,creep_5_death_right,creep_6_death_right,creep_7_death_right,creep_8_death_right,creep_9_death_right,creep_10_death_right],
                      [creep_1_idle_left,creep_2_idle_left,creep_3_idle_left,creep_4_idle_left,creep_5_idle_left,creep_6_idle_left,creep_7_idle_left,creep_8_idle_left,creep_9_idle_left,creep_10_idle_left],
                      [creep_1_idle_right,creep_2_idle_right,creep_3_idle_right,creep_4_idle_right,creep_5_idle_right,creep_6_idle_right,creep_7_idle_right,creep_8_idle_right,creep_9_idle_right,creep_10_idle_right]]
#2d array list, index 0 is walk left, 1 is walk right, 2 is attack left, 3 is attack right, 4 is got hit left, 5 is got hit right, 6 is death left, 7 is death right
# 8 is idle left, 9 is idle right
#starting from creep 6 is bosses, they each have 2 attacks, final boss has 5
def enemy_animation(direction, creep_type, change_x, creep_x, creep_y, is_attacking, is_attacked, is_dead, frame_rate, atk_type):
    global enemy_sprite
    if creep_type == 1:
        if is_attacking == 0:
            if change_x<0:
                enemy_sprite = creep_animation_list[0][0]
                enemy_image = blank
                image_x = creep_x-7
                image_y = creep_y-5
                frame_rate = 4
            if change_x>0:
                enemy_sprite = creep_animation_list[1][0]
                enemy_image = blank
                image_x = creep_x-10
                image_y = creep_y-5
                frame_rate = 4
            if change_x == 0:
                enemy_sprite = blank_animation
                if direction == 0:
                    enemy_image = creep_animation_list[8][0]
                    image_x = creep_x-7
                    image_y = creep_y-5
                if direction == 1:
                    enemy_image = creep_animation_list[9][0]
                    image_x = creep_x-7
                    image_y = creep_y-5
        if is_attacking == 1:
            frame_rate = 12
            enemy_image = blank
            if direction == 0:
                enemy_sprite = creep_animation_list[2][0]
                image_x = creep_x-7
                image_y = creep_y-5
            if direction == 1:
                enemy_sprite = creep_animation_list[3][0]
                image_x = creep_x-7
                image_y = creep_y-5
        if is_attacked == 1:
            enemy_sprite = blank_animation
            if direction == 0:
                enemy_image = creep_animation_list[4][0]
                image_x = creep_x-7
                image_y = creep_y-5
            if direction == 1:
                enemy_image = creep_animation_list[5][0]
                image_x = creep_x-7
                image_y = creep_y-5
        if is_dead == 1:
            frame_rate = 24
            enemy_image = blank
            if direction == 0:
                enemy_sprite = creep_animation_list[6][0]
                image_x = creep_x-7
                image_y = creep_y-5
            if direction == 1:
                enemy_sprite = creep_animation_list[7][0]
                image_x = creep_x-7
                image_y = creep_y-5
        
    if creep_type == 2:
        if is_attacking == 0:
            if change_x<0:
                enemy_sprite = creep_animation_list[0][1]
                enemy_image = blank
                image_x = creep_x-8
                image_y = creep_y-2
                frame_rate = 4
            if change_x>0:
                enemy_sprite = creep_animation_list[1][1]
                enemy_image = blank
                image_x = creep_x-14
                image_y = creep_y-2
                frame_rate = 4
            if change_x == 0:
                enemy_sprite = blank_animation
                if direction == 0:
                    enemy_image = creep_animation_list[8][1]
                    image_x = creep_x-12
                    image_y = creep_y-2
                if direction == 1:
                    enemy_image = creep_animation_list[9][1]
                    image_x = creep_x-6
                    image_y = creep_y-2
        if is_attacking == 1:
            frame_rate = 12
            enemy_image = blank
            if direction == 0:
                enemy_sprite = creep_animation_list[2][1]
                image_x = creep_x-7
                image_y = creep_y-5
            if direction == 1:
                enemy_sprite = creep_animation_list[3][1]
                image_x = creep_x-7
                image_y = creep_y-5
        if is_attacked == 1:
            enemy_sprite = blank_animation
            if direction == 0:
                enemy_image = creep_animation_list[4][1]
                image_x = creep_x-7
                image_y = creep_y-5
            if direction == 1:
                enemy_image = creep_animation_list[5][1]
                image_x = creep_x-7
                image_y = creep_y-5
        if is_dead == 1:
            frame_rate = 24
            enemy_image = blank
            if direction == 0:
                enemy_sprite = creep_animation_list[6][1]
                image_x = creep_x-7
                image_y = creep_y-5
            if direction == 1:
                enemy_sprite = creep_animation_list[7][1]
                image_x = creep_x-7
                image_y = creep_y-5
        
##    if creep_type == 3:
##        if change_x<0:
##            enemy_sprite = creep_animation_list[0][2]
##            enemy_image = blank
##            image_x = creep_x-6
##            image_y = creep_y-6
##        if change_x>0:
##            enemy_sprite = creep_animation_list[1][2]
##            enemy_image = blank
##            image_x = creep_x-60
##            image_y = creep_y-6
##        if change_x == 0:
##            enemy_sprite = blank_animation
##            if direction == 0:
##                enemy_image = creep_animation_list[8][2]
##                image_x = creep_x-6
##                image_y = creep_y-12
##            if direction == 1:
##                enemy_image = creep_animation_list[9][2]
##                image_x = creep_x-40
##                image_y = creep_y-12
##        if is_dead == 1:
##            enemy_image = blank
##            if direction == 0:
##                enemy_sprite = creep_animation_list[6][2]
##                image_x = creep_x-7
##                image_y = creep_y-5
##            if direction == 1:
##                enemy_sprite = creep_animation_list[7][2]
##                image_x = creep_x-7
##                image_y = creep_y-5
##        lst = [enemy_sprite, enemy_image, image_x, image_y]

    if creep_type == 3:
        if is_attacking == 0:
            if change_x<0:
                enemy_sprite = creep_animation_list[0][3]
                enemy_image = blank
                image_x = creep_x-37
                image_y = creep_y-5
                frame_rate = 4
            if change_x>0:
                enemy_sprite = creep_animation_list[1][3]
                enemy_image = blank
                image_x = creep_x-15
                image_y = creep_y-5
                frame_rate = 4
            if change_x == 0:
                enemy_sprite = blank_animation
                if direction == 0:
                    enemy_image = creep_animation_list[8][3]
                    image_x = creep_x-45
                    image_y = creep_y-10
                if direction == 1:
                    enemy_image = creep_animation_list[9][3]
                    image_x = creep_x-10
                    image_y = creep_y-5
        if is_attacking == 1:
            frame_rate = 12
            enemy_image = blank
            if direction == 0:
                enemy_sprite = creep_animation_list[2][3]
                image_x = creep_x-107
                image_y = creep_y-5
            if direction == 1:
                enemy_sprite = creep_animation_list[3][3]
                image_x = creep_x-25
                image_y = creep_y-5
        if is_attacked == 1:
            enemy_sprite = blank_animation
            if direction == 0:
                enemy_image = creep_animation_list[4][3]
                image_x = creep_x-47
                image_y = creep_y-5
            if direction == 1:
                enemy_image = creep_animation_list[5][3]
                image_x = creep_x-7
                image_y = creep_y-5
        if is_dead == 1:
            frame_rate = 24
            enemy_image = blank
            if direction == 0:
                enemy_sprite = creep_animation_list[6][3]
                image_x = creep_x-49
                image_y = creep_y-5
            if direction == 1:
                enemy_sprite = creep_animation_list[7][3]
                image_x = creep_x-22
                image_y = creep_y-5


    if creep_type == 4:
        if is_attacking == 0:
            if change_x<0:
                enemy_sprite = creep_animation_list[0][4]
                enemy_image = blank
                image_x = creep_x-7
                image_y = creep_y-5
                frame_rate = 4
            if change_x>0:
                enemy_sprite = creep_animation_list[1][4]
                enemy_image = blank
                image_x = creep_x-30
                image_y = creep_y-5
                frame_rate = 4
            if change_x == 0:
                enemy_sprite = blank_animation
                if direction == 0:
                    enemy_image = creep_animation_list[8][4]
                    image_x = creep_x-7
                    image_y = creep_y-5
                if direction == 1:
                    enemy_image = creep_animation_list[9][4]
                    image_x = creep_x-27
                    image_y = creep_y-5
        if is_attacking == 1:
            frame_rate = 12
            enemy_image = blank
            if direction == 0:
                enemy_sprite = creep_animation_list[2][4]
                image_x = creep_x-57
                image_y = creep_y-5
            if direction == 1:
                enemy_sprite = creep_animation_list[3][4]
                image_x = creep_x-35
                image_y = creep_y-5
        if is_attacked == 1:
            enemy_sprite = blank_animation
            if direction == 0:
                enemy_image = creep_animation_list[4][4]
                image_x = creep_x-7
                image_y = creep_y-5
            if direction == 1:
                enemy_image = creep_animation_list[5][4]
                image_x = creep_x-7
                image_y = creep_y-5
        if is_dead == 1:
            frame_rate = 24
            enemy_image = blank
            if direction == 0:
                enemy_sprite = creep_animation_list[6][4]
                image_x = creep_x-7
                image_y = creep_y-5
            if direction == 1:
                enemy_sprite = creep_animation_list[7][4]
                image_x = creep_x-7
                image_y = creep_y-5
    if creep_type == 5: #first boss, desert soldier
        if is_attacking == 0:
            if change_x<0:
                enemy_sprite = creep_animation_list[0][5]
                enemy_image = blank
                image_x = creep_x-7
                image_y = creep_y-1
                frame_rate = 1
            if change_x>0:
                enemy_sprite = creep_animation_list[1][5]
                enemy_image = blank
                image_x = creep_x-10
                image_y = creep_y-1
                frame_rate = 1
            if change_x == 0:
                enemy_sprite = blank_animation
                if direction == 0:
                    enemy_image = creep_animation_list[8][5]
                    image_x = creep_x-27
                    image_y = creep_y-3
                if direction == 1:
                    enemy_image = creep_animation_list[9][5]
                    image_x = creep_x-7
                    image_y = creep_y-3
        if is_attacking == 1:
            frame_rate = 12
            enemy_image = blank
            if direction == 0:
                if atk_type == 1:
                    enemy_sprite = creep_animation_list[2][5]
                    image_x = creep_x-77
                    image_y = creep_y-5
                if atk_type == 2:
                    enemy_sprite = creep_animation_list[2][6]
                    image_x = creep_x-77
                    image_y = creep_y-5
            if direction == 1:
                if atk_type == 1:
                    enemy_sprite = creep_animation_list[3][5]
                    image_x = creep_x-7
                    image_y = creep_y-5
                if atk_type == 2:
                    enemy_sprite = creep_animation_list[3][6]
                    image_x = creep_x-17
                    image_y = creep_y-5
        if is_attacked == 1:
            enemy_sprite = blank_animation
            if direction == 0:
                enemy_image = creep_animation_list[4][5]
                image_x = creep_x-7
                image_y = creep_y-3
            if direction == 1:
                enemy_image = creep_animation_list[5][5]
                image_x = creep_x-7
                image_y = creep_y-3
        if is_dead == 1:
            frame_rate = 48
            enemy_image = blank
            if direction == 0:
                enemy_sprite = creep_animation_list[6][5]
                image_x = creep_x-7
                image_y = creep_y-3
            if direction == 1:
                enemy_sprite = creep_animation_list[7][5]
                image_x = creep_x-7
                image_y = creep_y-3
    if creep_type == 6: #second boss, ripper
        if is_attacking == 0:
            if change_x<0:
                enemy_sprite = creep_animation_list[0][6]
                enemy_image = blank
                image_x = creep_x-7
                image_y = creep_y-5
                frame_rate = 1
            if change_x>0:
                enemy_sprite = creep_animation_list[1][6]
                enemy_image = blank
                image_x = creep_x-30
                image_y = creep_y-5
                frame_rate = 1
            if change_x == 0:
                enemy_sprite = blank_animation
                if direction == 0:
                    enemy_image = creep_animation_list[8][6]
                    image_x = creep_x-15
                    image_y = creep_y-15
                if direction == 1:
                    enemy_image = creep_animation_list[9][6]
                    image_x = creep_x-30
                    image_y = creep_y-15
        if is_attacking == 1:
            enemy_image = blank
            if direction == 0:
                if atk_type == 1:
                    frame_rate = 14
                    enemy_sprite = creep_animation_list[2][7]
                    image_x = creep_x-25
                    image_y = creep_y-30
                if atk_type == 2:
                    frame_rate = 16
                    enemy_sprite = creep_animation_list[2][8]
                    image_x = creep_x-57
                    image_y = creep_y-25
            if direction == 1:
                if atk_type == 1:
                    frame_rate = 14
                    enemy_sprite = creep_animation_list[3][7]
                    image_x = creep_x-15
                    image_y = creep_y-30
                if atk_type == 2:
                    frame_rate = 16
                    enemy_sprite = creep_animation_list[3][8]
                    image_x = creep_x-27
                    image_y = creep_y-25
        if is_attacked == 1:
            enemy_sprite = blank_animation
            if direction == 0:
                enemy_image = creep_animation_list[4][6]
                image_x = creep_x-7
                image_y = creep_y-18
            if direction == 1:
                enemy_image = creep_animation_list[5][6]
                image_x = creep_x-7
                image_y = creep_y-18
        if is_dead == 1:
            frame_rate = 48
            enemy_image = blank
            if direction == 0:
                enemy_sprite = creep_animation_list[6][6]
                image_x = creep_x-7
                image_y = creep_y-18
            if direction == 1:
                enemy_sprite = creep_animation_list[7][6]
                image_x = creep_x-7
                image_y = creep_y-18
    if creep_type == 7: #third boss, crab
        if is_attacking == 0:
            if change_x<0:
                enemy_sprite = creep_animation_list[0][7]
                enemy_image = blank
                image_x = creep_x-7
                image_y = creep_y-13
                frame_rate = 6
            if change_x>0:
                enemy_sprite = creep_animation_list[1][7]
                enemy_image = blank
                image_x = creep_x-10
                image_y = creep_y-13
                frame_rate = 6
            if change_x == 0:
                enemy_sprite = blank_animation
                if direction == 0:
                    enemy_image = creep_animation_list[8][7]
                    image_x = creep_x-7
                    image_y = creep_y-13
                if direction == 1:
                    enemy_image = creep_animation_list[9][7]
                    image_x = creep_x-7
                    image_y = creep_y-13
        if is_attacking == 1:
            enemy_image = blank
            if direction == 0:
                if atk_type == 1:
                    frame_rate = 8
                    enemy_sprite = creep_animation_list[2][9]
                    image_x = creep_x-7
                    image_y = creep_y-13
                if atk_type == 2:
                    frame_rate = 10
                    enemy_sprite = creep_animation_list[2][10]
                    image_x = creep_x-7
                    image_y = creep_y-13
            if direction == 1:
                if atk_type == 1:
                    frame_rate = 8
                    enemy_sprite = creep_animation_list[3][9]
                    image_x = creep_x-7
                    image_y = creep_y-13
                if atk_type == 2:
                    frame_rate = 10
                    enemy_sprite = creep_animation_list[3][10]
                    image_x = creep_x-7
                    image_y = creep_y-13
        if is_attacked == 1:
            enemy_sprite = blank_animation
            if direction == 0:
                enemy_image = creep_animation_list[4][7]
                image_x = creep_x-7
                image_y = creep_y-13
            if direction == 1:
                enemy_image = creep_animation_list[5][7]
                image_x = creep_x-7
                image_y = creep_y-13
        if is_dead == 1:
            frame_rate = 49
            enemy_image = blank
            if direction == 0:
                enemy_sprite = creep_animation_list[6][7]
                image_x = creep_x-7
                image_y = creep_y-13
            if direction == 1:
                enemy_sprite = creep_animation_list[7][7]
                image_x = creep_x-7
                image_y = creep_y-13
    if creep_type == 8: #fourth boss, gladiator
        if is_attacking == 0:
            if change_x<0:
                enemy_sprite = creep_animation_list[0][8]
                enemy_image = blank
                image_x = creep_x-17
                image_y = creep_y-5
                frame_rate = 1
            if change_x>0:
                enemy_sprite = creep_animation_list[1][8]
                enemy_image = blank
                image_x = creep_x-20
                image_y = creep_y-5
                frame_rate = 1
            if change_x == 0:
                enemy_sprite = blank_animation
                if direction == 0:
                    enemy_image = creep_animation_list[8][8]
                    image_x = creep_x-7
                    image_y = creep_y-18
                if direction == 1:
                    enemy_image = creep_animation_list[9][8]
                    image_x = creep_x-27
                    image_y = creep_y-18
        if is_attacking == 1:
            enemy_image = blank
            if direction == 0:
                if atk_type == 1:
                    frame_rate = 10
                    enemy_sprite = creep_animation_list[2][11]
                    image_x = creep_x-67
                    image_y = creep_y-48
                if atk_type == 2:
                    frame_rate = 8
                    enemy_sprite = creep_animation_list[2][12]
                    image_x = creep_x-92
                    image_y = creep_y-18
            if direction == 1:
                if atk_type == 1:
                    frame_rate = 10
                    enemy_sprite = creep_animation_list[3][11]
                    image_x = creep_x-37
                    image_y = creep_y-48
                if atk_type == 2:
                    frame_rate = 8
                    enemy_sprite = creep_animation_list[3][12]
                    image_x = creep_x-32
                    image_y = creep_y-18
        if is_attacked == 1:
            enemy_sprite = blank_animation
            if direction == 0:
                enemy_image = creep_animation_list[4][8]
                image_x = creep_x-6
                image_y = creep_y-45
            if direction == 1:
                enemy_image = creep_animation_list[5][8]
                image_x = creep_x-7
                image_y = creep_y-45
        if is_dead == 1:
            frame_rate = 50
            enemy_image = blank
            if direction == 0:
                enemy_sprite = creep_animation_list[6][8]
                image_x = creep_x-8
                image_y = creep_y-42
            if direction == 1:
                enemy_sprite = creep_animation_list[7][8]
                image_x = creep_x-7
                image_y = creep_y-42
    if creep_type == 9: #final boss, alex
        if is_attacking == 0:
            if change_x<0:
                enemy_sprite = creep_animation_list[0][9]
                enemy_image = blank
                image_x = creep_x-7
                image_y = creep_y-5
                frame_rate = 3
            if change_x>0:
                enemy_sprite = creep_animation_list[1][9]
                enemy_image = blank
                image_x = creep_x-20
                image_y = creep_y-5
                frame_rate = 3
            if change_x == 0:
                enemy_sprite = blank_animation
                if direction == 0:
                    enemy_image = creep_animation_list[8][9]
                    image_x = creep_x-17
                    image_y = creep_y-10
                if direction == 1:
                    enemy_image = creep_animation_list[9][9]
                    image_x = creep_x-7
                    image_y = creep_y-10
        if is_attacking == 1:
            enemy_image = blank
            if direction == 0:
                if atk_type == 1:
                    frame_rate = 15
                    enemy_sprite = creep_animation_list[2][13]
                    image_x = creep_x-147
                    image_y = creep_y-10
                if atk_type == 2:
                    frame_rate = 14
                    enemy_sprite = creep_animation_list[2][14]
                    image_x = creep_x-67
                    image_y = creep_y-10
                if atk_type == 3:
                    frame_rate = 16
                    enemy_sprite = creep_animation_list[2][15]
                    image_x = creep_x-57
                    image_y = creep_y-50
                if atk_type == 4:
                    frame_rate = 17
                    enemy_sprite = creep_animation_list[2][16]
                    image_x = creep_x-60
                    image_y = creep_y-20
                if atk_type == 5:
                    frame_rate = 44
                    enemy_sprite = creep_animation_list[2][17]
                    image_x = creep_x-7
                    image_y = creep_y-50
            if direction == 1:
                if atk_type == 1:
                    frame_rate = 15
                    enemy_sprite = creep_animation_list[3][13]
                    image_x = creep_x-27
                    image_y = creep_y-10
                if atk_type == 2:
                    frame_rate = 14
                    enemy_sprite = creep_animation_list[3][14]
                    image_x = creep_x-17
                    image_y = creep_y-10
                if atk_type == 3:
                    frame_rate = 16
                    enemy_sprite = creep_animation_list[3][15]
                    image_x = creep_x-7
                    image_y = creep_y-50
                if atk_type == 4:
                    frame_rate = 17
                    enemy_sprite = creep_animation_list[3][16]
                    image_x = creep_x-14
                    image_y = creep_y-20
                if atk_type == 5:
                    frame_rate = 44
                    enemy_sprite = creep_animation_list[3][17]
                    image_x = creep_x-7
                    image_y = creep_y-50
        if is_attacked == 1:
            enemy_sprite = blank_animation
            if direction == 0:
                enemy_image = creep_animation_list[4][9]
                image_x = creep_x-25
                image_y = creep_y-9
            if direction == 1:
                enemy_image = creep_animation_list[5][9]
                image_x = creep_x-8
                image_y = creep_y-9
        if is_dead == 1:
            frame_rate = 48
            enemy_image = blank
            if direction == 0:
                enemy_sprite = creep_animation_list[6][9]
                image_x = creep_x-25
                image_y = creep_y-9
            if direction == 1:
                enemy_sprite = creep_animation_list[7][9]
                image_x = creep_x-8
                image_y = creep_y-9
    lst = [enemy_sprite, enemy_image, image_x, image_y, frame_rate]

    return lst


