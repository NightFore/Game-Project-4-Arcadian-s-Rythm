import os
import pygame
import time
import pickle           # Load/Save Game
import random
import re               # re.split()


pygame.init()
clock = pygame.time.Clock()

# Title
Project_Title = "Arcadians's Rythm"
pygame.display.set_caption(Project_Title)

# Screen
display_width   = 1280
display_height  = 720
gameDisplay = pygame.display.set_mode((display_width, display_height))

# Background
BG_Title_Screen = pygame.image.load("Data\Background\Background_Title_Screen.jpg")

# Icon
Icon_Arrow_A = pygame.image.load("Data\Icon\Icon_Arrow_A.png")
Icon_Arrow_B = pygame.image.load("Data\Icon\Icon_Arrow_B.png")
Arrow_A_Rect = Icon_Arrow_A.get_rect()
Arrow_B_Rect = Icon_Arrow_B.get_rect()

# OST
Glorious_Morning_2  = "Data\OST\Glorious_Morning_2.mp3"
Jumper              = "Data\OST\Jumper.mp3"

# Enemy
Sprite_Wolf     = pygame.image.load("Data\Sprite\Sprite_Wolf.png")
Sprite_Direwolf = pygame.image.load("Data\Sprite\Sprite_Direwolf.png")
Sprite_Ghoul    = pygame.image.load("Data\Sprite\Sprite_Ghoul.png")
Sprite_Zombie   = pygame.image.load("Data\Sprite\Sprite_Zombie.png")

# Color
Color_Red           = 255, 20,  0
Color_Green         = 60,  210, 120
Color_Blue          = 0,   160, 230
Color_Black         = 0,   0,   0
Color_Grey          = 150, 170, 210
Color_White         = 255, 255, 255

Color_Button        = 140, 205, 245
Color_Title_Screen  = 210, 100, 240

Color_Grid          = [Color_Grey, Color_Red, Color_Green, Color_Blue]



class Tools():
    def __init__(self, name):
        self.event = ""

class GameState():
    def __init__(self, name):
        self.Press = [0] * 300          # Key Press (Button)
        self.Enemy_Sprite = []
        self.Enemy_Sprite_Rect = []
GameState.Press = [0] * 300




