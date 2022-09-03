import pgzrun
from random import randint

HEIGHT = 800
WIDTH = 1000

ps = 3 # player speed
es = 3 # enemy speed

game_over = False  # switch
game_started = False # switch

center = (WIDTH//2, HEIGHT//2) # points to center coordinates of screen

bg = Actor('bg', center=(0,0))

def show_screen_1():
        screen.fill('#ffff00')
        bg.draw()
        screen.draw.text('Our Game', center=center, fontsize=100, color='white')
        screen.draw.text('press Space to start', center = (center[0], center[1]+100), 
                        fontsize=50, color='white')
def draw():
    if not game_started:
        show_screen_1()

def update():
    pass

pgzrun.go()