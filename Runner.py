from ctypes.wintypes import SC_HANDLE
from glob import glob
from multiprocessing import set_forkserver_preload
from re import S
import threading
import pygame, threading
from sys import exit
import random
from pygame import K_ESCAPE, K_RIGHT, K_UP, MOUSEBUTTONUP, font, init, mixer
import time
import math
gameover = pygame.image.load("background/menubackground.jpg")
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
clock = pygame.time.Clock()
bgX = 0
bgX_menu = 0
restart_player = 0
restart_snail = 0
icon = pygame.image.load("background/running1.png")
pygame.display.set_icon(icon)
menu_active = True
shop_coming_a = False
options_volume_on  = True
options_volume_off = False
friends = False
map_pick = False
game_active = False
loading_active = False
escactive = False
player_moving = True
move = False

mixer.init()
file =('sound_effects/main_music.mp3')
mixer.music.load(file)
mixer.music.set_volume(0.5)
mixer.music.play(-1)
music_active = True
timer = 0

coins = 0

s = 0
froze = 0
reset_flag = True
spell = False
spell2 = False
ice_spell_flag = False
ice_spell_flag_back = False
fire_spell_flag = False
fire_spell_flag_back = False
unrealengineflag = True
unrealtimer = 0
#####SOUND EFFECTS #######
coin_effect = mixer.Sound('sound_effects/CollectCoinSoundEffect.wav')
click_effect = mixer.Sound('sound_effects/cilick_mouse.wav')
click_effect.set_volume(0.4)
jump_effect = mixer.Sound('sound_effects/jump_effect.wav')
jump_effect.set_volume(0.09)
ice_effect = mixer.Sound('sound_effects/ice_effect.wav')
ice_effect.set_volume(0.1)
fire_effect = mixer.Sound('sound_effects/fire_ball_effect.wav')
fire_effect.set_volume(0.1)
kill_snail_effect = mixer.Sound('sound_effects/kil_snail_effect.wav')

class Background():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Maze Runner')
        self.clock = pygame.time.Clock()
        
        self.restart_timer = pygame.time.get_ticks()
        # Creating text and timer
        
        self.text_font_for_score = pygame.font.Font('fonts/LeagueGothic-Regular.otf',50)

        self.text_font = pygame.font.Font('fonts/ChrustyRock-ORLA.ttf',40)
        
      
        
        # Creating BG
        self.background_surface = pygame.image.load('background/background.jpg')
        self.background_surface = pygame.transform.scale(self.background_surface,(1280,740)).convert_alpha()
        self.background2 = pygame.image.load("background/background1.jpg")
        self.background2 = pygame.transform.scale(self.background2,(1280,740)).convert_alpha()
        self.background3 = pygame.image.load("background/background2.jpg")
        self.background3 = pygame.transform.scale(self.background3,(1280,740)).convert_alpha()
    def screen_blit(self):
        screen.blit(self.background_surface,(bgX,0))
        screen.blit(self.background2, (WIDTH+bgX-11, 0))
        screen.blit(self.background3, (WIDTH*2+bgX-11, 0))
        screen.blit(self.background_surface, (WIDTH*3+bgX-11, 0))
        screen.blit(self.background2, (WIDTH*4 + bgX - 11, 0))
        screen.blit(self.background3, (WIDTH * 5 + bgX - 11, 0))
        screen.blit(self.background_surface, (WIDTH*6+bgX -11, 0))
        screen.blit(self.background2, (WIDTH*7 + bgX - 11, 0))
        screen.blit(self.background3, (WIDTH * 8 + bgX - 11, 0))
        screen.blit(self.background_surface, (WIDTH*9+bgX-11, 0))
        screen.blit(self.background2, (WIDTH*10 + bgX - 11, 0))
        screen.blit(self.background3, (WIDTH * 11 + bgX - 11, 0))
    def timer(self):
        global timer
        self.set_timer = self.restart_timer - self.restart_timer + int(timer)
        self.timer_text = self.text_font_for_score.render(f'TIMER:{self.set_timer}', 1, '#072d2d')
        screen.blit(self.timer_text, (600, 20))
    
    def restart_timer(self):
        self.set_timer -= self.restart_timer
        
    def total_restart_timer(self):
        global timer
        timer = 0
