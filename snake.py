import pygame
import random
class Snake:
    def __init__(self,x,y,block_width,block_height):
        self.body = [[x,y]]
        self.color=(0,255,0)
        self.block_width=block_width
        self.block_height=block_height
        self.direction=1
    def draw(self,screen):
        for i in self.body:
            pygame.draw.rect(screen,self.color,(i[0]*self.block_width,i[1]*self.block_height,self.block_width,self.block_height))
    def moving(self,food_coords):
        new_head =self.body[-1].copy()
        if self.direction == 0:
            new_head[1] = self.body[-1][1]-1
        elif self.direction==1:
            new_head[0] = self.body[-1][0]+1
        elif self.direction==2:
            new_head[1] = self.body[-1][1]+1
        elif self.direction ==3:
            new_head[0] = self.body[-1][0]-1

        if not self.can_grow(food_coords,new_head):
            self.body.append(new_head)
            del(self.body[0])
        else:
            self.grow(food_coords,new_head)
    def can_grow(self,food_coords,head_coords):
        if self.direction==0 and [head_coords[0],head_coords[1]] in food_coords:
            return True
        elif self.direction==1 and [head_coords[0],head_coords[1]] in food_coords:
            return True
        elif self.direction==2 and [head_coords[0],head_coords[1]] in food_coords:
            return True
        elif self.direction==3 and [head_coords[0],head_coords[1]] in food_coords:
            return True
        else:
            return False
    def grow(self,food_coords,head_coords):
        del (food_coords[food_coords.index(head_coords)])
        self.body.append(head_coords)
class Menu:
    def __init__(self,x,y,text_size=30,text_color=(0,0,255)):
        self.font = pygame.font.SysFont("Times New Roman",text_size)
        self.text_color=text_color
        self.x=x
        self.y=y
    def draw(self,screen,scores,x,y,width,height):
        pygame.draw.rect(screen,(200,200,200),(x,y,width,height))
        surface =self.font.render(f"scores: {str(scores)}",False,self.text_color)
        screen.blit(surface,(self.x,self.y))
class App:
    def __init__(self):
        pygame.init()

        self.screen_width = 800
        self.screen_height = 640
        self.game_width = 800
        self.game_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.app_running = True
        self.field_width = 20
        self.field_height = 20
        self.snake = Snake(5,5,self.game_width/self.field_width,self.game_height/self.field_height)
        self.food_coords=[]

        self.food_number=3
        self.food_color = (255,255,0)

        self.add_food()
        self.frames_for_wait=100
        self.frames=0
        self.menu=Menu(20,self.game_height)
        self.scores = 0

        self.need_to_give_scores=False
        self.need_to_up_speed=False
        self.speed_boosters={
            5:5,
            10:10,
            15: 5,
            20: 5,
            30: 5,
            50: 5,
            80: 5,
            100: 15
        }
    def events_check(self,events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.app_running=False
                elif event.key == pygame.K_w:
                    self.snake.direction=0
                elif event.key == pygame.K_d:
                    self.snake.direction = 1
                elif event.key == pygame.K_s:
                    self.snake.direction = 2
                elif event.key == pygame.K_a:
                    self.snake.direction = 3

            if event.type == pygame.QUIT:
                self.app_running=False
    def drawing(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.draw_food()
        # pygame.draw.line(self.screen, (255, 255, 255), (0, self.game_height), (self.game_width, self.game_height), 5)
        self.menu.draw(self.screen,self.scores,0,self.game_height,self.game_width,self.screen_height-self.game_height)
        pygame.display.update()
    def draw_food(self):
        for i in self.food_coords:
            pygame.draw.rect(self.screen,self.food_color,(i[0]*self.snake.block_width,i[1]*self.snake.block_height,self.snake.block_width,self.snake.block_height))
    def add_food(self):
        if len(self.food_coords) < self.food_number:
            while len(self.food_coords) < self.food_number:
                x = random.randint(0, self.field_width-1)
                y = random.randint(0, self.field_height-1)
                if [x, y] not in self.snake.body and [x, y] not in self.food_coords:
                    self.food_coords.append([x, y])
            self.need_to_up_speed=True
            self.need_to_give_scores=True
            # self.give_scores()
    def give_scores(self):
        self.scores+=1
        self.need_to_give_scores=False
        # self.scores+= int((self.food_number-len(self.food_coords)) * (1/self.frames_for_wait)*100)
    def speed_booster(self):
        for i in self.speed_boosters.keys():
            max_scores=i
            break

        for i in self.speed_boosters.keys():
            if i< self.scores:
                max_scores=i
            else:
                max_scores = i
                break
        if self.scores ==max_scores:
            self.frames_for_wait-= self.speed_boosters[max_scores]
            self.need_to_up_speed=False

    def mainloop(self):
        # self.scores=99
        while self.app_running:
            self.drawing()
            events = pygame.event.get()
            self.events_check(events)
            print(self.frames_for_wait)
            if self.frames<self.frames_for_wait:
                self.frames+=1
            else:
                self.frames=0
                self.snake.moving(self.food_coords)

                # self.scores=10

                self.add_food()
                if self.need_to_give_scores:
                    self.give_scores()
                if self.need_to_up_speed:
                    self.speed_booster()

if __name__== "__main__":
    app=App()
    app.mainloop()