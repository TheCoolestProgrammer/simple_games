import pygame
import random
class App:
    def __init__(self):
        pygame.init()

        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.app_running = True

        wall_thick = 10
        self.left_wall= Block(0,0,wall_thick,self.screen_height,"immortal",1)
        self.right_wall= Block(self.screen_width-wall_thick,0,wall_thick,self.screen_height,"immortal",1)
        self.bottom_wall = Block(0,self.screen_height-wall_thick,self.screen_width,wall_thick,"immortal",1)
        self.top_wall = Block(0,0,self.screen_width,wall_thick,"immortal",1)
        # another_block = Block(200,200,100,100,(0,0,255))
        self.blocks=[self.left_wall,self.right_wall,self.top_wall,self.bottom_wall]

        self.board=Board(50,self.screen_height-20)
        self.blocks.append(self.board)
        # block_width = (self.screen_width-(wall_thick*2))//5
        # block_height=20
        # color = [0,50,50]
        # for i in range(2):
        #     color[0] +=100
        #     for j in range(5):
        #         block = Block(block_width*j+wall_thick,wall_thick+i*block_height,block_width,block_height,"mortal",1,color)
        #         self.blocks.append(block)


        ball1 = Ball(50,self.screen_height-40,10,1,100)
        # ball2 = Ball(550,550,10,1,135)
        self.balls = [ball1]


        # self.balls=[]
        # for i in range(5):
        #     angle = random.randint(0,360)
        #
        #     speed = random.randint(1,1)
        #     radius = random.randint(20,40)
        #     x = random.randint(radius+5, self.screen_width-radius-5)
        #     y = random.randint(radius+5, self.screen_height-radius-5)
        #     ball = Ball(x,y,radius,speed,angle)
        #     self.balls.append(ball)
    def events_check(self,events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.app_running=False
            if event.type == pygame.QUIT:
                self.app_running=False
        self.board.moving()
    def drawing(self):
        self.screen.fill((0, 0, 0))
        for ball in self.balls:
            ball.draw(self.screen)
            # ball.draw_vector(self.screen)
        for i in self.blocks:
            i.draw(self.screen)

        pygame.display.update()
    def mainloop(self):
        while self.app_running:
            self.drawing()
            events = pygame.event.get()
            self.events_check(events)
            # print(self.balls[0].angle)
            # new_balls = []
            # for ball in self.balls:
            #     ball.move()
            #     new_balls.append(ball)
            for ball in self.balls:
                # pass
                ball.change_angle(self.blocks, self.balls)
                # print(ball.angle)
            for ball in self.balls:
                ball.move()
            new_blocks=[]
            for block in self.blocks:
                if block.hp !=0:
                    new_blocks.append(block)
            self.blocks=new_blocks
            # self.balls=self.balls
            # print(self.balls[0].angle)
if __name__== "__main__":
    from classes import Ball,Block,Board
    app=App()
    app.mainloop()