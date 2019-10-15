from tkinter import *
import random as rnd

root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg = 'white')
canv.pack(fill=BOTH, expand=1)
field = [400, 300]

polygon = canv.create_polygon(0, 0, field[0], field[1])



class Ball:
    def __init__(self, state=[0, 0, 0, 0], color='red', r=10):
        self.pos = [state[0], state[1]]
        self.vel = [state[2], state[3]]
        self.color = color
        self.r = r
        self.obj = canv.create_oval(0, 0, 0, 0)
        self.draw_ball()

    def draw_ball(self):
        canv.delete(self.obj)
        self.obj = canv.create_oval(
        self.pos[0] - self.r, self.pos[1] - self.r, 
        self.pos[0] + self.r, self.pos[1] + self.r, 
        fill = self.color)

    def move_ball(self, platform):
        self = hit(self, platform)
        self.pos = pos_step(self.pos, self.vel)
        self.vel = vel_step(self.vel, self.pos)

#changes ball's velocity due to the different collisionss
def hit(ball, platform):
    ball = platform_hit(ball, platform)
    ball = floor_hit(ball)
    ball = wall_hit(ball)
    return ball

#turnes ball's velocity if it hits the wall
def wall_hit(ball):
    if ball.pos[0] <= 0 or ball.pos[0] >= field[0]:
        ball.vel[0]*=-1
    if ball.pos[1] <= 0 or ball.pos[1] >= field[1]:
        ball.vel[1]*=-1
    return ball

def floor_hit(ball):
    if ball.pos[1] >= field[1]:
        ball.vel = [0, 0]
        #the_end(ball)
    return(ball)

def platform_hit(ball, platform):
    if (ball.pos[1] + ball.r > field[1] - 25 - platform.sizey and
    ball.pos[1] <= field[1]-25 and
    ball.pos[0]>=platform.x  and 
    ball.pos[0]<=platform.x + platform.sizex):
        ball.vel[1]*=-1
        ball.pos[1] = field[1] - 25 - platform.sizey - ball.r
    return(ball)


#Draws game over screen       
def the_end(ball):
    end = canv.create_rectangle(0, 0, field[0], field[1], fill = 'red')

#changes coordinates of the ball along the timeline
def pos_step(pos, vel, dt=0.01):
    pos[0]+= vel[0]*dt
    pos[1]+= vel[1]*dt
    return pos

#changes velocity of the ball along the timeline
def vel_step(vel, pos, dt=0.01):
    return vel

#================================================

class Platform:
    def __init__(self, pos=field[0]*0.5, sizey=50, sizex = 10, color='black'):
        self.x = pos
        self.sizey = sizey
        self.sizex = sizex
        self.color = color
        self.draw_platform
        self.obj = canv.create_rectangle(0, 0, 0, 0)
        self.draw_platform()

    def draw_platform(self):
        canv.delete(self.obj)
        self.obj = canv.create_rectangle(
            self.x, field[1] - 25, self.x + self.sizey, field[1] - 25 - self.sizex,
            fill = self.color)   
    
    def move_platform_right(self):
        self.x = pos_platform_step(self.x, self.sizey)
    def move_platform_left(self):
        self.x = pos_platform_step(self.x, -self.sizey)
    

#=========================
def platform_movement_buttons(platform):
    move_platform_right_button = Button(root, 
    command = platform.move_platform_right, text = '-->')
    move_platform_left_button  = Button(root, 
    command = platform.move_platform_left,  text = '<--')
    move_platform_right_button.place(x = field[0] - 40, y = field[1] - 40)
    move_platform_left_button.place(x = 40, y = field[1] - 40)

def pos_platform_step(pos, vel, dt = 1):
    pos += vel*dt
    return pos