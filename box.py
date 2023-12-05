import pygame
import math

class Box(pygame.sprite.Sprite):
  def __init__(self, screen, gravity, x, y):
    super().__init__()
    self.y_velocity = 0
    self.gravity = gravity
    self.screen = screen
    self.image = pygame.image.load('images/ball.png')
    self.rect = self.image.get_rect()
    self.rect.topleft = [x, y]

  def update(self):

    self.rect.y += self.y_velocity

    if self.rect.y > 1200:
      self.rect.y = 0

    self.y_velocity += self.gravity

    self.screen.blit(self.image, self.rect)

  def boost(self):
    self.y_velocity = -10 * (math.log(self.gravity/0.5) + 1)