class main_menu(Background):
    def __init__(self):
        super().__init__()
    
        self.backgroundmenu = pygame.image.load("background/menubackground.jpg")
        self.backgroundmenu = pygame.transform.scale(self.backgroundmenu,(1280,740))
        self.text_font = pygame.font.Font("fonts/ChrustyRock-ORLA.ttf",50)
        self.background_text = pygame.image.load("background/menutext.png")
        self.unreallogo = pygame.image.load("images/unreallogo.png")
        self.unreallogo = pygame.transform.scale(self.unreallogo, (250, 180))
        self.roglogo = pygame.image.load("images/roglogo.png")
        self.roglogo = pygame.transform.scale(self.roglogo, (210, 80))
        self.nvidialogo = pygame.image.load("images/nvidialogo.png")
        self.nvidialogo = pygame.transform.scale(self.nvidialogo, (300, 200))
        self.rtxlogo = pygame.image.load("images/rtxonlogo.png")
        self.rtxlogo = pygame.transform.scale(self.rtxlogo, (250, 200))
        self.intellogo = pygame.image.load("images/intellogo.png")
        self.intellogo = pygame.transform.scale(self.intellogo, (250, 80))


        
        
    def esc(self):
        global escactive,game_active,menu_active,map_pick,reset_flag,s
        self.cx, self.cy = pygame.mouse.get_pos()
        self.keys = pygame.key.get_pressed()
        
        if self.keys[pygame.K_ESCAPE]:
            escactive = True
        if self.cx > 770 and self.cx < 806 and self.cy > 286 and self.cy < 325:
            if event.type == pygame.MOUSEBUTTONDOWN:
                escactive = False
        if self.cx > 479 and self.cx < 786 and self.cy > 406 and self.cy < 445:
            if event.type == pygame.MOUSEBUTTONDOWN:
                escactive = False
                game_active = False
                menu_active = True
                map_pick = False
                s = 0
                
                
                if reset_flag == False:
                    reset_flag = True
                else:
                    reset_flag = False

    def esc_menu(self):
            global escactive
            self.escphoto = pygame.image.load("images/escmenu.png")
            if escactive:
                screen.blit(self.escphoto,(350, 180))
            elif escactive == False:
                pass
                
    def menu_background(self):
        screen.blit(self.backgroundmenu,(bgX_menu,0))
        screen.blit(self.backgroundmenu,(WIDTH * 1 + bgX_menu , 0))
        screen.blit(self.backgroundmenu, (WIDTH * 2 + bgX_menu, 0))
        screen.blit(self.backgroundmenu, (WIDTH * 3 + bgX_menu, 0))
        screen.blit(self.backgroundmenu, (WIDTH * 4 + bgX_menu, 0))
        screen.blit(self.backgroundmenu, (WIDTH * 5 + bgX_menu, 0))
        screen.blit(self.backgroundmenu, (WIDTH * 6 + bgX_menu, 0))
        screen.blit(self.backgroundmenu, (WIDTH * 7 + bgX_menu, 0))
        screen.blit(self.backgroundmenu, (WIDTH * 8 + bgX_menu, 0))
        screen.blit(self.backgroundmenu, (WIDTH * 9 + bgX_menu, 0))
        screen.blit(self.backgroundmenu, (WIDTH * 10 + bgX_menu, 0))
        screen.blit(self.backgroundmenu, (WIDTH * 11 + bgX_menu, 0))
        screen.blit(self.backgroundmenu, (WIDTH * 12 + bgX_menu, 0))
        screen.blit(self.backgroundmenu, (WIDTH * 13 + bgX_menu, 0))
        screen.blit(self.backgroundmenu, (WIDTH * 14 + bgX_menu, 0))
        screen.blit(self.backgroundmenu, (WIDTH * 15 + bgX_menu, 0))
        screen.blit(self.backgroundmenu, (WIDTH * 16 + bgX_menu, 0))
        screen.blit(self.backgroundmenu, (WIDTH * 17 + bgX_menu, 0))
        screen.blit(self.backgroundmenu, (WIDTH * 18 + bgX_menu, 0))
        screen.blit(self.backgroundmenu, (WIDTH * 19 + bgX_menu, 0))
        screen.blit(self.backgroundmenu, (WIDTH * 20 + bgX_menu, 0))
        screen.blit(self.backgroundmenu, (WIDTH * 21 + bgX_menu, 0))
        screen.blit(self.backgroundmenu, (WIDTH * 22 + bgX_menu, 0))
        screen.blit(self.background_text, (-490, 10))
        #screen.blit(self.unreallogo, (0,30))
        #screen.blit(self.roglogo, (20,210))
        #screen.blit(self.nvidialogo, (-20, 280))
        #screen.blit(self.rtxlogo,(20, 400))
        #screen.blit(self.intellogo, (20, 570))
    def start_text(self):
        play_text = self.text_font.render("CLICK TO PLAY", 1, "White")
        screen.blit(play_text,(470,360))
    def shop_text(self):
        shop_txt = self.text_font.render("SHOP", 1, "White")
        screen.blit(shop_txt,(593, 450))

    def settings_text(self):
        settings_txt = self.text_font.render("SETTINGS", 1, "White")
        screen.blit(settings_txt,(532, 537))

    def exit_text(self):
        exit_txt = self.text_font.render("EXIT", 1, "White")

        screen.blit(exit_txt,(602, 615))

    def hover(self):
        self.mx, self.my = pygame.mouse.get_pos()
        play_text_hover = self.text_font.render("CLICK TO PLAY", 1, "#2dac8d")
        shop_txt_hover = self.text_font.render("SHOP", 1, "#2dac8d")
        settings_txt_hover = self.text_font.render("SETTINGS", 1, "#2dac8d")
        exit_txt_hover = self.text_font.render("EXIT", 1, "#2dac8d")
        self.arrow = pygame.image.load("background/arrow.png")
        self.arrow = pygame.transform.scale(self.arrow, (45, 45))
        self.arrow2 = pygame.image.load("background/arrow.png")
        self.arrow2 = pygame.transform.rotate(self.arrow2, 180)
        self.arrow2 = pygame.transform.scale(self.arrow2, (45, 45))
        if self.mx >= 470 and self.mx < 850 and self.my >= 360 and self.my < 400:
            screen.blit(play_text_hover, (470, 357))
            screen.blit(self.arrow, (410, 360))
            screen.blit(self.arrow2, (855, 360))

        if self.mx >= 593 and self.mx < 734 and self.my >= 450 and self.my < 490:
            screen.blit(shop_txt_hover, (593, 447))
            screen.blit(self.arrow, (540, 450))
            screen.blit(self.arrow2, (740, 450))

        if self.mx >= 532 and self.mx < 790 and self.my >= 537 and self.my < 576:
            screen.blit(settings_txt_hover, (532, 534))
            screen.blit(self.arrow, (470, 533))
            screen.blit(self.arrow2, (800, 533))

        if self.mx >= 602 and self.mx < 723 and self.my >= 615 and self.my < 654:
            screen.blit(exit_txt_hover, (602, 612))
            screen.blit(self.arrow, (550, 610))
            screen.blit(self.arrow2, (725, 610))

    def click(self):
        global menu_active
        global map_pick
        global music_active
        if event.type == pygame.MOUSEBUTTONDOWN and self.mx >= 470 and self.mx < 850 and self.my >= 360 and self.my < 400:
            if event.button == 1:
                menu_active = False
                map_pick = True
                
                click_effect.play()
            


        if event.type == pygame.MOUSEBUTTONDOWN and self.mx >= 602 and self.mx < 723 and self.my >= 615 and self.my < 654:
            if event.button == 1:

                exit()

    def shop_coming(self):
        global shop_coming_a
        global menu_active
        if self.mx >= 593 and self.mx < 734 and self.my >= 450 and self.my < 490:
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    shop_coming_a = True
                    menu_active = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_effect.play()

    def shop_coming_exit(self):
        global shop_coming_a
        global menu_active
        self.cx, self.cy = pygame.mouse.get_pos()
        if self.cx > 17  and self.cx < 564 and self.cy >= 636 and self.cy < 690:
            if event.type == pygame.MOUSEBUTTONDOWN:
                shop_coming_a = False
                menu_active = True
                click_effect.play()

    def buy_unavailable(self):
        self.cx, self.cy = pygame.mouse.get_pos()
        self.buyimg = pygame.image.load("background/shoperror.png")
        self.buyimg = pygame.transform.scale(self.buyimg, (1280, 740))
        if self.cx > 298 and self.cx < 419 and self.cy > 445 and self.cy < 494:
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                screen.blit(self.buyimg, (0,0))
        if self.cx > 582 and self.cx < 700 and self.cy > 445 and self.cy < 494:
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                screen.blit(self.buyimg, (0,0))
        if self.cx > 874 and self.cx < 992 and self.cy > 445 and self.cy < 494:
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                screen.blit(self.buyimg, (0,0))

    def shop_coming_window(self):
        self.cx, self.cy = pygame.mouse.get_pos()
        self.closeshop = pygame.image.load("background/shop.png")
        self.closeshop = pygame.transform.scale(self.closeshop, (1280, 740))
        screen.blit(self.closeshop, (0, 0))

    def settings_click(self):
        global options_volume_on,game_active, options_volume_off
        global menu_active
        self.mx, self.my = pygame.mouse.get_pos()
        if self.mx >= 532 and self.mx < 790 and self.my >= 537 and self.my < 576:
            if menu_active:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    menu_active = False
                    game_active = False
                    
                    click_effect.play()

    def friends(self):
        self.friends_img = pygame.image.load("background/friends.png")
        self.friends_img = pygame.transform.scale(self.friends_img, (150, 90))
        screen.blit(self.friends_img, (1150, 0))

    def friends_tab(self):
        global friends
        global  menu_active
        self.cx, self.cy = pygame.mouse.get_pos()
        if self.cx > 1150 and self.cx < 1300 and self.cy > 0 and self.cy < 90:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    friends = True
                    menu_active = False
                    click_effect.play()
                    
                   
                
        if self.cx > 984 and self.cx < 1018 and self.cy > 403 and self.cy < 437:
            if event.type == pygame.MOUSEBUTTONDOWN:
                friends = False
                menu_active = True
                click_effect.play()
            
    def friends_popup(self):
        self.friends_window = pygame.image.load("background/friendstab.png")
        screen.blit(self.friends_window,(975,0))


    def settings_mode(self):
        self.cx, self.cy = pygame.mouse.get_pos()
        self.settingsbackground2 = pygame.image.load("background/settingsbackground2.png")
        self.settingsbackground2 = pygame.transform.scale(self.settingsbackground2, (1280, 740))
        screen.blit(self.settingsbackground2,(0, 0))

    def setting_off(self):
        self.settingsbackground = pygame.image.load("background/settingsbackground1.png")
        self.settingsbackground = pygame.transform.scale(self.settingsbackground, (1280, 740))
        screen.blit(self.settingsbackground, (0, 0))
    def settings_volume(self):
        global options_volume_on, music_active
        global  options_volume_off
        self.cx, self.cy = pygame.mouse.get_pos()
        if self.cx > 204 and self.cx < 281 and self.cy > 282 and self.cy < 420:
            if event.type == pygame.MOUSEBUTTONDOWN:
                options_volume_off = False
                options_volume_on = True
                mixer.music.play()
        if options_volume_off == True:
            music_active = False
            

        if self.cx > 282 and self.cx < 359 and self.cy > 282 and self.cy < 420:
            if event.type == pygame.MOUSEBUTTONDOWN:
                options_volume_on = False
                options_volume_off = True
                mixer.music.pause()

    def settings_exit(self):
        global options_volume_on
        global menu_active
        self.cx, self.cy = pygame.mouse.get_pos()
        if self.cx > 20 and self.cx < 140 and self.cy > 580 and self.cy < 690:
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                menu_active = True
                click_effect.play()
    def map_pick(self):
        self.cx, self.cy = pygame.mouse.get_pos()
        self.mappick = pygame.image.load("background/mappick.jpg.png")
        self.mappick = pygame.transform.scale(self.mappick,  (1280, 740))
        screen.blit(self.mappick,(0, 0))

    def map_true(self):
        global map_pick , menu_active,loading_active, restart_player
        global game_active
        self.cx, self.cy = pygame.mouse.get_pos()
        if self.cx > 501 and self.cx < 784 and self.cy > 537 and self.cy < 620:
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                
                game_active = True
                map_pick = False
                menu_active = False
                click_effect.play()
                

    def map_exit(self):
        global map_pick
        global menu_active
        self.cx, self.cy = pygame.mouse.get_pos()
        if self.cx > 10 and self.cx < 395 and self.cy > 659 and self.cy < 683:
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu_active = True
                map_pick = False
                click_effect.play()
