import pygame
import time
import random


#global variables
snake_speed = 5
snake_block = 20


class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0
        self.snake_List = []
        self.Length_of_snake = 1

    def our_snake(self,dis,color):
        for x in self.snake_List:
            pygame.draw.rect(dis, color, [x[0], x[1], snake_block, snake_block])

    def add_head(self):
        snake_Head = []
        snake_Head.append(self.x)
        snake_Head.append(self.y)
        self.snake_List.append(snake_Head)
        return snake_Head

class Food:
    def __init__(self,foodx,foody):
        self.foodx = foodx
        self.foody = foody

    def create_food(self,dis,color):
        pygame.draw.rect(dis, color, [self.foodx, self.foody, snake_block, snake_block])

class User:
    def __init__(self,name):
        self.name=name
        self.score=0




class Game:
    def __init__(self):
        self.game_over = False
        self.game_close = False
        self.white = (255, 255, 255)
        self.yellow = (255, 255, 102)
        self.black = (0, 0, 0)
        self.red = (213, 50, 80)
        self.green = (0, 255, 0)
        self.blue = (50, 153, 213)
        self.dis_width = 800
        self.dis_height = 600

    def message(self,dis,msg,color,cord):
        font_style = pygame.font.SysFont("bahnschrift", 35)
        score_font = pygame.font.SysFont("comicsansms", 35)
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg,cord )

    def your_score(self,dis,score1,score2,player1,player2):
        font_style = pygame.font.SysFont("bahnschrift", 35)
        score_font = pygame.font.SysFont("comicsansms", 35)
        value1 = score_font.render(str(player1)+": " + str(score1), True, self.black)
        dis.blit(value1, [0, 0])
        pygame.display.update()
        value2 = score_font.render(str(player2)+": "  + str(score2), True, self.red)
        dis.blit(value2, [self.dis_width / 2, 0])
        pygame.display.update()

    def game_start(self):
        pygame.init()
        dis = pygame.display.set_mode((self.dis_width, self.dis_height))
        pygame.display.set_caption('Snake game by Raihana')
        clock = pygame.time.Clock()
        return dis,clock

    def game_loop(self,dis,clock,name1,name2):
        player1 = User(name1)
        player2 = User(name2)
        game_over = False
        game_close = False
        x1,y1= self.dis_width / 8,self.dis_height / 2
        x2,y2= self.dis_width / 4,self.dis_width / 2

        #creating 2 snakes
        snake1 = Snake(x1,y1)
        snake2 = Snake(x2,y2)

        #creating food
        foodx = round(random.randrange(0, self.dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, self.dis_height - snake_block) / 10.0) * 10.0
        food = Food(foodx,foody)

        while not game_over:
            while game_close == True:
                dis.fill(self.blue)
                if player1.score>player2.score:
                    self.message(dis, "Winner: "+player1.name+ "  Score :" +str(player1.score), self.red, [self.dis_width / 3, self.dis_height / 3])
                elif player1.score<player2.score:
                    self.message(dis, "Winner: "+player2.name+ "  Score :" +str(player2.score), self.red, [self.dis_width / 3, self.dis_height / 3])
                else:
                    self.message(dis, "Winner: tie Score :" +str(player2.score), self.red, [self.dis_width / 3, self.dis_height / 3])
                #pygame.display.update()
                self.message(dis,"Press C-Play Again or Q-Quit", self.red,[self.dis_width / 3, self.dis_height / 2])
                #self.your_score(dis,snake1.Length_of_snake - 1,snake2.Length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            self.game_loop(dis,clock,name1,name2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    #snake1
                    if event.key == pygame.K_LEFT:
                        snake1.x_change = -snake_block
                        snake1.y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        snake1.x_change = snake_block
                        snake1.y_change = 0
                    elif event.key == pygame.K_UP:
                        snake1.y_change = -snake_block
                        snake1.x_change = 0
                    elif event.key == pygame.K_DOWN:
                        snake1.y_change = snake_block
                        snake1.x_change = 0
                    #snake2
                    elif event.key == pygame.K_s:
                        snake2.x_change = -snake_block
                        snake2.y_change = 0
                    elif event.key == pygame.K_f:
                        snake2.x_change = snake_block
                        snake2.y_change = 0
                    elif event.key == pygame.K_e:
                        snake2.y_change = -snake_block
                        snake2.x_change = 0
                    elif event.key == pygame.K_d:
                        snake2.y_change = snake_block
                        snake2.x_change = 0



            if snake1.x >= self.dis_width or snake1.x < 0 or \
                    snake1.y >= self.dis_height or snake1.y < 0 or \
                    snake2.x >= self.dis_width or snake2.x < 0 or \
                    snake2.y >= self.dis_height or snake2.y < 0:
                game_close = True

            snake1.x += snake1.x_change
            snake1.y += snake1.y_change
            snake2.x += snake2.x_change
            snake2.y += snake2.y_change

            dis.fill(self.blue)
            food.create_food(dis,self.green)
            snake_head1,snake_head2 = [],[]
            snake_head1 = snake1.add_head()
            snake_head2 = snake2.add_head()


            if len(snake1.snake_List) > snake1.Length_of_snake :
                del snake1.snake_List[0]
            if len(snake2.snake_List) > snake2.Length_of_snake :
                del snake2.snake_List[0]

            for x in snake1.snake_List[:-1]:
                if x == snake_head1:
                    game_close = True
            for x in snake2.snake_List[:-1]:
                if x == snake_head2:
                    game_close = True


            snake1.our_snake(dis,self.black)
            snake2.our_snake(dis,self.red)
            player1.score = snake1.Length_of_snake - 1
            player2.score = snake2.Length_of_snake - 1
            self.your_score(dis,player1.score,player2.score,player1.name,player2.name)

            pygame.display.update()

            if (snake1.x == food.foodx and snake1.y == food.foody) or \
                    (snake1.x == food.foodx + 10 and snake1.y == food.foody) or \
                    (snake1.x == food.foodx and snake1.y == food.foody + 10) or \
                    (snake1.x == food.foodx - 10 and snake1.y == food.foody) or \
                    (snake1.x == food.foodx and snake1.y == food.foody - 10) or \
                    (snake1.x == food.foodx + 10 and snake1.y == food.foody + 10) or \
                    (snake1.x == food.foodx - 10 and snake1.y == food.foody - 10):
                food.foodx = round(random.randrange(0, self.dis_width - snake_block) / 10.0) * 10.0
                food.foody = round(random.randrange(0, self.dis_height - snake_block) / 10.0) * 10.0
                snake1.Length_of_snake += 1

            if (snake2.x == food.foodx and snake2.y == food.foody) or \
                    (snake2.x == food.foodx + 10 and snake2.y == food.foody) or \
                    (snake2.x == food.foodx and snake2.y == food.foody + 10) or \
                    (snake2.x == food.foodx - 10 and snake2.y == food.foody) or \
                    (snake2.x == food.foodx and snake2.y == food.foody - 10) or \
                    (snake2.x == food.foodx + 10 and snake2.y == food.foody + 10) or \
                    (snake2.x == food.foodx - 10 and snake2.y == food.foody - 10):
                food.foodx = round(random.randrange(0, self.dis_width - snake_block) / 10.0) * 10.0
                food.foody = round(random.randrange(0, self.dis_height - snake_block) / 10.0) * 10.0
                snake2.Length_of_snake += 1

            player1.score = snake1.Length_of_snake - 1
            player2.score = snake2.Length_of_snake - 1
            self.your_score(dis, player1.score, player2.score, player1.name, player2.name)
            pygame.display.update()

            clock.tick(snake_speed)

        pygame.quit()
        quit()






