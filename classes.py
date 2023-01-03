import pygame
import math
class Ball:
    def __init__(self,x,y,radius,speed=2,angle=0):
        self.x=x
        self.y=y
        self.radius=radius
        self.speed = speed
        self.angle=angle
        self.color=(255,255,255)
        self.plus_90 = [
            ("left","down"),
            ("right","up"),
            ("down","right"),
            ("up","left")
        ]
        self.frames_for_collision_check = 5
        self.frames = 0
    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)

    def draw_vector(self,screen):
        # pygame.draw.line(screen,(0,255,0),(self.x - (self.speed*4*self.radius),self.y),(self.x+(self.speed*4*self.radius),self.y),5)
        # pygame.draw.line(screen,(0,255,0),(self.x,self.y - (self.speed*4*self.radius)),(self.x,self.y+(self.speed*4*self.radius)),5)
        pygame.draw.line(screen,(255,0,0),(self.x,self.y),(self.x +math.cos(math.radians(self.angle))*4*self.radius,self.y -math.sin(math.radians(self.angle))*self.radius*4),5)
        # pygame.draw.line(screen,(0,255,0),())
        # pygame.draw.line(screen,(0,255,0),())
    def move(self):
        self.x = self.x +math.cos(math.radians(self.angle))*self.speed
        self.y = self.y -math.sin(math.radians(self.angle))*self.speed

        # if collision: print(collision)

    def change_angle(self,blocks,balls):
        # if self.frames !=self.frames_for_collision_check:
        #     self.frames+=1
        #     return
        # else:
        #     self.frames=0
        collision = self.has_collision(blocks, balls)
        # if collision: print(collision)
        if collision:
            # self.color=(0,255,0)
            print(collision)
            # print("_____________________")

            if collision in self.plus_90:
                self.angle+=90
            else:
                self.angle-=90
            if self.angle <0:
                self.angle = 360+self.angle
            self.angle = self.angle%360
            # if collision=="up" or collision == "down":
            #     self.angle=360-self.angle
            #
            # elif collision=="right":
            #     # self.angle = self.angle+90
            #     self.angle = -(self.angle-180 )
            # elif collision == "left":
            #     self.angle = self.angle +(90-self.angle)*2


            # elif len(collision)==2:
            #     # for balls
            #     # print("balls")
            #     if collision[1] == "up" or collision[1] == "down":
            #         # collision[0].angle = -collision[0].angle
            #         self.angle = -self.angle
            #     elif collision[1] == "right":
            #         # collision[0].angle = collision[0].angle + (90 - collision[0].angle) * 2
            #         self.angle = -(self.angle - 180)
            #     elif collision[1] == "left":
            #         self.angle = self.angle + (90 - self.angle) * 2
            # self.angle = round(self.angle)
            # if 60> self.angle %90 <30:
            #     self.angle=+30
                    # collision[0].angle  = -(collision[0].angle - 180)
                    # self.y = self.y - math.sin(math.radians(self.angle)) * self.speed
                # collision[0].x = collision[0].x + math.cos(math.radians(collision[0].angle)) * collision[0].speed
                # collision[0].y = collision[0].y - math.sin(math.radians(collision[0].angle)) * collision[0].speed
                # moved_balls.append(collision[0])
        # self.x = self.x + math.cos(math.radians(self.angle)) * self.speed
        # self.y = self.y - math.sin(math.radians(self.angle)) * self.speed
        # else:
        #     self.color = (255,0,0)
    def has_collision(self,blocks,balls):
        has_collision=False
        for block in blocks:
            # if block.x-self.radius<= new_pos[0] <= block.x+block.width-self.radius or block.y+self.radius>= new_pos[1] >= block.y+block.height-self.radius:
            # if (abs(block.x-self.x) <=self.radius or abs(self.x -(block.x+block.width))<=self.radius) or\
            #         ( abs(block.y-self.y) <=self.radius or abs(self.y-(block.y+block.height)) <=self.radius):
            if ((block.x<= self.x+self.radius <=  block.x+block.width or block.x<= self.x-self.radius <=  block.x+block.width )and \
                (block.y <= self.y - self.radius <= block.y + block.height or block.y <= self.y + self.radius <= block.y + block.height)) :
            #  (block.x <= self.x <= block.x+block.width and block.y <=self.y<=block.y+block.height):
                vector=[]
                # >= self.x-self.radius
                if self.x>=block.x+block.width :

                    vector.append("right")
                # self.x+self.radius>=
                elif block.x >= self.x:
                    vector.append("left")
                #self.y-self.radius<=
                elif block.y+block.height<=self.y:
                    vector.append("up")
                # self.y+self.radius>=
                elif  block.y>= self.y:
                    vector.append("down")
                if vector:
                    if not block.type == "immortal":
                        block.hp-=1
                    if vector[0] =="left" or vector[0] =="right":
                        if 180<self.angle%360 <360:
                            vector.append("up")
                        else:
                            vector.append("down")
                    else:
                        if 90<self.angle%360 <270:
                            vector.append("left")
                        else:
                            vector.append("right")
                    return vector
        for ball in balls:
            # print(abs(self.x-ball.x))
            # print(abs(self.y-ball.y))
            if ball == self :
                continue
            if self.radius+ball.radius >= ((self.x - ball.x)**2 + (self.y-ball.y)**2)**0.5:
                vector=[]
                if self.x>=ball.x:
                    vector=["right"]
                elif self.x<= ball.x:
                    vector=["left"]
                elif self.y>=ball.y:
                    vector=["down"]
                elif self.y< ball.y:
                    vector=["up"]
                if vector:
                    if vector[0] =="left" or vector[0] =="right":
                        if 180<self.angle%360 <360:
                            vector.append("up")
                        else:
                            vector.append("down")
                    else:
                        if 90<self.angle%360 <270:
                            vector.append("left")
                        else:
                            vector.append("right")
                    return vector
        return has_collision
class Block:
    def __init__(self,x,y,width,height,type="mortal",hp=1,color=(255,255,0)):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color

        self.type = type
        # if self.type == "mortal":
        self.hp = hp
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))
class Board(Block):
    def __init__(self,x,y):
        super(Board, self).__init__(x,y,100,20,"immortal",1,(0,0,255))
    def moving(self):
        self.x=pygame.mouse.get_pos()[0]
