#**************************************************************************************************************
#                                                                                                             
#                                                                                                  
#                                                                                                                                    
#                                                                          
#                                               
#                                                                                                            
#                                                                                                             
#**************************************************************************************************************

from ImportingPictures import *

win = pygame.display.set_mode((1000,700))

pygame.display.set_caption("Adventures of Chum")

clock = pygame.time.Clock()
#creates clock

music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
#sets backround music and puts it on a loop

effect = pygame.mixer.Sound('star_sound.wav')
effect2 = pygame.mixer.Sound('zombie_sound.wav')
#sound effects

font = pygame.font.SysFont('timesnewroman', 100 , True)
font2 = pygame.font.SysFont('timesnewroman', 75 , True)
font3 = pygame.font.SysFont('timesnewroman', 40 , True)
font4 = pygame.font.SysFont('timesnewroman', 30 , True)
font5 = pygame.font.SysFont('timesnewroman', 170, True)
#creates font and size for letters and numbers (color and position later on)

startscreen = True
directionsscreen = False
deathscreen = False
winscreen = False
#booleans for telling what screen player is looking at

up = True
down = False
#booleans for up and down keys while on screens (not for man movement)

walking = False
falling = False
lives = 3

count = 0
#used to make pressing ENTER easier(default count = 0)

i = 0
#for falling

level1 = False
level2 = False
level3 = False
level4 = False
level5 = False
#booleans for determining what level player is on (need to add boolean if level add)


#********************************************************* PLAYER CLASS ***************************************************            

class Player(object):

    def __init__(self,x,y,width,height):

        self.x = x
        self.y = y
        self.originaly = y
        #sets the y coordiante of man on ground
        self.width = width
        self.height = height
        self.vel = 0
        self.originalvel = 10
        self.isRun = False
        self.isJump = False
        #boolean to determine if man is jumping (Not True if man is falling)
        self.left = False
        self.right = True
        self.walkCount = 0
        self.jumpCount = 10
        #integer used to determine jumping height (10 is default jumpcount)
        self.fallCount = 2
        self.standing = True
        self.isOnPlatform = True
        #used to determine if man is on a platform or on the ground
        self.hitbox = pygame.Rect(self.x, self.y, 150, 137)
        #hitbox unadjusted
        self.feetbox = pygame.Rect(self.x, self.y, 150, 137)
        #feet box unadjusted
        self.dead = False
        self.dying = False
        #boolean to determine if man can move or be affected by anything (no if True yes if False)

    
    def draw_man(self, win):

        if self.walkCount >= 15 and not deathscreen:

            self.walkCount = 0

        if self.walkCount >= 15 and deathscreen:

            self.walkCount = 14
        #keeps man in dead animation until player chooses option in death screen

        if not(self.standing):

            if not self.isJump and not self.isRun and not falling:

                if self.left:
                    #if man is walking left
                    
                    win.blit(walk_left[self.walkCount], (self.x - 85, self.y))
                    self.walkCount += 1                  #self.x - 85 because picture issues (only when facing left)

                else:
                    #if man is walking right

                    win.blit(walk_right[self.walkCount], (self.x, self.y))
                    self.walkCount += 1

            if not(self.isJump) and self.isRun and not falling:

                if self.left:
                    #if man is running left

                    win.blit(run_left[self.walkCount], (self.x - 85, self.y))
                    self.walkCount += 1

                else:
                    #if man is running right
                    
                    win.blit(run_right[self.walkCount], (self.x, self.y))
                    self.walkCount += 1

            if (self.isJump) and not falling:

                if self.left:
                    #if man is jumping left

                    win.blit(jump_left[self.walkCount], (self.x - 85, self.y))

                    if self.walkCount == 14:

                        self.walkCount == self.walkCount
                        #keeps man in jumping animation while in the air until landing
                        
                    else:

                        self.walkCount += 1

                else:
                    #if man is jumping right

                    win.blit(jump_right[self.walkCount], (self.x, self.y))

                    if self.walkCount == 14:

                        self.walkCount == self.walkCount
                        #keeps man in jumping animation while in the air until landing

                    else:

                        self.walkCount += 1
        else:

            if self.left and not man.dead and not deathscreen and not falling:
                #if man is not moving and facing left

                win.blit(idle_left[self.walkCount], (self.x - 85, self.y))
                self.walkCount += 1

            else:
                #if man is not moving and facing right

                if not man.dead and not deathscreen and not falling:

                    win.blit(idle_right[self.walkCount], (self.x, self.y))
                    self.walkCount += 1

        if falling and not self.dead:

            if self.left:
                #if man is falling left

                self.walkCount = 14
                win.blit(jump_left[self.walkCount], (self.x - 85, self.y)) 


            else:
                #if man is falling right

                self.walkCount = 14
                win.blit(jump_right[self.walkCount], (self.x, self.y))


        
        if self.dead:
            #if man loses a life

            win.blit(dead_ani[self.walkCount], (self.x, self.y))
            self.walkCount += 1
            self.dying = True
            #self.dying becomes true so man is not affected by anything during dying animation and so man can't move

            if self.walkCount == 15 and not deathscreen:

                Lose_life()
                #function that: delays game, checks how many lives man has left, and resets man to original starting position

        self.hitbox = pygame.Rect(self.x + 10, self.y + 30, 45, 95)
        #hitbox of man adjusted
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
        #draws hitbox of man

        self.feetbox = pygame.Rect(self.x + 15, self.y + 115, 35, 4)
        #feet box of man adjusted
        #pygame.draw.rect(win, (255,0,0), self.feetbox,2)
        #draws feet box of man
        #pygame.draw.rect(win, (255,0,0), ground,2)
        #draws ground

        
