from tkinter import *

root = Tk()
root.geometry('800x600')
field = [800, 600]

canv = Canvas(root, bg = 'white')
canv.pack(fill=BOTH, expand=1)

class Ball():
    def __init__(self, state=[0, 0, 0, 0], color='red', r=10):
        self.pos = [state[0], state[1]]
        self.vel = [state[2], state[3]]
        self.color = color
        self.r = r
        self.draw_ball()

    def draw_ball(self):
        canv.delete(ALL)
        canv.create_oval(
        self.pos[0] - self.r, self.pos[1] - self.r, 
        self.pos[0] + self.r, self.pos[1] + self.r, 
        fill = self.color)

    def move_ball(self):
        self = hit(self)
        self.pos = pos_step(self.pos, self.vel)
        self.vel = vel_step(self.vel, self.pos)

#changes ball's velocity due to the different collisionss
def hit(ball):
    ball = wall_hit(ball)
    return ball

#turnes ball's velocity if it hits the wall
def wall_hit(ball):
    #right wall
    if ball.pos[0] <= 0 or ball.pos[0] >= field[0]:
        ball.vel[0]*=-1
    if ball.pos[1] <= 0 or ball.pos[1] >= field[1]:
        ball.vel[1]*=-1
    return ball

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
    def __init__(self, pos=field[0]*0.5, size=20, color='black'):
        self.x = pos
        self.size = size
        self.color = color