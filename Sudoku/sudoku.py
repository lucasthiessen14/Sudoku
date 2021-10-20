
#Importing Libraries required for Game
import pygame
import sys
from puzzle_solver import solution
from boards import easy_board, medium_board, hard_board

#Initializers for pygame and mixer libraries
pygame.init()

#Visuals for game window
icon = pygame.image.load(".\\assets\\logo.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Soduko")
background = pygame.image.load(".\\assets\\backround.jpg")
background2 = pygame.image.load(".\\assets\\won.png")
pic = pygame.image.load(".\\assets\\intro.jpg")
pic1 = pygame.image.load(".\\assets\\introb.jpg")



#Sets the size of the game window
length = 540
height = 600
screen = pygame.display.set_mode((length,height))

#Sets colours
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)

#Sets the different fonts
myFont = pygame.font.SysFont("Comic Sans MS",35)
myFont2 = pygame.font.SysFont("Comic Sans MS",60)
myFont3 = pygame.font.SysFont("Comic Sans MS",15)

def game_intro():
    intro = True
    select = 0
    while game_intro:

        #Creates the backround for the intro screen
        screen.fill((161,30,255))
        screen.blit(pic1, (0,0))
        screen.blit(pic, (150,130))
        title = myFont2.render("Sudoku", 1, (white))
        botton1 = myFont.render("Start", 1, (black))
        screen.blit(title, (170, 25))
        pygame.draw.rect(screen, (130,128,128), (175, 450, 200, 50))
        screen.blit(botton1, (230, 450))

        #Keeps track of the mouse and if it is clicked
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()


        for event in pygame.event.get():

            #Exits the game when the game window is closed
            if event.type == pygame.QUIT:
                sys.exit()

            #Keeps track of the keys that are clicked
            if event.type == pygame.KEYDOWN:
                s = select
                if event.key == pygame.K_RIGHT:
                    if select < 2:
                        s += 1

                if event.key == pygame.K_LEFT:
                    if select > 0:
                        s -= 1
                select = s

        #Changes the colour of the difficulty level selected
        if select == 1:
            diff1 = myFont3.render("Easy", 1, (black))
            diff2 = myFont3.render("Medium", 1, (red))
            diff3 = myFont3.render("Hard", 1, (black))
        elif select == 2:
            diff1 = myFont3.render("Easy", 1, (black))
            diff2 = myFont3.render("Medium", 1, (black))
            diff3 = myFont3.render("Hard", 1, (red))
        else:
            diff1 = myFont3.render("Easy", 1, (red))
            diff2 = myFont3.render("Medium", 1, (black))
            diff3 = myFont3.render("Hard", 1, (black))

        #Starts game with the appropriate Sudoku board when start is clicked
        if 175+200 > mouse[0] > 175 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(screen, (red), (175, 450, 200, 50), 2)
            if clicked[0] == 1:
                if select == 0:
                    grid = easy_board
                elif select == 1:
                    grid = medium_board
                elif select == 2:
                    grid = hard_board
                gameloop(grid)
        else:
            pygame.draw.rect(screen, (black), (175, 450, 200, 50), 2)

        screen.blit(diff1, (180, 500))
        screen.blit(diff2, (250, 500))
        screen.blit(diff3, (335, 500))

        pygame.display.update()

def game_end():
    end = True

    while end:

        #Creates the backround for the end screen
        screen.fill(black)
        screen.blit(background2, (150,100))
        text1 = myFont.render("Press Spacebar to", 1, (white))
        text2 = myFont.render("Return to Main Menu", 1, (white))
        screen.blit(text1, (125, 450))
        screen.blit(text2, (100, 500))
        pygame.display.update()

        for event in pygame.event.get():

            #Exits the game when the game window is closed
            if event.type == pygame.QUIT:
                sys.exit()

            #Goes back to the main menu when spacebar is clicked
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_intro()

def draw_grid():
    for i in range(0,81):
        pos = pos_list[i]
        pos1 = positions[i]
        val = num_list[i]
        if val == 0:
            val = " "
        if pos1 in zero_list:
            if pos == [select_pos[0]+15, select_pos[1]]:
                if keys != 0:
                    num_list[i] = keys
        if pos1 in zero_list:
            text_color3 = (blue)
        else:
            text_color3 = black
        val = str(val)
        dnum = myFont.render(val, 1, text_color3)
        screen.blit(dnum, (pos))

