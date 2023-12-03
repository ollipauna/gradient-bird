import pygame

class Ball(pygame.sprite.Sprite):
  def __init__(self, gravity, x, y):
    super().__init__()
    self.y_velocity = 0
    self.gravity = gravity

    self.image = pygame.image.load('images/ball.png')
    self.rect = self.image.get_rect()
    self.rect.topleft = [x, y]

  def update(self, screen):

    self.rect.y += self.y_velocity

    if self.rect.y > 1200:
      self.rect.y = 0

    self.y_velocity += self.gravity

    screen.blit(self.image, self.rect)

  def boost(self):
    self.y_velocity = -10