# Game - Main Function
def Main():
    def Quit_Game():
        pygame.quit()
        quit()

    # Game - Secondary Functions
    def Title_Screen():

    # Background
        gameDisplay.blit(BG_Title_Screen, (0,0))

    # BGM
        pygame.mixer.music.load(Jumper)
        pygame.mixer.music.play(-1)
        
        gameExit = False
        while not gameExit:
            for event in pygame.event.get():
                pygame.display.update()
                Tools.event = event
                if event.type == pygame.QUIT:
                    Quit_Game()
                
                Text_Display(Project_Title, display_width/2, display_height/4, Text_Title_Screen)
                Button("Start"  , "", 0, 1*display_width/4, 3*display_height/4, display_width/8, display_height/12, Color_Green, Color_Red, Text_Button_1, Tools.event, Main_Game)
                Button("Levels",  "", 0, 2*display_width/4, 3*display_height/4, display_width/8, display_height/12, Color_Green, Color_Red, Text_Button_1, Tools.event, Levels)
                Button("Exit"   , "", 0, 3*display_width/4, 3*display_height/4, display_width/8, display_height/12, Color_Green, Color_Red, Text_Button_1, Tools.event, Quit_Game)



    def Main_Game():
    # BGM
        pygame.mixer.music.load(Glorious_Morning_2)
        pygame.mixer.music.play(-1)

    # Loading List_Enemies
        f = open("List_Enemies.txt", "r")
        List_Enemies = re.split('; |, |\*|\n',f.read())
        List_Enemies = [List_Enemies[x:x+4] for x in range(0, len(List_Enemies),4)]     # List every 4 Parameters



    # Total Enemy_Count
        global Enemy_Count, Enemy_Sprite, Enemy_Sprite_Rect, Enemy_X
        Enemy_Count = len(List_Enemies)
        
        Enemy_Sprite        = [0] * Enemy_Count     # List Enemy_Sprite
        Enemy_Sprite_Rect   = [0] * Enemy_Count     # List Enemy_Sprite_Rect
        Arrow_Position      = [0] * Enemy_Count     # List Arrow
        Enemy_X             = [0] * Enemy_Count     # List Position X
        Enemy_Y             = [0] * Enemy_Count     # List Position Y
        Enemy_Speed         = [0] * Enemy_Count     # List Speed



    # Starting Parameters
        n = 0
        for Parameters in List_Enemies:
            # Enemy_Sprite
            Enemy_Sprite[n]         = globals()[List_Enemies[n][0]]
            Enemy_Sprite_Rect[n]    = Enemy_Sprite[n].get_rect()

            # Starting Position
            Enemy_X[n]      = int(Parameters[1])    # Position X
            Enemy_Y[n]      = int(Parameters[2])    # Position Y
            Enemy_Speed[n]  = int(Parameters[3])    # Enemy Speed
            n = n + 1



    # Main Game
        gameExit = False
        while not gameExit:
            for event in pygame.event.get():
                pygame.display.update()
                Tools.event = event
                if event.type == pygame.QUIT:
                    Quit_Game()
                    
        # Background
            gameDisplay.fill(Color_Blue)

        # Grid
            # 1280 / 160 = 8
            # (720 - (24*3) - (4*2)) / 160 = 4
            Grid_Draw(8,4, +24, 4,4,160,160, "Standard")


        # Buttons
            # 80 + 2 + 160*col
            # 80 + 4 + (160+3)*row
            Button_Key("X", pygame.K_x, "", 0, 240+2, 80+4,   160-4, 160, Color_Green, Color_Red, Text_Button_2, Tools.event, Tap_Square)
            Button_Key("C", pygame.K_c, "", 0, 240+2, 240+28, 160-4, 160, Color_Green, Color_Red, Text_Button_2, Tools.event, Tap_Square)
            Button_Key("V", pygame.K_v, "", 0, 240+2, 400+52, 160-4, 160, Color_Green, Color_Red, Text_Button_2, Tools.event, Tap_Square)
            Button_Key("B", pygame.K_b, "", 0, 240+2, 560+76, 160-4, 160, Color_Green, Color_Red, Text_Button_2, Tools.event, Tap_Square)


        # Sprite Position
            for n in range(Enemy_Count):
            # Arrow - Position
                Arrow_A_Rect.center = (Enemy_X[n], Enemy_Y[n]+90)           # Centering Arrow Position
                gameDisplay.blit(Icon_Arrow_A, Arrow_A_Rect)                # Displaying Arrow
            
            # Enemy - Position
                Enemy_Sprite_Rect[n].center = (Enemy_X[n], Enemy_Y[n])      # Centering Enemy Position
                gameDisplay.blit(Enemy_Sprite[n], Enemy_Sprite_Rect[n])     # Displaying Enemy

            # Enemy - Movement
                Enemy_X[n] += Enemy_Speed[n]
                if Enemy_X[n] <= 80 :
                    Enemy_X[n] = 1180


            pygame.display.update()
            clock.tick(60)




    def Levels():
        pass



    def Tap_Square(Box):
        # Checking Enemy Position
        for n in range(Enemy_Count):
            if pygame.Rect.colliderect(Enemy_Sprite_Rect[n], Box):
                Enemy_X[n] = 1200


        
    Title_Screen()


# Text - Main Function
def Text_Display(msg, x, y, Text_Font):
    textSurf, textRect = Text_Font(msg)
    textRect.center = (x, y)
    gameDisplay.blit(textSurf, textRect)

# Text - Secondary Functions
def Text_Title_Screen(msg):
    font = pygame.font.SysFont(None, 100)
    textSurface = font.render(msg, True, Color_Title_Screen)
    return textSurface, textSurface.get_rect()

def Text_Button_1(msg):
    font = pygame.font.SysFont(None, 40)
    textSurface = font.render(msg, True, Color_Blue)
    return textSurface, textSurface.get_rect()


