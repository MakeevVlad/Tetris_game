#from settings import *
from kernel import *



#initializing ball
ball = Ball([200, 150, 20, 20], 'blue', 10)
platform = Platform()
platform_movement_buttons(platform)
#Runs game
def game():
    ball.move_ball(platform)
    ball.draw_ball()
    platform.draw_platform()
    root.after(1, game)

game()
mainloop()