class Player(main_menu):
    def __init__(self):
        super().__init__()
        global playerx , menu_active


        self.player_stand_surface = pygame.image.load('images/playerStand.png') 
        self.player_animation_1 = pygame.image.load('images/player2.png')
        self.player_animation_2 = pygame.image.load('images/player3.png')
        self.player_animation_3 = pygame.image.load('images/player4.png')
        self.player_animation_4 = pygame.image.load('images/player.png')
        self.list_animations = [self.player_animation_1,self.player_animation_2,self.player_animation_3,self.player_animation_4]
        self.index_list = 0
        self.rect_surface_image = pygame.Rect(40,650,65,128)
        self.player_gravity = 0
        self.surface_image = self.list_animations[self.index_list]
        
        self.player_frozen = pygame.image.load('images/froze.png')
        self.player_frozen = pygame.transform.scale(self.player_frozen,(128,200))
        
        
    

    def player_input(self):
        
        global bgX, restart_player, player_moving
        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_RIGHT] and player_moving:
            self.player_animation()
            self.rect_surface_image.x +=6
            

            if self.rect_surface_image.x >= 420:
                bgX -=6
                self.rect_surface_image.x -= 6
                restart_player += 6

            screen.blit(self.surface_image, self.rect_surface_image)
        else:
            screen.blit(self.player_stand_surface,self.rect_surface_image)

        if self.keys[pygame.K_SPACE] and player_moving:
            if self.rect_surface_image.bottom >= 600:
                self.player_gravity =-18
                jump_effect.play()
                
                
        
    def apply_gravity(self):
        self.player_gravity += 1
        self.rect_surface_image.y += self.player_gravity
        if self.rect_surface_image.bottom >= 650:
            self.rect_surface_image.bottom = 650
    def player_animation(self):
        self.index_list += 0.1
        if self.index_list > len(self.list_animations):
            self.index_list = 0
        self.surface_image = self.list_animations[int(self.index_list)]   