def Text_Button_2(msg):
    font = pygame.font.SysFont(None, 100)
    textSurface = font.render(msg, True, Color_Blue)
    return textSurface, textSurface.get_rect()


# Tools
def Grid_Draw(Row,Col,Gap, x,y,w,h,Color):
    Grid = [[0]*Row for n in range(Col)]
    x0 = x
    
    for row in Grid:
        for col in row:
            Rectangle = (x,y,w,h)
            # Border
            pygame.draw.rect(gameDisplay, Color_Black, Rectangle, 10)

            # Fill
            Grid_Color(Grid, Rectangle, col, Color)

            # Position
            x = x+w
        y = y+h+Gap     # Gap = Space between row
        x = x0          # Rectification



def Grid_Color(Grid, Rectangle, col, Color):
    if Color == "":
        pygame.draw.rect(gameDisplay, Color_Black, Rectangle)
        
    if Color == "Standard":
##        Grid[5][2] = 1
##        Grid[5][3] = 2
##        Grid[5][4] = 3
        
        for i in range(4):
            if col == i:
                pygame.draw.rect(gameDisplay, Color_Grid[i], Rectangle)
        


def Button(msg, Selection, width, x,y,w,h, ac,ic, Text_Font, event, action=None):
    # msg       = Message insde Button
    # Selection = Button Number (Multiple)
    # width     = Border witdh
    # x,y,w,h   = Position
    # ac/ic     = Active/Inactive Color
    Xb = x-(w/2)    # Center X (Box)
    Yb = y-(h/2)    # Center Y (Box)
    Xm = Xb+(w/2)   # Center X (Message)
    Ym = Yb+(h/2)   # Center Y (Message)
    
    Box = pygame.Rect(Xb,Yb,w,h)
    mouse = pygame.mouse.get_pos()

    pygame.draw.rect(gameDisplay, Color_Black, Box, 15)
    
    # Active Color
    if Box.collidepoint(mouse):
        pygame.draw.rect(gameDisplay, ac, Box, width)
        # Action
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if action != None:
                    if Selection != "":
                        action(Selection)
                    else:
                        action()

    # Inactive Color
    else:
        pygame.draw.rect(gameDisplay, ic, Box, width)

    # Button Message
    textSurf, textRect = Text_Font(msg)

    # Button Rect
    textRect.center = Xm, Ym
    gameDisplay.blit(textSurf, textRect)
        


def Button_Key(msg, Key_Pressed, Selection, width, x,y,w,h, ac,ic, Text_Font, event, action=None):
    # msg       = Message insde Button
    # Selection = Button Number (Multiple)
    # width     = Border witdh
    # x,y,w,h   = Position
    # ac/ic     = Active/Inactive Color
    Xb = x-(w/2)    # Center X (Box)
    Yb = y-(h/2)    # Center Y (Box)
    Xm = Xb+(w/2)   # Center X (Message)
    Ym = Yb+(h/2)   # Center Y (Message)
    
    Box = pygame.Rect(Xb,Yb,w,h)
    mouse = pygame.mouse.get_pos()

    # Key
    if event.type == pygame.KEYDOWN:
        if event.key == Key_Pressed:
            for n in range(len(GameState.Press)):
                GameState.Press[n] = False
                GameState.Press[Key_Pressed] = True
                if action != None:
                    action(Box)
            

    if event.type == pygame.KEYUP:
        if event.key == Key_Pressed:
            GameState.Press[Key_Pressed] = False

    # Inactive Color
    pygame.draw.rect(gameDisplay, ic, Box, width)
                
    # Active Color
    if GameState.Press[Key_Pressed] == True:
        if event.type == pygame.KEYDOWN:
            pygame.draw.rect(gameDisplay, ac, Box, width)

    # Button Message
    textSurf, textRect = Text_Font(msg)

    # Button Rect
    textRect.center = Xm, Ym
    gameDisplay.blit(textSurf, textRect)



Main()
