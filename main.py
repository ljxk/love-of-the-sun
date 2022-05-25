import pygame,random,sys,math
from pygame.locals import *
from cat import *
from player import *
from sprite_load import *

pygame.init()
screen_info = pygame.display.Info()
size = (width, height) = (screen_info.current_w, screen_info.current_h)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 0, 0)
cat_images = []
man_images = []
def getimages():
  catsheet = SpriteSheet('runningcat.png')
  mansheet = SpriteSheet('mrman.jpg')
  directions = ['n', 'w', 's', 'e']
  for i in range(4):
    for j in range(2):
      cat_images.append(cat_sheet.get_image(j*512, i*256, 512, 256)) 
      cat_images[-1] = pygame.transform.smoothscale(cat_images[-1], (180, 90))
    for i in range(len(directions)):
      for j in range(9):
        man_images[directions[i]+str(j)] = man_sheet.get_image(j*64, i*64, 64, 64)

def main():
  cat(-90,random.randint(50, height-50)), cat_images
  Player((width//2, height//2), man_images)
  while True:
    pass