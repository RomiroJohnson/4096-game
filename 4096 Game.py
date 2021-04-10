import pygame, sys
import tkinter as tk
import random
import time
import pickle
import playsound



# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('4096')  #This  is for the title of the game window
font = pygame.font.SysFont(None, 25) # These are the fonts used in the text
font1 = pygame.font.SysFont(None, 25)

screen = pygame.display.set_mode((300, 300),0,32)
jij = pygame.display.set_mode((300, 300),0,32)
a = open("highscore.txt", "r") #This is used to read the textfileand save that score as the highscore
b = (a.read())
flag =True 

textsurface = font.render('Start Game', True, (0, 0, 0))
textsurface1 = font.render('Instructions', True, (0, 0, 0))


 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():
    global click 
    while True:
 
        screen.fill((200, 200, 200))
        draw_text('4096 ', font1, (255, 255, 255), screen, 130, 50)
        
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(50, 100, 200, 50) 
        
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        screen.blit(textsurface,(100, 120, 200, 70 ))
        screen.blit(textsurface1,(100, 220, 200, 70 ))
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  #This states that if the escape key is pressed quit the program 
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:  #this means if the user clicks on the button then return click is true 
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def game():
    class Game(tk.Tk):
        pygame.quit()
        board = []
        new_tile_selection = [2,2,2,2,2,2,2,2,2,4,8]
        score = 0
        scorestring = 0
        highscorestring=b
        highscore =b
        
        
        
        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)
            self.scorestring = tk.StringVar(self)
            self.scorestring.set("0")
            self.highscorestring = b
            self.create_widgets()
            self.canvas = tk.Canvas(self, width=500, height=500, borderwidth=5, highlightthickness=0)
            self.canvas.pack(side="top")
            self.new_game()

        #Adds 1 new tiles to board in empty spaces, highlights tile


        
        def addNewTile(self):
            index = random.randint(0,6)
            x = -1
            y = -1
            while self.isFull() == False:
                x = random.randint(0,3)
                y = random.randint(0,3)
                if (self.board[x][y] == 0):
                    self.board[x][y] = self.new_tile_selection[index]
                    x1 = y*130
                    y1 = x*130
                    x2 = x1 + 130 - 5
                    y2 = y1 + 130 - 5
                    num = self.board[x][y]
                    if num == 2:
                        self.square[x,y] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#0029ff", tags="rect", outline="", width=0)
                        self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 36), fill="#3fe470", text="2")
                    elif num == 4:
                        self.square[x,y] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#b8dbe5", tags="rect",  outline="", width=0)
                        self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 36), fill="#3fe470", text="4")
                
                    
                    break
        #Returns True if board is full
        def isFull(self):
            for i in range(0,4):
                for j in range(0,4):
                    if (self.board[i][j] == 0):
                        return False
            return True
        #Prints game board
        def printboard(self):
            cellwidth = 130
            cellheight = 130
            self.square = {}

            for column in range(4):
                for row in range(4):
                    x1 = column*cellwidth
                    y1 = row*cellheight
                    x2 = x1 + cellwidth - 5
                    y2 = y1 + cellheight - 5
                    num = self.board[row][column]
                    if num == 0:
                        self.a(row, column, x1, y1, x2, y2)
                    elif num == 2:
                        self.b(row, column, x1, y1, x2, y2)
                    elif num == 4:
                        self.c(row, column, x1, y1, x2, y2)
                    elif num == 8:
                        self.d(row, column, x1, y1, x2, y2)
                    elif num == 16:
                        self.e(row, column, x1, y1, x2, y2)
                    elif num == 32:
                        self.f(row, column, x1, y1, x2, y2)
                    elif num == 64:
                        self.g(row, column, x1, y1, x2, y2)
                    elif num == 128:
                        self.h(row, column, x1, y1, x2, y2)
                    elif num == 256:
                        self.i(row, column, x1, y1, x2, y2)
                    elif num == 512:
                        self.j(row, column, x1, y1, x2, y2)
                    elif num == 1024:
                        self.k(row, column, x1, y1, x2, y2)
                    elif num == 2048:
                        self.l(row, column, x1, y1, x2, y2)
                    elif num == 4096:
                        self.m(row, column, x1, y1, x2, y2)
                    elif num == 8192:
                        self.n(row, column, x1, y1, x2, y2)
                    elif num ==16384 :
                        self.o(row, column, x1, y1, x2, y2)
                    

        def a(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#000000", tags="rect", outline="")
        def b(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#fe0505", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 36), fill="white", text="2")
        def c(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#00ffea", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 36), fill="white", text="4")
        def d(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#24ff00", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 36), fill="white", text="8")
        def e(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#1c00ff", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 36), fill="white", text="16")
        def f(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#ff00fe", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 36), fill="white", text="32")
        def g(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#66bb6a", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 36), fill="white", text="64")
        def h(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#fff700", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 32), fill="white", text="128")
        def i(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#e357ff", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 32), fill="white", text="256")
        def j(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#b6ff0b", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 32), fill="white", text="512")
        def k(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#9c005d", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 30), fill="white", text="1024")
        def l(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#ff7700", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 30), fill="white", text="2048")
        def m(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#ff0000", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 30), fill="white", text="4096")
        def n(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#ff0000", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 30), fill="white", text="8192")

        def o(self, row, column, x1, y1, x2, y2):
            self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#ff0000", tags="rect", outline="")
            self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 30), fill="white", text="16384")
        
        def save_info(self):
            savescore = str(self.score)

            file = open("highscore.txt", "w")
            file.write(savescore)
            file.close
            
            

        #Creates buttons at top of screen
        def create_widgets(self):
            self.buttonframe = tk.Frame(self)
            self.buttonframe.grid(row=2, column=0, columnspan=4)
            tk.Button(self.buttonframe, text = "New Game",command=self.new_game).grid(row=0, column=0)
            tk.Label(self.buttonframe, text = "Score:").grid(row=0, column=1)
            tk.Label(self.buttonframe, textvariable=self.scorestring).grid(row=0, column=2)
            tk.Label(self.buttonframe, text=b).grid(row=0, column=4)
            tk.Label(self.buttonframe, text = "Record:").grid(row=0, column=3)
            tk.Label(self.buttonframe, text = "Created by RSJ").grid(row=0, column=5)
            self.buttonframe.pack(side="top")

        #executes moves based on arroy keys pressed
        def keyPressed(self,event):
            shift = 0
            if event.keysym == 'Down':
               ## playsound.playsound('C:/Users/johns/OneDrive/Desktop/CS Project Files/Click_sound.mp3', False)
                for j in range(0,4):
                    shift = 0
                    for i in range(3,-1,-1): #This uses the step it will start from 2 and iterate once
                        if self.board[i][j] == 0:
                            shift += 1
                        else:
                            if i - 1 >= 0 and self.board[i-1][j] == self.board[i][j]:
                                self.board[i][j] *= 2
                                self.score += self.board[i][j]
                                self.board[i-1][j] = 0
                            elif i - 2 >= 0 and self.board[i-1][j] == 0 and self.board[i-2][j] == self.board[i][j]:
                                self.board[i][j] *= 2
                                self.score += self.board[i][j]
                                self.board[i-2][j] = 0
                            elif i == 3 and self.board[2][j] + self.board[1][j] == 0 and self.board[0][j] == self.board[3][j]:
                                self.board[3][j] *= 2
                                self.score += self.board[3][j]
                                self.board[0][j] = 0
                            if shift > 0:
                                self.board[i+shift][j] = self.board[i][j]
                                self.board[i][j] = 0
                self.printboard()
                self.addNewTile() 
                self.isOver()
            elif event.keysym == 'Right':
               ## playsound.playsound('C:/Users/johns/OneDrive/Desktop/CS Project Files/Click_sound.mp3', False)
                for i in range(0,4):
                    shift = 0
                    for j in range(3,-1,-1):
                        if self.board[i][j] == 0:
                            shift += 1
                        else:
                            if j - 1 >= 0 and self.board[i][j-1] == self.board[i][j]:
                                self.board[i][j] *= 2
                                self.score += self.board[i][j]
                                self.board[i][j-1] = 0
                            elif j - 2 >= 0 and self.board[i][j-1] == 0 and self.board[i][j-2] == self.board[i][j]:
                                self.board[i][j] *= 2
                                self.score += self.board[i][j]
                                self.board[i][j-2] = 0
                            elif j == 3 and self.board[i][2] + self.board[i][1] == 0 and self.board[0][j] == self.board[3][j]:
                                self.board[i][3] *= 2
                                self.score += self.board[i][3]
                                self.board[i][0] = 0
                            if shift > 0:
                                self.board[i][j+shift] = self.board[i][j]
                                self.board[i][j] = 0
                self.printboard()
                self.addNewTile() 
                self.isOver()
            elif event.keysym == 'Left':
                ##playsound.playsound('C:/Users/johns/OneDrive/Desktop/CS Project Files/Click_sound.mp3', False)
                for i in range(0,4):
                    shift = 0
                    for j in range(0,4):
                        if self.board[i][j] == 0:
                            shift += 1
                        else:
                            if j + 1 < 4 and self.board[i][j+1] == self.board[i][j]:
                                self.board[i][j] *= 2
                                self.score += self.board[i][j]
                                self.board[i][j+1] = 0
                            elif j + 2 < 4 and self.board[i][j+1] == 0 and self.board[i][j+2] == self.board[i][j]:
                                self.board[i][j] *= 2
                                self.score += self.board[i][j]
                                self.board[i][j+2] = 0
                            elif j == 0 and self.board[i][1] + self.board[i][2] == 0 and self.board[i][3] == self.board[i][0]:
                                self.board[i][0] *= 2
                                self.score += self.board[i][0]
                                self.board[i][3] = 0
                            if shift > 0:
                                self.board[i][j-shift] = self.board[i][j]
                                self.board[i][j] = 0
                self.printboard()
                self.addNewTile() 
                self.isOver()
            elif event.keysym == 'Up':
               ## playsound.playsound('C:/Users/johns/OneDrive/Desktop/CS Project Files/Click_sound.mp3', False)
                for j in range(0,4):
                    shift = 0
                    for i in range(0,4):
                        if self.board[i][j] == 0:
                            shift += 1
                        else:
                            if i + 1 < 4 and self.board[i+1][j] == self.board[i][j]:
                                self.board[i][j] *= 2
                                self.score += self.board[i][j]
                                self.board[i+1][j] = 0
                            elif i + 2 < 4 and self.board[i+1][j] == 0 and self.board[i+2][j] == self.board[i][j]:
                                self.board[i][j] *= 2
                                self.score += self.board[i][j]
                                self.board[i+2][j] = 0
                            elif i == 0 and self.board[1][j] + self.board[2][j] == 0 and self.board[3][j] == self.board[0][j]:
                                self.board[0][j] *= 2
                                self.score += self.board[0][j]
                                self.board[3][j] = 0
                            if shift > 0:
                                self.board[i-shift][j] = self.board[i][j]
                                self.board[i][j] = 0
                self.printboard()
                self.addNewTile() 
                self.isOver()
            elif event.keysym == 'w':
                self.youWon()
            elif event.keysym == 'Escape':
                quit()
            elif event.keysym =='l':
                self.youLost()
            elif event.keysym == 'r':
                self.new_game()
            self.scorestring.set(str(self.score))


                

               

            
            
            
        def new_game(self):
            self.score = 0
            self.scorestring.set("0")
            self.board = []
            self.board.append([0,0,0,0])
            self.board.append([0,0,0,0])
            self.board.append([0,0,0,0])
            self.board.append([0,0,0,0])
            while True:
                x = random.randint(0,3)
                y = random.randint(0,3)
                if (self.board[x][y] == 0):
                    self.board[x][y] = 2
                    break

            index = random.randint(0,6)
            while self.isFull() == False:
                x = random.randint(0,3)
                y = random.randint(0,3)
                if (self.board[x][y] == 0):
                    self.board[x][y] = self.new_tile_selection[index]
                    break
            self.printboard()
        

##        def ups(self):
##            if self.board[i][j] == 4096:
##                return 4096
####            elif self.board[i][j] == 8192:
####                return 8192
####            elif self.board[i][j] == 16384:
####                return 16384
        #Returns True if board is full & has no more moves
 
        def isOver(self):
            global flag 
            for i in range(0,4):
                for j in range(0,4):
                        if (self.board[i][j] == 4096):
                            while flag == True:
                                self.youWon()
                                flag = False 
                        

            for i in range(0,4):
                for j in range(0,4):
                    if (self.board[i][j] == 0):
                        return False
            for i in range(0,4):
                for j in range(0,3):
                    if (self.board[i][j] == self.board[i][j+1]):
                        return False
            for j in range(0,4):
                for i in range(0,3):
                    if self.board[i][j] == self.board[i+1][j]:
                        return False
            gameover = [["G", "A", "M", "E",],["O", "V", "E", "R"], ["", "", "", ""],  ["", "", "", ""]]
            cellwidth = 130
            cellheight = 130
            self.square = {}

            for column in range(4):
                for row in range(4):
                    x1 = column*cellwidth
                    y1 = row*cellheight
                    x2 = x1 + cellwidth - 5
                    y2 = y1 + cellheight - 5
                    self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#ee4912", tags="rect", outline="")
                    self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 36), fill="#0071f0", text=gameover[row][column])
            playsound.playsound('C:/Users/johns/OneDrive/Desktop/CS Project Files/Game Over - Sound Effect [HD].mp3', False)
            if int(self.score) > int(self.highscore):
                self.save_info()



##            if str(self.score)> str(self.highscore):
##                self.score= save_info()
            


        def youLost(self):
            gameover = [["G", "A", "M", "E",],["O", "V", "E", "R"], ["", "", "", ""],  ["", "", "", ""]]
            cellwidth = 130
            cellheight = 130
            self.square = {}

            for column in range(4):
                for row in range(4):
                    x1 = column*cellwidth
                    y1 = row*cellheight
                    x2 = x1 + cellwidth - 5
                    y2 = y1 + cellheight - 5
                    self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#ee4912", tags="rect", outline="")
                    self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 36), fill="#0071f0", text=gameover[row][column])
##            l= self.score
##            e = self.highscore
##            if str(l)> str(e):
##                print(l)


##            playsound.playsound('C:/Users/johns/OneDrive/Desktop/Game Over - Sound Effect [HD].mp3', False)

        ## if you are creting a continue button add it here 


        def cont(self):
            self.printboard()
            self.addNewTile()
            
        
    
        def youWon(self):
            tk.Button(self.buttonframe, text = "Continue",command=self.cont).grid(row=2, column=5)
            tk.Button(self.buttonframe, text = "Save Score",command=self.save_info).grid(row=0, column=10)
            gameover = [["Y", "O", "U", "",],["W", "O", "N", "!"], ["", "", "", ""],  ["", "", "", ""]]

            cellwidth = 130
            cellheight = 130
            self.square = {}
            for column in range(4):
                for row in range(4):
                    x1 = column*cellwidth
                    y1 = row*cellheight
                    x2 = x1 + cellwidth - 5
                    y2 = y1 + cellheight - 5
                    self.square[row,column] = self.canvas.create_rectangle(x1,y1,x2,y2, fill="#000000", tags="rect", outline="")
                    self.canvas.create_text((x1 + x2)/2, (y1+y2)/2, font=("Arial", 36), fill="#00ffda", text=gameover[row][column], tags="tre")
            playsound.playsound('C:/Users/johns/OneDrive/Desktop/CS Project Files/Epic Win - Sound Effect [HD] (1).mp3', False)


    
        

    if __name__ == "__main__":
        app = Game()
        app.bind_all('<Key>', app.keyPressed)
        app.wm_title("4096")
        app.minsize(420,450)
        app.maxsize(620,600)
        app.mainloop()



def options():
    running = True
    while running:
        screen.fill((168, 235, 52))
 
        draw_text('The movement of the tiles', font, (255, 255, 255), jij, 35, 100)
        draw_text('occurs by pressng the arrow keys', font, (255, 255, 255), jij, 10, 120)
        draw_text('How to play the game',font, (255,255,255), jij , 60,50)
        draw_text('when two tiles of the same number collide', font, (255, 255, 255), jij, 10, 140)
        draw_text('they merge into creating the sum ', font, (255, 255, 255), jij, 12, 160)
        draw_text('of the two tiles the goal is to ', font, (255, 255, 255), jij, 29, 180)
        draw_text('reach the tile 4096 to win the game ', font, (255, 255, 255), jij, 10, 200)
        draw_text('however you lose the game if the ', font, (255, 255, 255), jij, 15, 220)
        draw_text('board s full and there is no ', font, (255, 255, 255), jij, 35, 240)
        draw_text('possible move left. ', font, (255, 255, 255), jij, 70, 260)





        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        mainClock.tick(60)
pygame.init() 
main_menu()