#******************************************************* ZOMBIE CLASS **********************************************

class Enemy(object):

    def __init__(self,x,y,width,height,x_boundry1, x_boundry2, left_boolean, right_boolean):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_boundry1 = x_boundry1
        self.x_boundry2 = x_boundry2
        self.vel = 4
        self.walkCount = 0
        self.hitbox = pygame.Rect(self.x, self.y, 150, 137)
        self.left = left_boolean
        self.right = right_boolean
        



    def draw_zombie(self, win):

        if self.walkCount >= 30 and not deathscreen:

            self.walkCount = 0

        if (man.hitbox.colliderect(self.hitbox) and self.walkCount >= 14):

            self.walkCount = 14

        if self.left and not(man.hitbox.colliderect(self.hitbox)):
                        
                win.blit(zombiewalk_left[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1 

        if self.right and not(man.hitbox.colliderect(self.hitbox)):

                win.blit(zombiewalk_right[self.walkCount // 3], (self.x + 18, self.y))
                self.walkCount += 1

        if (man.hitbox.colliderect(self.hitbox)):

            if self.left:

                win.blit(zombieattack_left[self.walkCount // 2], (self.x, self.y))
                self.walkCount += 1

            if self.right:

                win.blit(zombieattack_right[self.walkCount // 2], (self.x, self.y))
                self.walkCount += 1

        self.hitbox = pygame.Rect(self.x + 40, self.y + 28, 52, 100)
        #hitbox of zombie adjusted
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
        #draws hitbox of zombie

#******************************************************** SPIKE CLASS *******************************************************        

class Spike(object):

    def __init__(self,x,y,width,height):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, 32, 32)
        #hitbox of spike unadjusted

    def draw_spike(self, win):

        win.blit(spikes, (self.x, self.y))
        self.hitbox = pygame.Rect(self.x + 5, self.y + 6, 23, 25)
        #hitbox of spike adjusted
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
        #draws hitbox of spike

#********************************************************* STAR CLASS *********************************************************

class Star(object):

    def __init__(self,x,y,width,height):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, 64, 64)
        #star hitbox unadjusted

    def draw_star(self, win):

        win.blit(stars, (self.x, self.y))
        self.hitbox = pygame.Rect(self.x + 4, self.y + 5, 55, 55)
        #star hitbox adjusted
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
        #draws star hitbox

#********************************************************* LOG CLASS **********************************************************
#Object is True if it is a log and False if it is a platform
        
class Log(object):

    def __init__(self,x,y,width,height,log):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.log = log
        self.hitbox = pygame.Rect(self.x, self.y, 64, 64)
        #log hitbox unadjusted

    def draw_log(self, win):

        if self.log:
            win.blit(logs, (self.x, self.y))
            self.hitbox = pygame.Rect(self.x, self.y + 20, 64, 30)
            #log hitbox adjusted
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
            #draws log hitbox
        else:
            win.blit(platform, (self.x, self.y))
            self.hitbox = pygame.Rect(self.x + 10, self.y + 32, 172, 40)
            #log hitbox adjusted
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
            #draws log hitbox

#******************************************************** LEVEL FUNCTIONS ******************************************************

# For every level, that levels function is where the objects are made and drawn on the screen only if player is on that level
# In order to make new level, must make function and boolean, also must add function to redrawGameWindow(), also must add to star mechanics
# To add object in level, 1.add to object_list  2. if log add to log_hitbox_list   3. must create object down below in the lists
# Functions iterate once a frame if player is on that level

def level_1(): # Level 1
    
    if level1:

        global spike_list
        spike_list = [spike1, spike2, spike3, spike4, spike5]
        #choose which spikes you want in level from number of spikes(below), put them in spike_list

        for spike in spike_list:
            spike.draw_spike(win)
        #draws all the spikes in spike_list

        global star_list
        star_list = [star1]
        #choose which star you want in level from number of stars(should only be one), put them in star_list

        for star in star_list:
            star.draw_star(win)
        #draws star in star_list
        
        global log_list
        log_list = [log1, log2, log3, log4, log5, log6, log7]
        #choose which logs you want from number of logs(below), put them in log_list]

        global log_hitbox_list
        log_hitbox_list = [log1.hitbox, log2.hitbox, log3.hitbox, log4.hitbox, log5.hitbox, log6.hitbox, log7.hitbox]

        for log in log_list:
            log.draw_log(win)
        #draws logs in log_list

        global zombie_list
        zombie_list = [zombie1]

        for zombie in zombie_list:
            zombie.draw_zombie(win)
        

def level_2(): # Level 2

    if level2:

        global spike_list
        spike_list = [spike7, spike8, spike9, spike10]

        for spike in spike_list:
            spike.draw_spike(win)

        global star_list
        star_list = [star2]

        for star in star_list:
            star.draw_star(win)
        
        global log_list
        log_list = [log8, log9, log10, log11, log12, log13, log14]

        global log_hitbox_list
        log_hitbox_list = [log8.hitbox, log9.hitbox, log10.hitbox, log11.hitbox, log12.hitbox, log13.hitbox, log14.hitbox]

        for log in log_list:
            log.draw_log(win)

        global zombie_list
        zombie_list = [zombie2, zombie3]

        for zombie in zombie_list:
            zombie.draw_zombie(win)


def level_3(): # Level 3

    if level3:

        global spike_list
        spike_list = [spike11, spike12, spike13, spike14, spike15, spike16, spike17, spike18, spike19, spike20]

        for spike in spike_list:
            spike.draw_spike(win)

        global star_list
        star_list = [star3]

        for star in star_list:
            star.draw_star(win)
        
        global log_list
        log_list = [log15, log16, log17, log18, log19, log20, log21, log22, log23]

        global log_hitbox_list
        log_hitbox_list = [log15.hitbox, log16.hitbox, log17.hitbox, log18.hitbox, log19.hitbox, log20.hitbox, log21.hitbox, log22.hitbox, log23.hitbox]

        for log in log_list:
            log.draw_log(win)

        global zombie_list
        zombie_list = [zombie4, zombie5]

        for zombie in zombie_list:
            zombie.draw_zombie(win)
        
def level_4(): # Level 4

    if level4:

        global spike_list
        spike_list = [spike21, spike22, spike23, spike24, spike25, spike26, spike27]

        for spike in spike_list:
            spike.draw_spike(win)

        global star_list
        star_list = [star4]

        for star in star_list:
            star.draw_star(win)
        
        global log_list
        log_list = [log24, log25, log26, log27, log28, log29, log30, log31, log32, log33, log34, log35, log36]

        global log_hitbox_list
        log_hitbox_list = [log24.hitbox, log25.hitbox, log26.hitbox, log27.hitbox, log28.hitbox, log29.hitbox, log30.hitbox, log31.hitbox, log32.hitbox, log33.hitbox, log34.hitbox, log35.hitbox, log36.hitbox]

        for log in log_list:
            log.draw_log(win)

        global zombie_list
        zombie_list = [zombie6, zombie7, zombie8]

        for zombie in zombie_list:
            zombie.draw_zombie(win)

def level_5(): # Level 5

    if level5:

        global spike_list
        spike_list = [spike28, spike29, spike30, spike31, spike32, spike33]

        for spike in spike_list:
            spike.draw_spike(win)

        global star_list
        star_list = [star5]

        for star in star_list:
            star.draw_star(win)
        
        global log_list
        log_list = [log37, log38, log39, log40, log41, log42, log43, log44, log45, log46, log47, log48, log49, log50]

        global log_hitbox_list
        log_hitbox_list = [log37.hitbox, log38.hitbox, log39.hitbox, log40.hitbox, log41.hitbox, log42.hitbox, log43.hitbox, log44.hitbox, log45.hitbox, log46.hitbox, log47.hitbox, log48.hitbox, log49.hitbox, log50.hitbox]

        for log in log_list:
            log.draw_log(win)

        global zombie_list
        zombie_list = [zombie9, zombie10, zombie11, zombie12]

        for zombie in zombie_list:
            zombie.draw_zombie(win)
                        
#********************************************************* DEATH FUNCTION ********************************************************

# Function happens when man loses life

def Lose_life():

    pygame.time.delay(1000)
    #delays game creating a slight pause of 1 second

    if lives < 1:

        deathscreen = True
        #boolean becomes true which allows the function death_screen to happen

    if lives > 0:

        man.x = 480
        man.y = man.originaly
        man.dead = False
        man.dying = False
        
#*********************************************************** DEATH SCREEN *********************************************************

# Function happens when man has died and lost all of his lives
# Gives options to player of either restarting the game or quitting the game
# Restarting the game takes the player back to the start screen and gives man 3 lives
# Quitting exits the game
# man is unable to move while deathscreen is True

def Death_screen():

    if deathscreen:

        text7 = font.render('RESTART', 1, (0,0,0))
        win.blit(text7, (280, 200))
        text8 = font2.render ('QUIT', 1, (0,0,0))
        win.blit(text8, (410, 330))
        #draws RESTART and QUIT on screen

        if up and not down:

            text7 = font.render('RESTART', 1, (199,183,107))
            win.blit(text7, (280, 200))

        if down and not up:

            text8 = font2.render('QUIT', 1, (189,183,107))
            win.blit(text8, (410, 330))
        #allows player to know which option will happen when they press ENTER

        
#*********************************************************** START SCREEN **********************************************************

# Function happens when player first starts game or when man loses all lives and player chooses RESTART on death screen
# Gives player the options of starting the game or looking at directions screen
# starting the game puts man in level 1
# man is unable to move while startscreen is True


def Start_screen():

    if startscreen:

        text = font.render('START', 1, (0,0,0))
        win.blit(text, (350, 200))
        text2 = font2.render ('DIRECTIONS', 1, (0,0,0))
        win.blit(text2, (280, 300))
        #draws START and DIRECTIONS on screen

        if up and not down:

            text = font.render('START', 1, (189,183,107))
            win.blit(text, (350, 200))

        if down and not up:

            text2 = font2.render('DIRECTIONS', 1, (189,183,107))
            win.blit(text2, (280, 300))
        #allows player to know which option will happen when they press ENTER


#******************************************************** DIRECTIONS SCREEN ***********************************************************

# Function happens when player chooses DIRECTIONS from start screen
# Shows player how to move man
# man is unable to move while directionsscreen is True (maybe can change)

def Direction_screen():
    
    if directionsscreen:
        
        text3 = font3.render('← and → to walk', 1, (0,0,0))
        win.blit(text3, (350, 200))
        text4 = font3.render('Hold SHIFT to run', 1, (0,0,0))
        win.blit(text4, (350, 275))
        text5 = font3.render('↑ to jump', 1, (0,0,0))
        win.blit(text5, (350, 350))
        text6 = font3.render('BACK', 1, (189,183,107))
        win.blit(text6, (350, 425))
        #draws directions on screen

#***************************************************** WIN SCREEN *******************************************************

def Win_screen():

    if winscreen:

        text9 = font5.render('YOU WIN!', 1, (0,0,0))
        win.blit(text9, (100, 100))
        text7 = font.render('RESTART', 1, (0,0,0))
        win.blit(text7, (280, 300))
        text8 = font2.render ('QUIT', 1, (0,0,0))
        win.blit(text8, (410, 430))

        if up and not down:

            text7 = font.render('RESTART', 1, (199,183,107))
            win.blit(text7, (280, 300))

        if down and not up:

            text8 = font2.render('QUIT', 1, (189,183,107))
            win.blit(text8, (410, 430))



        
#********************************************************* LIVES COUNTER ****************************************************************

# Displays amount of current lives in top right of screen while startscreen and directionsscreen are False

def Lives_counter():
    
    if not startscreen and not directionsscreen and not winscreen:
              
        if lives == 3:

            lives_3 = font4.render('LIVES: 3', 1, (0,0,0))
            win.blit(lives_3, (720, 15))

        if lives == 2:

            lives_2 = font4.render('LIVES: 2', 1, (0,0,0))
            win.blit(lives_2, (720, 15))

        if lives == 1:

            lives_1 = font4.render('LIVES: 1', 1, (0,0,0))
            win.blit(lives_1, (720, 15))

        if lives == 0:

            lives_0 = font4.render('LIVES: 0', 1, (0,0,0))
            win.blit(lives_0, (720, 15)) 
    #draws amount of lives in top right corner


#******************************************************** DRAW GAME WINDOW **************************************************************

# Function that happens once an iteration
# Used to call all methods or functions that draw things on screen
# Draws backround, man, spikes, logs etc....
# Must call every level method even if player is not on level, booleans will determine if player is on level
# pygame.display.update() must come after everything in method
                
def redrawGameWindow():

    win.blit(bg, (0,0))
    #draws backround
    man.draw_man(win)
    #draws man
    Start_screen()
    #draws start screen if true
    Direction_screen()
    #draws directions screen if true
    Death_screen()
    #draws death screen if true
    Lives_counter()
    #draws lives counter if true
    Win_screen()
    level_1()
    level_2()
    level_3()
    level_4()
    level_5()
    #draws whatever level player is on or none if not on any level
    pygame.display.update()
    #updates screen


#******************************************************* GAME VARIABLES ***************************************************************

spike_list = []
star_list = []
log_list = []
log_hitbox_list = []
zombie_list = []


spike1 = Spike(650, 620, 30, 30)
spike2 = Spike(700, 620, 30, 30)
spike3 = Spike(820, 620, 30, 30)
spike4 = Spike(870, 620, 30, 30)
spike5 = Spike(920, 620, 30, 30)
spike6 = Spike(300, 620, 30, 30)
#
spike7 = Spike(740, 620, 30, 30)
spike8 = Spike(940, 620, 30, 30)
spike9 = Spike(430, 620, 30, 30)
spike10 = Spike(890, 530, 30, 30)
#
spike11 = Spike(600, 620, 30, 30)
spike12 = Spike(650, 620, 30, 30)
spike13 = Spike(700, 620, 30, 30)
spike14 = Spike(750, 620, 30, 30)
spike15 = Spike(800, 620, 30, 30)
spike16 = Spike(70, 420, 30, 30)
spike17 = Spike(70, 210, 30, 30)
spike18 = Spike(420, 150, 30, 30)
spike19 = Spike(550, 150, 30, 30)
spike20 = Spike(680, 150, 30, 30)
#
spike21 = Spike(10, 620, 30, 30)
spike22 = Spike(60, 620, 30, 30)
spike23 = Spike(110, 620, 30, 30)
spike24 = Spike(480, 395, 30, 30)
spike25 = Spike(600, 395, 30, 30)
spike26 = Spike(410, 395, 30, 30)
spike27 = Spike(830, 148, 30, 30)
#
spike28 = Spike(430, 620, 30, 30)
spike29 = Spike(560, 620, 30, 30)
spike30 = Spike(100, 386, 30, 30)
spike31 = Spike(880, 386, 30, 30)
spike32 = Spike(710, 130, 30, 30)
spike33 = Spike(265, 128, 30, 30)
#list of spikes to be added to level function, must create spikes here then add them to level function to draw

star1 = Star(110, 120, 64, 64)
#
star2 = Star(790, 90, 64, 64)
#
star3 = Star(885, 595, 64, 64)
#
star4 = Star(890, 105, 64, 64)
#
star5 = Star(478, 230, 64, 64)
#list of stars to be added to level function, must create star here then add it to level function to draw


log1 = Log(390, 540, 64, 64, True)
log2 = Log(600, 540, 64, 64, True)
log3 = Log(690, 465, 64, 64, True)
log4 = Log(500, 375, 64, 64, True)
log5 = Log(700, 275, 64, 64, True)
log6 = Log(475, 200, 64, 64, True)
log7 = Log(60, 300, 64, 64, False)
#
log8 = Log(750, 520, 64, 64, False)
log9 = Log(550, 450, 64, 64, True)
log10 = Log(65, 450, 64, 64, False)
log11 = Log(40, 365, 64, 64, True)
log12 = Log(250, 300, 64, 64, True)
log13 = Log(420, 200, 64, 64, False)
log14 = Log(710, 300, 64, 64, False)
#
log15 = Log(400, 550, 64, 64, True)
log16 = Log(290, 480, 64, 64, True)
log17 = Log(20, 410, 64, 64, False)
log18 = Log(290, 320, 64, 64, True)
log19 = Log(20, 200, 64, 64, False)
log20 = Log(300, 140, 64, 64, False)
log21 = Log(470, 140, 64, 64, False)
log22 = Log(640, 140, 64, 64, False)
log23 = Log(660, 340, 64, 64, False)
#
log24 = Log(780, 140, 64, 64, False)
log25 = Log(620, 550, 64, 64, True)
log26 = Log(760, 460, 64, 64, False)
log27 = Log(640, 399, 64, 64, True)
log28 = Log(458, 385, 64, 64, False)
log29 = Log(285, 385, 64, 64, False)
log30 = Log(112, 450, 64, 64, False)
log31 = Log(30, 400, 64, 64, True)
log32 = Log(0, 290, 64, 64, True)
log33 = Log(165, 190, 64, 64, True)
log34 = Log(240, 100, 64, 64, False)
log35 = Log(415, 145, 64, 64, False)
log36 = Log(635, 170, 64, 64, True)
#
log37 = Log(370, 550, 64, 64, True)
log38 = Log(590, 550, 64, 64, True)
log39 = Log(270, 480, 64, 64, True)
log40 = Log(695, 480, 64, 64, True)
log41 = Log(50, 380, 64, 64, False)
log42 = Log(20, 280, 64, 64, True)
log43 = Log(770, 380, 64, 64, False)
log44 = Log(920, 280, 64, 64, True)
log45 = Log(70, 170, 64, 64, True)
log46 = Log(190, 120, 64, 64, False)
log47 = Log(870, 170, 64, 64, True)
log48 = Log(620, 120, 64, 64, False)
log49 = Log(280, 280, 64, 64, False)
log50 = Log(540, 280, 64, 64, False)
#list of logs to be added to level function, must create logs here then add them to level function to draw


man = Player(480,525,150,137)
#the creation of man

zombie1 = Enemy(200, 518, 80, 110, 10, 250, True, False)
#
zombie2 = Enemy(200, 518, 80, 110, 10, 320, False, True)
zombie3 = Enemy(690, 210, 80, 110, 680, 810, True, False)
#
zombie4 = Enemy(10, 518, 80, 110, 10, 300, False, True)
zombie5 = Enemy(660, 245, 80, 110, 620, 760, False, True)
#
zombie6 = Enemy(910, 518, 80, 110, 660, 910, True, False)
zombie7 = Enemy(100, 357, 80, 110, 90, 180, False, True)
zombie8 = Enemy(500, 50, 80, 110, 395, 505, False, True)
#
zombie9 = Enemy(10, 518, 80, 110, 0, 260, False, True)
zombie10 = Enemy(880, 518, 80, 110, 640, 880, True, False)
zombie11 = Enemy(250, 190, 80, 110, 250, 360, False, True)
zombie12 = Enemy(630, 188, 80, 110, 520, 630, True, False)

ground = pygame.Rect(0,640,1000,70)
#creates ground

#******************************************************** MAIN LOOP *********************************************************************


run = True
#True when game is running and False when game is over

while run:

    clock.tick(30)
    #frames per second

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            run = False

    if not startscreen:
        
        if not directionsscreen:

            if not deathscreen and not winscreen:

                if not man.dead:

                    if not falling:
                    
                        #************************************************************* MOVEMENT MECHANICS *********************************

                        if not man.isRun:

                            if keys[pygame.K_LEFT] and man.x > man.vel - 11:

                                man.x -= man.originalvel
                                man.left = True
                                man.right = False
                                man.standing = False
                                walking = True
                                

                             #if man walks left           

                            elif keys[pygame.K_RIGHT] and man.x < 1075 - man.width:

                                man.x += man.originalvel
                                man.right = True
                                man.left = False
                                man.standing = False
                                walking = True
                                

                            #if man walks right

                            else:

                                man.standing = True
                                walking = False

                            #if no keys are being pressed and on a platform or the ground, man is standing

                        if keys[pygame.K_LSHIFT] and keys[pygame.K_LEFT] and man.x > - man.vel + 18:

                            man.isRun = True

                            if not man.isJump: #doesn't allow sprinting in the air

                                man.vel = man.originalvel * 1.2
                            
                            man.x -= man.vel
                            man.left = True
                            man.right = False
                            man.standing = False
                            walking = False
                            

                        #if man runs left
                        
                        elif keys[pygame.K_LSHIFT] and keys[pygame.K_RIGHT] and man.x < 1075 - man.width:

                            man.isRun = True

                            if not man.isJump: #doesn't allow sprinting in the air

                                man.vel = man.originalvel * 1.2

                            man.x += man.vel
                            man.right = True
                            man.left = False
                            man.standing = False
                            walking = False
                            

                        #if man runs right
                        #********************** for walking after running(cant delete)
                        elif not walking:

                            if keys[pygame.K_LEFT] and man.x > man.vel - 11:

                                man.x -= man.originalvel
                                man.left = True
                                man.right = False
                                man.standing = False
                                man.isRun = False
                                

                            elif keys[pygame.K_RIGHT] and man.x < 1075 - man.width:

                                man.x += man.originalvel
                                man.right = True
                                man.left = False
                                man.standing = False
                                man.isRun = False
                                

                            else:

                                man.standing = True
                                man.isRun = False                      
                        #***************************
                                
                        if not(man.isJump): #stops man from jumping while already jumping

                            if keys[pygame.K_UP]:

                                man.walkCount = 0
                                man.standing = False
                                man.isJump = True
                                man.fallCount = 10

                            #if player presses up arrow key, man.isJump becomes true

                        else:
                            
                            if man.jumpCount >= -10:

                                neg = 1

                                if man.jumpCount < 0:

                                    neg = -1
                                    #if neg = -1, man is falling from top of jump arc
                                man.y -= round((man.jumpCount ** 2) * 0.25 * neg)
                                #equation for arc of jump
                                man.jumpCount -= 1
                                man.standing = False

                            #man jumps in an arc, man.isJump is True during whole duration

                            else:

                                man.isJump = False
                                man.jumpCount = 10

                            #finishes jump

                    else:

                        if keys[pygame.K_LEFT] and man.x > man.vel - 11:

                            man.x -= man.originalvel
                            man.left = True
                            man.right = False

                            #if man moves left while falling           

                        elif keys[pygame.K_RIGHT] and man.x < 1075 - man.width:

                            man.x += man.originalvel
                            man.right = True
                            man.left = False

                            #if man moves right while fallling
                 
                
                #************************************************************** INTERACTION MECHANICS *************************************************
                
                for spike in spike_list:

                    if (man.hitbox.colliderect(spike.hitbox)):  #checks if mans hitbox is collided with any spike hitbox in spike list

                        if not man.dying and not deathscreen: #allows man to smoothly go through dying animation and be on death screen

                            lives = lives - 1
                            man.jumpCount = 10
                            man.walkCount = 0
                            man.isJump = False
                            man.dead = True
                            man.standing = True
                            man.dying = True
                            falling = False

                #mechanics for man touching spike
                
                for star in star_list:  

                    if(man.hitbox.colliderect(star.hitbox) and not man.dead):    #checks if mans hitbox is collided with star hitbox in star list

                        man.walkCount = 0
                        man.standing = True
                        falling = False
                        man.isJump = False
                        man.x = 480
                        man.y = man.originaly - 1
                        man.jumpCount = 10
                        #puts man in original spot
                        effect.play()
                        pygame.time.delay(500)

                        if level1:                                          

                            level1 = False
                            level2 = True
                            continue

                        if level2:

                            level2 = False
                            level3 = True
                            continue

                        if level3:

                            level3 = False
                            level4 = True
                            continue

                        if level4:

                            level4 = False
                            level5 = True
                            continue

                        if level5:

                            level5 = False
                            winscreen = True
                            continue

                #mechanics for touching star and switching levels



                for log in log_list:

                    if(man.feetbox.colliderect(log.hitbox) and (neg == -1 or falling)):

                        falling = False
                        man.isJump = False
                        man.jumpCount = 10
                        man.fallCount = 0
                        man.y = log.hitbox[1] - man.hitbox[3] - 23
                        man.isOnPlatform = True
                        if keys[pygame.K_UP]:
                            man.y -= 2

                if man.feetbox.colliderect(ground) == 1:

                    man.y = man.originaly
                    man.fallCount = 0
                    man.isOnPlatform = True
                    falling = False
                    if keys[pygame.K_UP]:
                            man.y -= 4 

                
                if  man.feetbox.collidelist(log_hitbox_list) == -1 and not man.feetbox.colliderect(ground) == 1:

                    man.isOnPlatform = False

                if not man.isOnPlatform and not man.isJump and not winscreen:
                    
                    man.y += 8 + man.fallCount
                    man.fallCount += 2
                    falling = True

            #********************************************************* ZOMBIE MECHANICS ********************************************

                for zombie in zombie_list:

                    if not man.dying:
                        
                        if zombie.left:

                            zombie.x -= zombie.vel
                            if zombie.x < zombie.x_boundry1:
                                zombie.left = False
                                zombie.right = True

                        if zombie.right:

                            zombie.x += zombie.vel
                            if zombie.x > zombie.x_boundry2:
                                zombie.left = True
                                zombie.right = False


                    if (man.hitbox.colliderect(zombie.hitbox)):

                        if not man.dying and not deathscreen:

                            effect2.play()
                            zombie.walkCount = 2
                            lives = lives - 1
                            man.jumpCount = 10
                            man.walkCount = 0
                            man.isJump = False
                            man.dead = True
                            man.standing = True
                            man.dying = True
                            falling = False
                            
                
        #*************************************************************** DEATH SCREEN/WIN SCREEN MECHANICS ****************************************************

            else:
            
                if keys[pygame.K_UP]:

                    up = True
                    down = False

                if keys[pygame.K_DOWN]:

                    down = True
                    up = False
                
                if up and keys[pygame.K_RETURN] and not level1: #if player presses RESTART
                    
                    startscreen = True
                    deathscreen = False
                    winscreen = False
                    lives = 3
                    man.x = 480
                    man.y = man.originaly
                    man.dead = False
                    man.dying = False
                    man.jumpCount = 10
                    man.isJump = False
                    man.isRun = False
                    falling = False
                    man.standing = True
                    count = 0
                    


                if down and keys[pygame.K_RETURN]: #if player presses QUIT

                    run = False
                    count = 0

        #****************************************************************** DIRECTIONS SCREEN MECHANICS *************************************************

        else:

            if keys[pygame.K_RETURN] and count <= 3:

                count += 1

                if count == 2:

                    startscreen = True
                    directionsscreen = False
                    count = 0          

    #********************************************************************** START SCREEN MECHANICS *****************************************************

    else:

        if keys[pygame.K_UP]:

            up = True
            down = False

        if keys[pygame.K_DOWN]:

            down = True
            up = False

        if up and keys[pygame.K_RETURN] and count <= 3:

            count += 1

            if count == 2:

                level1 = True
                level2 = False
                level3 = False
                level4 = False
                level5 = False
                startscreen = False
                count = 0

        if down and keys[pygame.K_RETURN] and count <= 3:

            count += 1

            if count == 2:

                directionsscreen = True
                startscreen = False
                count = 0

    #******************************************************************** LOSING ALL LIVES MECHANICS *******************************************************

    if lives < 1:

        deathscreen = True
        man.jumpCount = 10
        man.isJump = False
        man.isRun = False
        level1 = False
        level2 = False
        level3 = False
        level4 = False
        level5 = False
        count = 0
    

    redrawGameWindow()
    #draws everything and refreshes screen

    
pygame.quit()
#ends game

    
