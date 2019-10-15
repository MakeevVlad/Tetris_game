#from settings import *
from kernel import *



#initializing ball
ball = Ball([10, 10, 20, 20], 'blue', 10)
platform = Platform()
interface_init(ball, platform)

#Runs game
def game():
    ball.move_ball(platform)
    ball.draw_ball()
    platform.draw_platform()
    root.after(1, game)

game()
mainloop()