def gameloop(grid):

    grid1 = grid
    game_over = False
    select_pos = [5, 5]
    num_list = []
    pos_list = []
    x = [20, 80, 140, 200, 260, 320, 380, 440, 500]
    y = [5, 65, 125, 185, 245, 305, 365, 425, 485]
    zero_list = []
    positions = []
    keys = 0
    play_list = []
    end = 0
    incorrect = False
    pygame.key.set_repeat(60,60)

    #draws the box selector
    def draw_border():
        pygame.draw.rect(screen, (red), (select_pos[0], select_pos[1], 50, 50), 2)

    #creates a list of all the numbers in the Sudoku board
    def num_val(board):
        for y in range(len(board)):
            for x in range(len(board[0])):
                i = board[y][x]
                if i == 0 and [y,x] not in zero_list:
                    zero_list.append([y,x])
                if [y,x] not in positions:
                    positions.append([y,x])
                if len(num_list) < 81:
                    num_list.append(i)

    #Converts the players answers into the proper format
    def player_answer():
        for x in [9,18,27,36,45,54,63,72,81]:
            y = x - 9
            i = num_list[y:x]
            if len(play_list) < 9:
                play_list.append(i)

    #Creates a list of where all the numbers should be printed on the screen
    def num_pos():
        for i in y:
            for j in x:
                pos_list.append([j, i])

    #Draws all the numbers on the screen
    def draw_grid():
        for i in range(0,81):
            pos = pos_list[i]
            pos1 = positions[i]
            val = num_list[i]
            if val == 0:
                val = " "
            if pos1 in zero_list:
                if pos == [select_pos[0]+15, select_pos[1]]:
                    if keys != 0:
                        num_list[i] = keys
            if pos1 in zero_list:
                text_color3 = (blue)
            else:
                text_color3 = black
            val = str(val)
            dnum = myFont.render(val, 1, text_color3)
            screen.blit(dnum, (pos))

    while not game_over:

        #Creates game backround
        screen.fill(black)
        screen.blit(background, (0,0))


        for event in pygame.event.get():

            #Exits the game when the game window is closed
            if event.type == pygame.QUIT:
                sys.exit()

            #Keeps track of all the keys that are clicked
            if event.type == pygame.KEYDOWN:

                a = select_pos[0]
                b = select_pos[1]

                if event.key == pygame.K_UP:
                    incorrect = False
                    if select_pos[1] > 5:
                        b -= 60
                elif event.key == pygame.K_DOWN:
                    incorrect = False
                    if select_pos[1] < 485:
                        b += 60
                elif event.key == pygame.K_RIGHT:
                    incorrect = False
                    if select_pos[0] < 485:
                        a += 60
                elif event.key == pygame.K_LEFT:
                    incorrect = False
                    if select_pos[0] > 5:
                        a -= 60

                select_pos = [a,b]
                k = keys

                if event.key == pygame.K_1:
                    incorrect = False
                    k = 1
                if event.key == pygame.K_2:
                    incorrect = False
                    k = 2
                if event.key == pygame.K_3:
                    incorrect = False
                    k = 3
                if event.key == pygame.K_4:
                    incorrect = False
                    k = 4
                if event.key == pygame.K_5:
                    incorrect = False
                    k = 5
                if event.key == pygame.K_6:
                    incorrect = False
                    k = 6
                if event.key == pygame.K_7:
                    incorrect = False
                    k = 7
                if event.key == pygame.K_8:
                    incorrect = False
                    k = 8
                if event.key == pygame.K_9:
                    incorrect = False
                    k = 9
                keys = k

                if event.key == pygame.K_a:
                    incorrect = False
                    num_list.clear()
                    solution(grid1)
                    num_val(grid1)
                    draw_grid()
                    end += 1

                if event.key == pygame.K_ESCAPE:
                    incorrect = False
                    for i in zero_list:
                        a = i[0]
                        b = i[1]
                        grid1[a][b] = 0
                    game_intro()

                elif event.key == pygame.K_RETURN:
                    player_answer()
                    solution(grid1)
                    if play_list == grid1:
                        for i in zero_list:
                            a = i[0]
                            b = i[1]
                            grid1[a][b] = 0
                        if end == 0:
                            game_end()
                        else:
                            end = 0
                            game_intro()
                    else:
                        if incorrect == True:
                            incorrect = False
                        else:
                            incorrect = True
                        play_list.clear()


        #Calls the functions created
        draw_border()
        num_val(grid1)
        num_pos()
        draw_grid()

        keys = 0
        if incorrect == True:
            text = myFont.render("Press Enter to Continue", 1, (white))
            screen.blit(text, (80, 550))
            screen.blit(myFont2.render("Try Again", 1, (red)), (120, 200))
        else:
            text = myFont.render("Press Enter to Check Answer", 1, (white))
            screen.blit(text, (40, 550))
        pygame.display.update()

#Calls the main game functions
game_intro()
gameloop()
game_end()
