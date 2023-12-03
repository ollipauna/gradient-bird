import sys
import pygame
from ball import Ball
from obstacle import Obstacle
from obstacles import Obstacles

gravity = 0.5
screenwidth = 1760
screenheight = 990
ball_initial_x = 100
ball_initial_y = 50


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("Gradient Bird")

def main():

  screen.fill('lightblue')
  ball = Ball(gravity, ball_initial_x, ball_initial_y)
  obstacles = Obstacles(screenwidth, screenheight)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          ball.boost()


    screen.fill('lightblue')
    obstacles.update(screen)
    ball.update(screen)
    pygame.display.flip()
    clock.tick(60)


if __name__=='__main__':
  main()