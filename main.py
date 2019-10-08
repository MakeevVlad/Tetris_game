#from settings import *
from kernel import *



#initializing ball
ball = Ball([400, 300, 100, 100], 'blue', 10)
platform = Platform()
platform_movement_buttons(platform)
#Runs game
def game():
    ball.move_ball()
    ball.draw_ball()
    root.after(1, game)

game()
mainloop()