import tkinter as tk

def submit():
    plyr1 = player1_var.get()
    plyr2 = player2_var.get()
    root.quit()
    """    player1_var.set("")
    player2_var.set("")"""

    game = Game()
    dis, clock = game.game_start()
    font_style = pygame.font.SysFont("bahnschrift", 35)
    score_font = pygame.font.SysFont("comicsansms", 35)
    game.game_loop(dis, clock,plyr1,plyr2)


root = tk.Tk()
root.title("Snake Multiplayer")

# setting the windows size
root.geometry("300x100")

# declaring string variable
player1_var = tk.StringVar()
player2_var = tk.StringVar()

player1_label = tk.Label(root, text='Player1', font=('calibre', 10, 'bold'))

player1_entry = tk.Entry(root, textvariable=player1_var, font=('calibre', 10, 'normal'))

player2_label = tk.Label(root, text='Player2', font=('calibre', 10, 'bold'))

player2_entry = tk.Entry(root, textvariable=player2_var, font=('calibre', 10, 'normal'))


sub_btn = tk.Button(root, text='Start Game', command=submit)

player1_label.grid(row=0, column=0)
player1_entry.grid(row=0, column=1)
player2_label.grid(row=1, column=0)
player2_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)




# performing an infinite loop
# for the window to display
root.mainloop()