class Obstacles(Player):
    global fbY
    def __init__(self):
        super().__init__()
        
        # Creating Snail
        self.snail_surface = pygame.image.load('images/snail.png')
        self.snail_surface2 = pygame.image.load('Animations/snail2.png')
        self.list_snail_animations = [self.snail_surface, self.snail_surface2]
        self.index_list = 0
        self.animations = self.list_snail_animations[self.index_list]
        self.animations_rect = pygame.Rect(1100, 580, 64, 64)
        # Snail 2
        self.snail_surface3 = pygame.image.load('images/snail.png')
        self.snail_surface4 = pygame.image.load('Animations/snail2.png')
        self.list_snail_animations1 = [self.snail_surface3, self.snail_surface4]
        self.index_list1 = 0
        self.animations1 = self.list_snail_animations1[self.index_list]
        self.animations_rect1 = pygame.Rect(4000, 580, 64, 64)
        self.snail_surface100 = pygame.image.load('images/snail.png')
        self.snail_surface200 = pygame.image.load('images/snail.png')
        self.lista_snijlova = [pygame.Rect(300, 580, 64, 64),pygame.Rect(500, 580, 64, 64)]
        # Snail 3
        self.snail_surface5 = pygame.image.load('images/snail.png')
        self.snail_surface6 = pygame.image.load('Animations/snail2.png')
        self.list_snail_animations2 = [self.snail_surface5, self.snail_surface6]
        self.index_list2 = 0
        self.animations2 = self.list_snail_animations2[self.index_list2]
        self.animations_rect2 = pygame.Rect(5500, 580, 64, 64)
        # Creating Bird 1
        self.bird_surf = pygame.image.load('images/bird.png').convert_alpha()
        self.bird_surf_2 = pygame.image.load('Animations/ptica1.png').convert_alpha()
        self.bird_surf_3 = pygame.image.load('Animations/ptica2.png').convert_alpha()
        self.bird_surf_4 = pygame.image.load('Animations/ptica3.png').convert_alpha()
        self.bird_surf_5 = pygame.image.load('Animations/ptica4.png').convert_alpha()
        self.bird_surf_rect = pygame.Rect(2000, 400, 64, 64)
        self.bird_list_animations = [self.bird_surf, self.bird_surf_2, self.bird_surf_3, self.bird_surf_4,
                                     self.bird_surf_5]
        self.bird_index = 0
        self.bird_surf = self.bird_list_animations[self.bird_index]
        # Creating Bird 2
        self.bird_surf6 = pygame.image.load('images/bird.png').convert_alpha()
        self.bird_surf_7 = pygame.image.load('Animations/ptica1.png').convert_alpha()
        self.bird_surf_8 = pygame.image.load('Animations/ptica2.png').convert_alpha()
        self.bird_surf_9 = pygame.image.load('Animations/ptica3.png').convert_alpha()
        self.bird_surf_10 = pygame.image.load('Animations/ptica4.png').convert_alpha()
        self.bird_surf_rect2 = pygame.Rect(3000, 330, 64, 64)
        self.bird_list_animations1 = [self.bird_surf6, self.bird_surf_7, self.bird_surf_8, self.bird_surf_9,
                                      self.bird_surf_10]
        self.bird_index1 = 0
        self.bird_surf6 = self.bird_list_animations1[self.bird_index1]
        # Creating boxes
        self.box = pygame.image.load('images/square.png')
        self.box1 = pygame.image.load('images/square.png')
        self.box2 = pygame.image.load('images/square.png')
        self.box3 = pygame.image.load('images/square.png')
        self.box4 = pygame.image.load('images/square.png')
        self.rect_box = pygame.Rect(1000, 450, 40, 64)
        self.rect_box1 = pygame.Rect(1500, 450, 40, 64)
        self.rect_box2 = pygame.Rect(1800, 450, 40, 64)
        self.rect_box3 = pygame.Rect(2300, 450, 40, 64)
        self.rect_box4 = pygame.Rect(4000, 450, 40, 64)
        self.box5 = pygame.image.load('images/square.png')
        self.box6 = pygame.image.load('images/square.png')
        self.box7 = pygame.image.load('images/square.png')
        self.box8 = pygame.image.load('images/square.png')
        self.box9 = pygame.image.load('images/square.png')
        self.rect5_box = pygame.Rect(1200, 450 - random.randint(100, 150), 40, 64)
        self.rect6_box1 = pygame.Rect(1650, 450 - random.randint(100, 150), 40, 64)
        self.rect7_box2 = pygame.Rect(1950, 450 - random.randint(100, 150), 40, 64)
        self.rect8_box3 = pygame.Rect(2420, 450 - random.randint(100, 150), 40, 64)
        self.rect9_box4 = pygame.Rect(4190, 450 - random.randint(100, 150), 40, 64)

        # Creating Flag
        self.flag1 = pygame.image.load('Animations/flag1.png')
        self.flag2 = pygame.image.load('Animations/flag2.png')
        self.flag3 = pygame.image.load('Animations/flag3.png')
        self.flag4 = pygame.image.load('Animations/flag4.png')
        self.flag5 = pygame.image.load('Animations/flag5.png')
        self.flag6 = pygame.image.load('Animations/flag6.png')
        self.list_flag_animations = [self.flag1, self.flag2, self.flag3, self.flag4, self.flag5, self.flag6]
        self.flag_index_list = 0
        self.flag_surface = self.list_flag_animations[self.flag_index_list]
        self.flag_rect = pygame.Rect(14000, 700, 64, -1000)
        # Creating Fireball and Explosion
        self.fire_ball_spell = pygame.image.load('images/golf-ball.png')
        self.fire_ball_surface_spell = pygame.image.load('images/avaiable_spell_true1.png')
        self.rect_meteor = pygame.Rect(random.randint(2000, 5500), random.randint(350, 500), 64, 64)
        self.fire_ball_backwards = pygame.image.load('images/fireball.png')
        self.fire_ball_forwards = pygame.image.load('images/fireball2.png')
        # Creating Coins
        self.coin_surface = pygame.image.load('Animations/coin1.png')
        self.coin_surface = pygame.transform.scale(self.coin_surface, (40, 40))
        self.coin2_surface = pygame.image.load('Animations/coin2.png')
        self.coin2_surface = pygame.transform.scale(self.coin2_surface, (40, 40))
        self.coin3_surface = pygame.image.load('Animations/coin3.png')
        self.coin3_surface = pygame.transform.scale(self.coin3_surface, (40, 40))
        self.coin4_surface = pygame.image.load('Animations/coin4.png')
        self.coin4_surface = pygame.transform.scale(self.coin4_surface, (40, 40))
        self.coin5_surface = pygame.image.load('Animations/coin5.png')
        self.coin5_surface = pygame.transform.scale(self.coin5_surface, (40, 40))
        self.coin6_surface = pygame.image.load('Animations/coin6.png')
        self.coin6_surface = pygame.transform.scale(self.coin6_surface, (40, 40))
        self.coin7_surface = pygame.image.load('Animations/coin7.png')
        self.coin7_surface = pygame.transform.scale(self.coin7_surface, (40, 40))
        self.coin8_surface = pygame.image.load('Animations/coin8.png')
        self.coin8_surface = pygame.transform.scale(self.coin8_surface, (40, 40))
        self.coin9_surface = pygame.image.load('Animations/coin9.png')
        self.coin9_surface = pygame.transform.scale(self.coin9_surface, (40, 40))
        self.coin10_surface = pygame.image.load('Animations/coin10.png')
        self.coin10_surface = pygame.transform.scale(self.coin10_surface, (40, 40))
        self.coin_list_index = 0
        self.coin_list_animations = [self.coin_surface, self.coin2_surface, self.coin3_surface, self.coin4_surface,
                                     self.coin5_surface, self.coin6_surface, self.coin7_surface, self.coin8_surface,
                                     self.coin9_surface, self.coin10_surface]
        self.coin_surface = self.coin_list_animations[self.coin_list_index]
        self.coin_surface_rect = pygame.Rect(1010, 400, 32, 32)
        self.coin11_surface = pygame.image.load('Animations/coin1.png')
        self.coin11_surface = pygame.transform.scale(self.coin11_surface, (40, 40))
        self.coin12_surface = pygame.image.load('Animations/coin2.png')
        self.coin12_surface = pygame.transform.scale(self.coin12_surface, (40, 40))
        self.coin13_surface = pygame.image.load('Animations/coin3.png')
        self.coin13_surface = pygame.transform.scale(self.coin13_surface, (40, 40))
        self.coin14_surface = pygame.image.load('Animations/coin4.png')
        self.coin14_surface = pygame.transform.scale(self.coin14_surface, (40, 40))
        self.coin15_surface = pygame.image.load('Animations/coin5.png')
        self.coin15_surface = pygame.transform.scale(self.coin15_surface, (40, 40))
        self.coin16_surface = pygame.image.load('Animations/coin6.png')
        self.coin16_surface = pygame.transform.scale(self.coin16_surface, (40, 40))
        self.coin17_surface = pygame.image.load('Animations/coin7.png')
        self.coin17_surface = pygame.transform.scale(self.coin17_surface, (40, 40))
        self.coin18_surface = pygame.image.load('Animations/coin8.png')
        self.coin18_surface = pygame.transform.scale(self.coin18_surface, (40, 40))
        self.coin19_surface = pygame.image.load('Animations/coin9.png')
        self.coin19_surface = pygame.transform.scale(self.coin19_surface, (40, 40))
        self.coin20_surface = pygame.image.load('Animations/coin10.png')
        self.coin20_surface = pygame.transform.scale(self.coin20_surface, (40, 40))
        self.coin_list_index1 = 0
        self.coin_list_animations1 = [self.coin11_surface, self.coin12_surface, self.coin13_surface,
                                      self.coin14_surface, self.coin15_surface, self.coin16_surface,
                                      self.coin17_surface, self.coin18_surface, self.coin19_surface,
                                      self.coin20_surface]
        self.coin11_surface = self.coin_list_animations1[self.coin_list_index1]
        self.coin11_rect = pygame.Rect(1800, 590, 32, 32)
        self.double_coin_surface = pygame.image.load("background/doublecoin.png")
        self.double_coin_surface = pygame.transform.scale(self.double_coin_surface, (80, 60))
        self.double_coin_surface_rect = pygame.Rect(random.randint(1000, 12000), 300, 30, 30)
        self.speedup = pygame.image.load("background/speedup.png")
        self.speedup = pygame.transform.scale(self.speedup, (80, 70))
        self.speedup_rect = pygame.Rect(random.randint(2500, 12000), random.randint(300, 450), 120, 60)
        # mysterybox
        self.questionmark = pygame.image.load("images/question-mark.png")
        self.questionmark = pygame.transform.scale(self.questionmark, (50, 50))
        self.questionmark_rect = pygame.Rect(random.randint(2000, 12000), random.randint(430, 500), 120, 60)
        # spell
        # Creating spell
        self.spell_animation1 = pygame.image.load('Animations/ice1.png')
        self.spell_animation2 = pygame.image.load('Animations/ice2.png')
        self.spell_animation3 = pygame.image.load('Animations/ice3.png')
        self.spell_animation4 = pygame.image.load('Animations/ice4.png')
        self.list_spell_animation = [self.spell_animation1, self.spell_animation2, self.spell_animation3,
                                     self.spell_animation4]
        self.list_index_spell_animations = 0
        self.spell_animation_rect = pygame.Rect(random.randint(2000, 5500), 400, 64, 64)
        self.bird_animation()
        self.bird_movement()
        self.snail_movement()
        self.spell_avaiable = pygame.image.load('images/avaiable_spell.png')
        self.spell_on = pygame.image.load('images/avaiable_spell_true.png')
        self.fire_spell = pygame.image.load('images/romb.png')
        self.fire_spell_rect_meteor = pygame.Rect(self.rect_surface_image.x + 60, self.rect_surface_image.y + 30,
                                                  64,
                                                  64)
        self.fire_spell_rect_back_meteor = pygame.Rect(self.rect_surface_image.x - 20,
                                                       self.rect_surface_image.y + 30,
                                                       64, 64)
        self.fire_spell_rect = pygame.Rect(self.rect_surface_image.x + 60, self.rect_surface_image.y + 30, 64, 64)
        self.fire_spell_rect_back = pygame.Rect(self.rect_surface_image.x - 20, self.rect_surface_image.y + 30, 64,
                                                64)


        ### box bottom ###

        
    def obstacles_blits(self):
       
        screen.blit(self.box, self.rect_box)
        screen.blit(self.box1, self.rect_box1)
        screen.blit(self.box2, self.rect_box2)
        screen.blit(self.box3, self.rect_box3)
        screen.blit(self.box4, self.rect_box4)
        screen.blit(self.coin_surface, self.coin_surface_rect)
        screen.blit(self.coin11_surface, self.coin11_rect)
        screen.blit(self.double_coin_surface, self.double_coin_surface_rect)
        screen.blit(self.speedup, self.speedup_rect)
        screen.blit(self.flag_surface, (self.flag_rect.x, 520))
        screen.blit(self.questionmark, self.questionmark_rect)
        self.animation_spell()
        screen.blit(self.spell_animation, self.spell_animation_rect)
        screen.blit(self.fire_ball_spell, self.rect_meteor)
        screen.blit(self.box5, self.rect5_box)
        screen.blit(self.box6, self.rect6_box1)
        screen.blit(self.box7, self.rect7_box2)
        screen.blit(self.box8, self.rect8_box3)
        screen.blit(self.box9, self.rect9_box4)
        self.flag_animation()
        self.coin_animation()
        self.coin_animation2()
        

        global bgX, restart_player
        if self.keys[pygame.K_RIGHT] and player_moving and self.rect_surface_image.x >= 412:
            self.box_movement()
    def animation_spell(self):
        self.list_index_spell_animations += 0.1
        if self.list_index_spell_animations > len(self.list_spell_animation):
            self.list_index_spell_animations = 0
        self.spell_animation = self.list_spell_animation[int(self.list_index_spell_animations)]

    def coinstozero(self):
        global coins
        coins = 0

    def addcoins(self):
        global coins
        coins += 10

    def box_movement(self):
        self.rect_box.x -= 6
        self.rect_box1.x -= 6
        self.rect_box2.x -= 6
        self.rect_box3.x -= 6
        self.rect_box4.x -= 6
        self.questionmark_rect.x -= 6
        self.coin_surface_rect.x -= 6
        self.coin11_rect.x -= 6
        self.double_coin_surface_rect.x -= 6
        self.speedup_rect.x -= 6
        self.flag_rect.x -= 6
        self.spell_animation_rect.x -= 6
        self.rect_meteor.x -= 6
        self.rect5_box.x -= 6
        self.rect6_box1.x -= 6
        self.rect7_box2.x -= 6
        self.rect8_box3.x -= 6
        self.rect9_box4.x -= 6
        
        if self.rect_box.left < - 200:
            self.rect_box.right = 2000
        elif self.rect_box1.left < - 100:
            self.rect_box1.right = 2500
        elif self.rect_box2.left < - 250:
            self.rect_box2.right = 3000
        elif self.rect_box3.left < - 350:
            self.rect_box3.right = 3500
        elif self.rect_box4.left < - 400:
            self.rect_box4.right = 4000
        elif self.rect5_box.left < - 200:
            self.rect5_box.right = 2000
        elif self.rect6_box1.left < - 100:
            self.rect6_box1.right = 2500
        elif self.rect7_box2.left < - 250:
            self.rect7_box2.right = 3000
        elif self.rect8_box3.left < - 250:
            self.rect8_box3.right = 3000
        elif self.rect9_box4.left < - 250:
            self.rect9_box4.right = 3000

    def coin_animation(self):
        self.coin_list_index += 0.3
        if self.coin_list_index >= len(self.coin_list_animations):
            self.coin_list_index = 0
        self.coin_surface = self.coin_list_animations[int(self.coin_list_index)]

    def coin_animation2(self):
        self.coin_list_index1 += 0.3
        if self.coin_list_index1 >= len(self.coin_list_animations1):
            self.coin_list_index1 = 0
        self.coin11_surface = self.coin_list_animations1[int(self.coin_list_index1)]

    def snail_animationn(self):
        self.index_list += 0.1
        self.index_list1 += 0.1
        self.index_list2 += 0.1
        if self.index_list >= len(self.list_snail_animations) or self.index_list1 >= len(
                self.list_snail_animations1) or self.index_list2 >= len(self.list_snail_animations2):
            self.index_list = 0
            self.index_list1 = 0
            self.index_list2 = 0
        self.animations = self.list_snail_animations[int(self.index_list)]
        self.animations1 = self.list_snail_animations1[int(self.index_list1)]
        self.animations2 = self.list_snail_animations2[int(self.index_list2)]

    def flag_animation(self):
        self.flag_index_list += 0.1
        if self.flag_index_list >= len(self.list_flag_animations):
            self.flag_index_list = 0
        self.flag_surface = self.list_flag_animations[int(self.flag_index_list)]

    def bird_animation(self):
        self.bird_index += 0.3
        self.bird_index1 += 0.3
        if self.bird_index >= len(self.bird_list_animations) or self.bird_index1 >= len(self.bird_list_animations1):
            self.bird_index = 0
            self.bird_index1 = 0
        self.bird_surf6 = self.bird_list_animations1[int(self.bird_index1)]
        self.bird_surf = self.bird_list_animations[int(self.bird_index)]

    def snail_movement(self):
        global restart_snail

        self.keys = pygame.key.get_pressed()
        self.animations_rect.x -= 6
        self.animations_rect1.x -= 6
        self.animations_rect2.x -= 6
        restart_snail += 6

        if bgX < 0 and self.keys[pygame.K_RIGHT]:
            self.animations_rect.x -= 6
            self.animations_rect1.x -= 6
            self.animations_rect2.x -= 6

        # When coin out of screen
        if self.coin_surface_rect.left < -300:
            self.coin_surface_rect.right = 10000
        if self.coin11_rect.left < -300:
            self.coin11_rect.right = 14000

        if self.animations_rect.left < -300:
            self.animations_rect.right = 7800
        if self.animations_rect1.left < -500:
            self.animations_rect1.right = 2000
        if self.animations_rect2.left < -300:
            self.animations_rect2.right = 10000

    def bird_movement(self):

        self.keys = pygame.key.get_pressed()
        self.bird_surf_rect.x -= 8
        self.bird_surf_rect2.x -= 8

        if bgX < 0 and self.keys[pygame.K_RIGHT]:
            self.bird_surf_rect.x -= 10
            self.bird_surf_rect2.x -= 10

        if self.bird_surf_rect.left < -300:
            self.bird_surf_rect.right = 6500
        if self.bird_surf_rect2.left < -300:
            self.bird_surf_rect2.right = 8900

    # def restart_snail(self):
    #     if game_active == False:
    #         self.return_positon()
    def obstacle_blit(self):
        self.player_input()
        screen.blit(self.animations, self.animations_rect)
        screen.blit(self.animations1, self.animations_rect1)
        screen.blit(self.animations2, self.animations_rect2)
        self.snail_animationn()
        self.snail_movement()
        self.bird_animation()
        screen.blit(self.bird_surf, self.bird_surf_rect)
        screen.blit(self.bird_surf6, self.bird_surf_rect2)
        self.bird_movement()

        self.animation_spell()

        self.player_frozen = pygame.image.load('images/froze.png')
        self.player_frozen = pygame.transform.scale(self.player_frozen, (128, 200))
        self.player_spells = 0


    def ice_spell(self):
        global spell, ice_spell_flag, ice_spell_flag_back
        self.keys = pygame.key.get_pressed()
        if spell:
            self.fire_spell_rect = pygame.Rect(self.rect_surface_image.x + 60, self.rect_surface_image.y + 30, 64, 64)
            self.fire_spell_rect_back = pygame.Rect(self.rect_surface_image.x - 20, self.rect_surface_image.y + 30, 64,
                                                    64)
            if self.keys[pygame.K_f]:
                ice_spell_flag = True
                spell = False
                
            if self.keys[pygame.K_g]:
                ice_spell_flag_back = True
                spell = False

    def icespelltrigger(self):
        global ice_spell_flag
        if ice_spell_flag:
            screen.blit(self.fire_spell, self.fire_spell_rect)
            self.fire_spell_rect.x += 10

    def icespelltrigger_backwards(self):
        global ice_spell_flag
        if ice_spell_flag_back:
            screen.blit(self.fire_spell, self.fire_spell_rect_back)
            self.fire_spell_rect_back.x -= 10

    def fire_spell_meteor(self):
        global spell2, fire_spell_flag, fire_spell_flag_back
        self.keys = pygame.key.get_pressed()
        if spell2:
            self.fire_spell_rect_meteor = pygame.Rect(self.rect_surface_image.x + 60, self.rect_surface_image.y + 30,
                                                      64,
                                                      64)
            self.fire_spell_rect_back_meteor = pygame.Rect(self.rect_surface_image.x - 20,
                                                           self.rect_surface_image.y + 30,
                                                           64, 64)
            if self.keys[pygame.K_f]:
                fire_spell_flag = True
                spell2 = False
                fire_effect.play()
            if self.keys[pygame.K_g]:
                fire_spell_flag_back = True
                spell2 = False
                fire_effect.play()

    def firespelltrigger(self):
        global fire_spell_flag
        if fire_spell_flag:
            screen.blit(self.fire_ball_forwards, self.fire_spell_rect_meteor)
            self.fire_spell_rect_meteor.x += 10

    def firespelltrigger_backwards(self):
        global fire_spell_flag
        if fire_spell_flag_back:
            screen.blit(self.fire_ball_backwards, self.fire_spell_rect_back_meteor)
            self.fire_spell_rect_back_meteor.x -= 10

    def box_restart(self):
        global restart_player

        self.rect_box.x += restart_player
        self.rect_box1.x += restart_player
        self.rect_box2.x += restart_player
        self.rect_box3.x += restart_player
        self.rect_box4.x += restart_player
        self.rect5_box.x += restart_player
        self.rect6_box1.x += restart_player
        self.rect7_box2.x += restart_player
        self.rect8_box3.x += restart_player
        self.rect9_box4.x += restart_player

    def freeze(self):
        global player_moving, froze, move
        if move and froze < 3:
            froze += 0.014
            player_moving = False
            screen.blit(self.player_frozen, (self.rect_surface_image.x, self.rect_surface_image.y - 55))
        if froze >= 3:
            move = False
            player_moving = True

    def coin_restart(self):
        self.coin_surface_rect.x = 1010
        self.coin11_rect.x = 2000
        self.flag_rect.x = 14000
        self.rect_box.x = 1000
        
        self.rect_box1.x = 1500
        self.rect_box2.x = 1800
        self.rect_box3.x = 2300
        self.rect_box4.x = 4000
        self.double_coin_surface_rect.x = 5500
        self.speedup_rect.x = 7500
        self.questionmark_rect.x = 6500
        self.spell_animation_rect.x = 9000
        self.fire_ball_spell_rect = 10000
        self.rect5_box.x = 1000 + random.randint(100, 220)
        self.rect6_box1.x = 1500 + random.randint(100, 220)
        self.rect7_box2.x = 1800 + random.randint(100, 220)
        self.rect8_box3.x = 2300 + random.randint(100, 220)
        self.rect9_box4.x = 4000 + random.randint(100, 220)

    def coinsadd(self):
        global coins
        coins += 1

    def coin_double(self):
        global coins
        coins = coins * 2

    def colision(self):
        global game_active, move, spell, spell2, ice_spell_flag, fire_spell_flag
        global bgX
        global coins
        global menu_active
        self.randomnum = random.randint(0, 2)

        if self.rect_surface_image.x > 0:
            if self.animations_rect.colliderect(self.rect_surface_image) or self.rect_surface_image.colliderect(
                    self.bird_surf_rect) or self.rect_surface_image.colliderect(
                self.animations_rect1) or self.rect_surface_image.colliderect(
                self.animations_rect2) or self.rect_surface_image.colliderect(self.bird_surf_rect2):
                self.rect_surface_image.x -= 12

        if self.rect_surface_image.colliderect(self.rect_box) or self.rect_surface_image.colliderect(
                self.rect_box1) or self.rect_surface_image.colliderect(
            self.rect_box2) or self.rect_surface_image.colliderect(
            self.rect_box3) or self.rect_surface_image.colliderect(self.rect_box4):
            self.rect_surface_image.top = 335
            self.player_gravity = 0
            if self.keys[pygame.K_SPACE] and player_moving:
                # if self.rect_surface_image.bottom >= 100:
                self.player_gravity = -19

                

        if self.rect_surface_image.colliderect(self.rect5_box):
            self.rect_surface_image.top = self.rect5_box.y - 115
            self.player_gravity = 0
            if self.keys[pygame.K_SPACE] and player_moving:
                # if self.rect_surface_image.bottom >= 100:
                self.player_gravity = -19
        if self.rect_surface_image.colliderect(self.rect6_box1):
            self.rect_surface_image.top = self.rect6_box1.y - 115
            self.player_gravity = 0
            if self.keys[pygame.K_SPACE] and player_moving:
                # if self.rect_surface_image.bottom >= 100:
                self.player_gravity = -19
        if self.rect_surface_image.colliderect(self.rect7_box2):
            self.rect_surface_image.top = self.rect7_box2.y - 115
            self.player_gravity = 0
            if self.keys[pygame.K_SPACE] and player_moving:
                # if self.rect_surface_image.bottom >= 100:
                self.player_gravity = -19
        if self.rect_surface_image.colliderect(self.rect8_box3):
            self.rect_surface_image.top = self.rect8_box3.y - 115
            self.player_gravity = 0
            if self.keys[pygame.K_SPACE] and player_moving:
                # if self.rect_surface_image.bottom >= 100:
                self.player_gravity = -19
        if self.rect_surface_image.colliderect(self.rect9_box4):
            self.rect_surface_image.top = self.rect9_box4.y - 115
            self.player_gravity = 0
            if self.keys[pygame.K_SPACE] and player_moving:
                # if self.rect_surface_image.bottom >= 100:
                self.player_gravity = -19


        if self.rect_surface_image.colliderect(self.coin_surface_rect):
            self.coin_surface_rect.x = 6000

            coin_effect.play()
            coins2 = Player()
            self.coinsadd()
        if self.rect_surface_image.colliderect(self.coin11_rect):
            self.coin11_rect.x = 6000
            coin_effect.play()
            coins2 = Player()
            self.coinsadd()
        if self.rect_surface_image.colliderect(self.double_coin_surface_rect):
            self.coin_double()
            self.double_coin_surface_rect.x = -5000
        if self.rect_surface_image.colliderect(self.speedup_rect):
            self.rect_surface_image.x += 20
        if self.rect_surface_image.colliderect(self.questionmark_rect) and self.randomnum == 0:
            self.addcoins()
            self.questionmark_rect.x = -2000
        if self.rect_surface_image.colliderect(self.spell_animation_rect) and spell2 == False:
            self.spell_animation_rect.x = random.randint(3000, 5000)
            spell = True

        if self.rect_surface_image.colliderect(self.questionmark_rect) and self.randomnum == 1:
            self.coinstozero()
            self.questionmark_rect.x = -2000
        if self.rect_surface_image.colliderect(self.questionmark_rect) and self.randomnum == 2:
            move = True
            ice_effect.play()
            self.questionmark_rect.x = random.randint(5000, 7000)

        if self.fire_spell_rect.colliderect(self.bird_surf_rect) and ice_spell_flag:
            self.bird_surf_rect.x = 2000
            # dodati zvuk kako zagiba
            kill_snail_effect.play()
            ice_spell_flag = False
        if self.fire_spell_rect.colliderect(self.bird_surf_rect2) and ice_spell_flag:
            self.bird_surf_rect2.x = 2000
            # dodati zvuk kako zagiba
            kill_snail_effect.play()
            ice_spell_flag = False
        if self.fire_spell_rect.colliderect(self.animations_rect) and ice_spell_flag:
            self.animations_rect.x = 2000
            # dodati zvuk kako zagiba
            kill_snail_effect.play()
            ice_spell_flag = False
        if self.fire_spell_rect.colliderect(self.animations_rect1) and ice_spell_flag:
            self.animations_rect1.x = 2000
            # dodati zvuk kako zagiba
            kill_snail_effect.play()
            ice_spell_flag = False
        if self.fire_spell_rect.colliderect(self.animations_rect2) and ice_spell_flag:
            self.animations_rect2.x = 2000
            # dodati zvuk kako zagiba
            kill_snail_effect.play()
            ice_spell_flag = False


        if self.fire_spell_rect_meteor.colliderect(self.bird_surf_rect) and fire_spell_flag:
            self.bird_surf_rect.x = 2000
            fire_spell_flag = False
            kill_snail_effect.play()
        if self.fire_spell_rect_meteor.colliderect(self.bird_surf_rect2) and fire_spell_flag:
            self.bird_surf_rect2.x = 2000
            fire_spell_flag = False
            kill_snail_effect.play()
        if self.fire_spell_rect_meteor.colliderect(self.animations_rect) and fire_spell_flag:
            self.animations_rect.x = 2000
            fire_spell_flag = False
            kill_snail_effect.play()
        if self.fire_spell_rect_meteor.colliderect(self.animations_rect1) and fire_spell_flag:
            self.animations_rect1.x = 2000
            fire_spell_flag = False
            kill_snail_effect.play()
        if self.fire_spell_rect_meteor.colliderect(self.animations_rect2) and fire_spell_flag:
            self.animations_rect2.x = 2000
            fire_spell_flag = False
            kill_snail_effect.play()



        self.text_font_for_score = pygame.font.Font('fonts/LeagueGothic-Regular.otf', 50)
        self.textcoins = self.text_font_for_score.render(f"COINS :{coins}", 1, "#072d2d")

        if self.rect_surface_image.colliderect(self.flag_rect):
            global game_active
            global menu_active
            global options_volume_on
            global options_volume_off

            options_volume_on = False
            options_volume_off = False
            menu_active = True
            game_active = False
        if self.rect_surface_image.colliderect(self.rect_meteor) and spell == False:
            spell2 = True
            self.rect_meteor.x = random.randint(3000, 5000)

            
       
    def blit_screen(self):
        self.apply_gravity()
        screen.blit(self.textcoins, (30, 30))
        if spell:
            screen.blit(self.spell_on, (-20, 585))
        if spell2:
            screen.blit(self.fire_ball_surface_spell, (-20, 585))
        else:
            screen.blit(self.spell_avaiable, (-20, 585))
        
        

    def restart(self):
        global bgX, coins
        coins = 0
        bgX = 0
        self.rect_surface_image.x = 40
        if game_active == False:
            self.coin_restart()

