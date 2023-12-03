import pygame

class Obstacle(pygame.sprite.Sprite):
  def __init__(self, screenwidth, screenheight):
    super().__init__()
    
    self.image = pygame.image.load('images/obstacle.png')

    self.x = screenwidth*1.1
    self.y_upper = 0
    self.y_lower = screenheight - self.image.get_height()

    self.x_velocity = -5
    self.rect_upper = self.image.get_rect()
    self.rect_lower = self.image.get_rect()

    self.rect_upper.topleft = [self.x, self.y_upper]
    self.rect_lower.topleft = [self.x, self.y_lower]

  def update(self):
    self.x += self.x_velocity
    self.rect_upper.x = self.x
    self.rect_lower.x = self.x