import pygame
class player(pygame.sprite.Sprite):
  def __init__(self,pos,images):
    super().__init__()
    self.images = images
    self.image = images[0]
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.speed = [8, 0]

def update(self): 
  if self.speed[0] != 0 or self.speed[1] != 0: 
    frame = pygame.time.get_ticks() // 100 % 9 
    self.image = self.images[self.heading + str(frame)] 
  else: self.image = self.images[self.heading + "0"] 
  self.rect.move_ip(self.speed) 
  self.speed = [0, 0] 
  def draw(self, screen): screen.blit(self.image, self.rect)
