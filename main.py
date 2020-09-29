import pygame
import time
import random
import numpy as np
import os
import grid
# import tkinter as tk
try:
    import Tkinter as tk
except:
    import tkinter as tk

os.environ["SDL_VIDEO_CENTERED"]='1'

width, height = 1920,1080
size = (width, height)

pygame.init()
pygame.display.set_caption("CONWAY'S GAME OF LIFE")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0,14,71)
white = (255, 255, 255)

scaler = 40
offset = 1

Grid = grid.Grid(width,height, scaler, offset)
Grid.random2d_array()


run = False

root = tk.Tk()
root.geometry = ('100x50')
root.title("Right there")

btn = tk.Button(root, text="Start the game", command=lambda:onClick(True))

def onClick(x):
    global run
    run = x
    root.destroy()

def onClear(x):
    global run
    run = x
    root2.destroy()

btn.pack()
root.mainloop()


while run:
    clock.tick(fps)
    screen.fill(black) 
    
    root.mainloop()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    Grid.Conway(off_color=white, on_color=blue1, surface=screen)
    pygame.display.update()

root2 = tk.Tk()
btn2 = tk.Button(root2, text="Clear the game", command=lambda:onClear(False))
btn2.pack()
root2.mainloop()    

pygame.quit()