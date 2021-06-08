import pygame
import random
pygame.init()

# Colors
bC = (161, 145, 201)
LvCo = (169, 209, 208)
Black = (0,0,0)
White = (225, 225, 225)
Red = (200, 10, 50)
Purpurish = (181,185,255)

# Setting the Display
S_Width = 1000
S_Height = 630
Screen = pygame.display.set_mode((S_Width, S_Height))
pygame.display.set_caption("PING PONG")
pygame.display.update()

def Two_Player_Match():
    global bC
    global LvCo
    global White
    GAME_EXIT = False    
    Font = pygame.font.SysFont("Harrington", 40)
    PadWidth = 10
    PadHeight = 150
    L_Pad_X = 5
    L_Pad_Y = S_Height/3
    R_Pad_X = S_Width-15
    R_Pad_Y = S_Height/3
    Ball_X = S_Width/2
    Ball_Y = S_Height/2
    VL_Pad_Y = 0
    VR_Pad_Y = 0
    vB_X = 0
    vB_Y = 0
    FPS =100
    L = 0
    R = 0
    Lv = 1
    # Images to Load
    Canvas = pygame.image.load("bg.png")
    UpperPanel = pygame.image.load("UpperPanel.png")
    Clock = pygame.time.Clock()
    
    while not GAME_EXIT:

        # Getting the Window Ready
        Screen.blit(Canvas, (0,80))    
        PlayerL = pygame.draw.rect(Screen, White, (L_Pad_X, L_Pad_Y, PadWidth, PadHeight), 0, PadWidth//2)
        PlayerR = pygame.draw.rect(Screen, White, (R_Pad_X, R_Pad_Y, PadWidth, PadHeight), 0, PadWidth//2)
        BoundaryU = pygame.draw.rect(Screen, bC, (0, 81, S_Width, 6,), 0, 3) 
        BoundaryL = pygame.draw.rect(Screen, bC, (0, S_Height-6, S_Width, 6), 0, 3)
        Screen.blit(UpperPanel, (0,0))
        Screen.blit(Font.render(f'Score: {L}', True, Black), (180, 91))
        Screen.blit(Font.render(f'Score: {R}', True, Black), (700, 91))
        Screen.blit(pygame.font.SysFont('JustAnotherhand', 275).render(f'{Lv}', False, LvCo), (440, 200))
        pygame.draw.line(Screen, bC, (S_Width/2,81),(S_Width/2, S_Height))
        pygame.draw.circle(Screen, Red, (Ball_X, Ball_Y), 7)
        Ball_X += vB_X 
        Ball_Y += vB_Y
        pygame.display.update()
        # Setting the Player Controls
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:
                GAME_EXIT = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    vB_X = 5
                    vB_Y = 5
                elif event.key == pygame.K_ESCAPE:
                    vB_X = 0
                    vB_Y = 0
                elif event.key == pygame.K_UP:
                    VR_Pad_Y = -20
                elif event.key == pygame.K_DOWN:
                    VR_Pad_Y = 20 
                elif event.key == pygame.K_w:
                    VL_Pad_Y = -20
                elif event.key == pygame.K_s:
                    VL_Pad_Y = 20        
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    VR_Pad_Y = 0
                elif event.key == pygame.K_DOWN:
                    VR_Pad_Y = 0
                elif event.key == pygame.K_w:
                    VL_Pad_Y = 0
                elif event.key == pygame.K_s:
                    VL_Pad_Y = 0 
            # elif event.type == pygame.MOUSEBUTTONDOWN:
                
        L_Pad_Y += VL_Pad_Y
        R_Pad_Y += VR_Pad_Y
        rY = random.random()            
            
        # Setting the Boundary for Player Pads        
        if L_Pad_Y<=92:
            L_Pad_Y = 92
            VL_Pad_Y = 0
        elif L_Pad_Y>=(S_Height-PadHeight-10):
            L_Pad_Y = (S_Height-PadHeight-10)
            VL_Pad_Y = 0

        if R_Pad_Y<=92:
            R_Pad_Y = 92
            VR_Pad_Y = 0
        elif R_Pad_Y>=(S_Height-PadHeight-10):
            R_Pad_Y = (S_Height-PadHeight-10)
            VR_Pad_Y = 0

        # Setting the Collision With Boundaries
        if Ball_Y >= (S_Height-10) or Ball_Y <= 91 :        
            vB_Y = -vB_Y

        # Setting the Ball Collision with Player Pads
        if Ball_X>=(R_Pad_X-10) and R_Pad_Y<=Ball_Y<=(R_Pad_Y+PadHeight):
            vB_X = -vB_X        
            if vB_X>-50:
                vB_X -= 0.5
            if vB_Y>0:
                vB_Y += rY
            else:
                vB_Y -= rY         
        elif Ball_X<=(L_Pad_X+20) and L_Pad_Y<=Ball_Y<=(L_Pad_Y+PadHeight):
            vB_X = -vB_X
            if vB_X<50:
                vB_X += 0.5
            if vB_Y>0:
                vB_Y += rY
            else:
                vB_Y -= rY   

        # Setting the Score for Players
        if Ball_X>S_Width:
            L += 10
            Ball_X = S_Width/2
            Ball_Y = S_Height/2
        elif Ball_X<0 :
            R += 10        
            Ball_X = S_Width/2
            Ball_Y = S_Height/2 

        # Setting the Levels on basis of ball velocity
        if 10<=vB_X<15:
            Lv = 2
        elif 15<=vB_X<20:
            Lv = 4
        elif 20<=vB_X<25:
            Lv = 5
        elif 25<=vB_X<30:
            Lv = 6
        elif 30<=vB_X<35:
            Lv = 7
        elif 35<=vB_X<40:
            Lv = 8
        elif 40<=vB_X<45:
            Lv = 9
        elif 45<=vB_X<50:
            Lv = 10     

        pygame.display.update()    
        Clock.tick(FPS)




def Computer_Match():
    global bC
    global LvCo
    global White
    GAME_EXIT = False    
    Font = pygame.font.SysFont("Harrington", 40)
    PadWidth = 10
    PadHeight = 150
    L_Pad_X = 5
    L_Pad_Y = S_Height/3
    R_Pad_X = S_Width-15
    R_Pad_Y = S_Height/3
    Ball_X = S_Width/2
    Ball_Y = S_Height/2
    VL_Pad_Y = 15
    VR_Pad_Y = 0
    vB_X = 0
    vB_Y = 0
    CvB_X = 15
    CvB_Y = 15
    FPS =60
    L = 0
    R = 0
    Lv = 1
    # Images to Load
    Canvas = pygame.image.load("bg.png")
    UpperPanel = pygame.image.load("UpperPanel.png")
    Clock = pygame.time.Clock()
    
    while not GAME_EXIT:

        # Getting the Window Ready
        Screen.blit(Canvas, (0,80))    
        PlayerL = pygame.draw.rect(Screen, White, (L_Pad_X, L_Pad_Y, PadWidth, PadHeight), 0, PadWidth//2)
        PlayerR = pygame.draw.rect(Screen, White, (R_Pad_X, R_Pad_Y, PadWidth, PadHeight), 0, PadWidth//2)
        BoundaryU = pygame.draw.rect(Screen, bC, (0, 81, S_Width, 6,), 0, 3) 
        BoundaryL = pygame.draw.rect(Screen, bC, (0, S_Height-6, S_Width, 6), 0, 3)
        Screen.blit(UpperPanel, (0,0))
        Screen.blit(Font.render(f'Score: {L}', True, Black), (180, 91))
        Screen.blit(Font.render(f'Score: {R}', True, Black), (700, 91))
        Screen.blit(pygame.font.SysFont('comicsans', 275).render(f'{Lv}', False, LvCo), (440, 200))
        pygame.draw.line(Screen, bC, (S_Width/2,81),(S_Width/2, S_Height))
        pygame.draw.circle(Screen, Red, (Ball_X, Ball_Y), 7)
        Ball_X += vB_X 
        Ball_Y += vB_Y
        
        pygame.display.update()
        # Setting the Player Controls
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:
                GAME_EXIT = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    vB_X = CvB_X
                    vB_Y = CvB_Y
                elif event.key == pygame.K_ESCAPE:
                    vB_X = CvB_X
                    vB_Y = CvB_Y
                elif event.key == pygame.K_UP:
                    VR_Pad_Y = -20
                elif event.key == pygame.K_DOWN:
                    VR_Pad_Y = 20        
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    VR_Pad_Y = 0
                elif event.key == pygame.K_DOWN:
                    VR_Pad_Y = 0
            # elif event.type == pygame.MOUSEBUTTONDOWN:
        R_Pad_Y += VR_Pad_Y
        rY = random.random()            
            
        # Setting the Boundary for Player Pads        
        if L_Pad_Y<=92:
            L_Pad_Y = 92
            VL_Pad_Y = -VL_Pad_Y
        elif L_Pad_Y>=(S_Height-PadHeight-10):
            L_Pad_Y = (S_Height-PadHeight-10)
            VL_Pad_Y = -VL_Pad_Y

        if R_Pad_Y<=92:
            R_Pad_Y = 92
            VR_Pad_Y = 0
        elif R_Pad_Y>=(S_Height-PadHeight-10):
            R_Pad_Y = (S_Height-PadHeight-10)
            VR_Pad_Y = 0

        # Setting the Collision With Boundaries
        if Ball_Y >= (S_Height-15) or Ball_Y <= 95 :        
            vB_Y = -vB_Y

        # Setting the Ball Collision with Player Pads
        if Ball_X>=(R_Pad_X-10) and R_Pad_Y<=Ball_Y<=(R_Pad_Y+PadHeight):
            vB_X = -vB_X        
            if vB_X>-50:
                vB_X -= 0.5
            if vB_Y>0:
                vB_Y += rY
            else:
                vB_Y -= rY         
        elif Ball_X<=(L_Pad_X+20) and L_Pad_Y<=Ball_Y<=(L_Pad_Y+PadHeight):
            vB_X = -vB_X
            if vB_X<50:
                vB_X += 0.5
            if vB_Y>0:
                vB_Y += rY
            else:
                vB_Y -= rY   

        # Setting the Score for Players
        if Ball_X>S_Width:
            L += 10
            Ball_X = S_Width/2
            Ball_Y = S_Height/2
            
        elif Ball_X<0 :
            R += 10        
            Ball_X = S_Width/2
            Ball_Y = S_Height/2 
        # Setting the Levels on basis of ball velocity
        if 10<=vB_X<15:
            Lv = 2
        elif 15<=vB_X<20:
            Lv = 3
        elif 20<=vB_X<25:
            Lv = 4
        elif 25<=vB_X<30:
            Lv = 5
        elif 30<=vB_X<35:
            Lv = 6
        elif 35<=vB_X<40:
            Lv = 7
        elif 40<=vB_X<45:
            Lv = 8
        elif 45<=vB_X<50:
            Lv = 9     
        # Automating L_Pad_Y:
        if Ball_X<S_Width/2 and vB_X<0:
            L_Pad_Y = Ball_Y-PadHeight/2
            if Ball_Y < 92+PadHeight/2:
                L_Pad_Y = 92
            elif Ball_Y > S_Height-PadHeight/2:
                L_Pad_Y = (S_Height-PadHeight)
        else:
            L_Pad_Y += VL_Pad_Y*(-CvB_Y/CvB_Y)

        pygame.display.update()    
        Clock.tick(FPS)

def HomeScreen():
    global bC
    global LvCo
    global White
    global Black
    gameSelect = False    
    Font = pygame.font.SysFont("Harrington", 40)
    PadWidth = 10
    PadHeight = 150
    L_Pad_X = 5
    L_Pad_Y = S_Height/2
    R_Pad_X = S_Width-15
    R_Pad_Y = S_Height/3
    Ball_X = S_Width/2
    Ball_Y = S_Height/2
    VL_Pad_Y = 20
    VR_Pad_Y = 20
    vB_X = 18
    vB_Y = 18
    FPS =100
    L = 280
    R = 350
    Lv = 7
    # Images to Load
    Canvas = pygame.image.load("bg.png")
    UpperPanel = pygame.image.load("UpperPanel.png")
    Clock = pygame.time.Clock()
    
    while not gameSelect:

        # Getting the Window Ready
        Screen.blit(Canvas, (0,80))    
        PlayerL = pygame.draw.rect(Screen, White, (L_Pad_X, L_Pad_Y, PadWidth, PadHeight), 0, PadWidth//2)
        PlayerR = pygame.draw.rect(Screen, White, (R_Pad_X, R_Pad_Y, PadWidth, PadHeight), 0, PadWidth//2)
        BoundaryU = pygame.draw.rect(Screen, bC, (0, 81, S_Width, 6,), 0, 3) 
        BoundaryL = pygame.draw.rect(Screen, bC, (0, S_Height-6, S_Width, 6), 0, 3)
        Screen.blit(UpperPanel, (0,0))
        Screen.blit(Font.render(f'Score: {L}', True, Black), (180, 91))
        Screen.blit(Font.render(f'Score: {R}', True, Black), (700, 91))
        Screen.blit(pygame.font.SysFont('comicsans', 275).render(f'{Lv}', False, LvCo), (440, 200))
        pygame.draw.line(Screen, bC, (S_Width/2,81),(S_Width/2, S_Height))
        pygame.draw.circle(Screen, Red, (Ball_X, Ball_Y), 7)
        Ball_X += vB_X 
        Ball_Y += vB_Y
        MousePos = pygame.mouse.get_pos()
        pygame.draw.rect(Screen, Black, (350, 2*S_Height/5, 300, 60), 0, 5)
        pygame.draw.rect(Screen, Purpurish, (353, (2*S_Height/5)+3, 293, 53), 0, 5)
        Screen.blit(Font.render("Computer Match", True, Black), (358, (2*S_Height/5)+5))

        pygame.draw.rect(Screen, Black, (335, 2*S_Height/5+70, 335, 60), 0, 5)
        pygame.draw.rect(Screen, Purpurish, (338, (2*S_Height/5)+73, 328, 53), 0, 5)
        Screen.blit(Font.render("Two Player Match", True, Black), (346, (2*S_Height/5)+75))
        if 353<MousePos[0]<646 and ((2*S_Height/5)+3)<MousePos[1]<((2*S_Height/5)+56):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif 338<MousePos[0]<666 and ((2*S_Height/5)+73)<MousePos[1]<((2*S_Height/5)+126):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        pygame.display.update()
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:
                gameSelect = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                if 353<MousePos[0]<646 and ((2*S_Height/5)+3)<MousePos[1]<((2*S_Height/5)+56):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    Computer_Match()
                elif 338<MousePos[0]<666 and ((2*S_Height/5)+73)<MousePos[1]<((2*S_Height/5)+126):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    Two_Player_Match() 
        
        # Automating L_Pad_Y:
        if Ball_X<S_Width/2 and vB_X<0:
            L_Pad_Y = Ball_Y-PadHeight/2
            if Ball_Y < 92+PadHeight/2:
                VL_Pad_Y = -VL_Pad_Y
            elif Ball_Y > S_Height-PadHeight/2:
                VL_Pad_Y = -VL_Pad_Y
        else:
            L_Pad_Y += VL_Pad_Y
        # Automating R_Pad_Y:
        if Ball_X>S_Width/2 and vB_X>0:
            R_Pad_Y = Ball_Y-PadHeight/2
            if Ball_Y < 92+PadHeight/2:
                VR_Pad_Y = -VR_Pad_Y
            elif Ball_Y > S_Height-PadHeight/2:
                VR_Pad_Y = -VR_Pad_Y
        else:
            R_Pad_Y += VR_Pad_Y
        # Collision with Player Pad
        if Ball_X>=(R_Pad_X-10) and R_Pad_Y<=Ball_Y<=(R_Pad_Y+PadHeight):
            vB_X = -vB_X        
        
        elif Ball_X<=(L_Pad_X+20) and L_Pad_Y<=Ball_Y<=(L_Pad_Y+PadHeight):
            vB_X = -vB_X   
        # Setting the Boundary for Player Pads        
        if L_Pad_Y<=92:
            L_Pad_Y = 92
            VL_Pad_Y = -VL_Pad_Y
        elif L_Pad_Y>=(S_Height-PadHeight-10):
            L_Pad_Y = (S_Height-PadHeight-10)
            VL_Pad_Y = -VL_Pad_Y

        if R_Pad_Y<=92:
            R_Pad_Y = 92
            VR_Pad_Y = -VR_Pad_Y
        elif R_Pad_Y>=(S_Height-PadHeight-10):
            R_Pad_Y = (S_Height-PadHeight-10)
            VR_Pad_Y = -VR_Pad_Y
        # Setting the Collision With Boundaries
        if Ball_Y >= (S_Height-15) or Ball_Y <= 95 :        
            vB_Y = -vB_Y
        if Ball_X<0 or Ball_X>S_Width:
            Ball_X = S_Width/2
            Ball_Y = S_Height/2

        pygame.display.update()    
        Clock.tick(FPS)

HomeScreen()