key_pressed = False
background = Background()
obstacles = Obstacles()
mainmenu = main_menu()
cx, cy = pygame.mouse.get_pos()

gamestarting = pygame.image.load("background/gamestarting.png")
three = pygame.image.load("background/3.png")
two = pygame.image.load("background/2.png")
one = pygame.image.load("background/1.png")
blurredimage = pygame.image.load("background/1.jpg")
gamestarting = pygame.transform.scale(gamestarting,(1280, 740))
three = pygame.transform.scale(three,(1280, 740))
two = pygame.transform.scale(two,(1280, 740))
one = pygame.transform.scale(one,(1280, 740))
unrealengine = pygame.image.load("images/Unreal-Engine-logo.jpg")
unrealengine = pygame.transform.scale(unrealengine,(1280,740)).convert_alpha()
running = True
#Main game loop¸b 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =  False
            exit()
            
    screen.fill("White")
    if menu_active and game_active == False:
        bgX_menu -= 0.5
        obstacles.restart()
        obstacles.box_restart()
        obstacles.coin_restart()
        obstacles.total_restart_timer()
        mainmenu.click()
        mainmenu.menu_background()
        mainmenu.start_text()
        mainmenu.shop_text()
        mainmenu.settings_text()
        mainmenu.exit_text()
        mainmenu.hover()
        mainmenu.friends()
        mainmenu.settings_click()
        mainmenu.shop_coming()
        mainmenu.friends_tab()
        
        
    elif map_pick:
        restart_player = 0
        mainmenu.map_pick()
        mainmenu.map_true()
        mainmenu.map_exit()
    elif friends:

        bgX_menu -= 0.5
        mainmenu.click()
        mainmenu.menu_background()
        mainmenu.start_text()
        mainmenu.shop_text()
        mainmenu.settings_text()
        mainmenu.exit_text()
        mainmenu.hover()
        mainmenu.settings_click()
        mainmenu.shop_coming()
        mainmenu.friends_popup()
        mainmenu.friends()
        mainmenu.friends_tab()
    elif options_volume_on and game_active == False:
        mainmenu.settings_mode()
        mainmenu.settings_exit()
        mainmenu.settings_volume()
    elif options_volume_off and game_active == False:
        mainmenu.settings_volume()
        mainmenu.setting_off()
        mainmenu.settings_exit()
    
    elif s < 2 and menu_active == False and map_pick == False:
        screen.blit(gamestarting, (0, 0))
        s += 0.05
    elif s > 2 and s < 4 and menu_active == False and map_pick == False:
        screen.blit(three, (0, 0))
        s += 0.05
    elif s > 4 and s < 6 and menu_active == False and map_pick == False:
        screen.blit(two, (0, 0))
        s += 0.05
    elif s > 6 and s < 8 and menu_active == False and map_pick == False:
        screen.blit(one, (0, 0))
        s += 0.05
    
    elif game_active:
        
        obstacles.colision()
        background.screen_blit()
        obstacles.blit_screen()
        background.timer()
        obstacles.obstacle_blit()

        obstacles.freeze()
        obstacles.ice_spell()
        obstacles.icespelltrigger()
        obstacles.icespelltrigger_backwards()
        obstacles.fire_spell_meteor()
        obstacles.firespelltrigger()
        obstacles.firespelltrigger_backwards()
        obstacles.obstacles_blits()
        mainmenu.esc()
        mainmenu.esc_menu()
        
        timer += 0.014

    if shop_coming_a:
        mainmenu.shop_coming_window()
        mainmenu.shop_coming_exit()
        mainmenu.buy_unavailable()
    unrealtimer += 0.02
    if unrealtimer < 3:
        screen.blit(unrealengine, (0, 0))
   
    pygame.display.update()
    clock.tick(60)



   