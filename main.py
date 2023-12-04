import sys
import pygame
from generation import Generation
import neat
import pickle
import math

speed_up = 5
gravity = 0.5 * speed_up**2 
speed = 5 * speed_up
screenwidth = 1600
screenheight = 900
ball_initial_x = 450
ball_initial_y = 450
background_color = 'lightblue'

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("Gradient Bird")

n = 1

def main(genomes, config):
  global n, speed
  generation = Generation(n, genomes, config, speed, screen, screenwidth, screenheight, ball_initial_x, ball_initial_y, gravity)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      
    if(generation.checkForEnd()):
      n += 1
      break

    screen.fill(background_color)
    generation.update()
    pygame.display.flip()
    clock.tick(60)


if __name__=='__main__':
  config_path = "./config-feedforward.txt"
  config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                              neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
  
  p = neat.Population(config)
  p.add_reporter(neat.StdOutReporter(True))
  stats = neat.StatisticsReporter()
  p.add_reporter(stats)

  winner = p.run(main, 1000)
  with open ("best.pickle", "wb") as f:
    pickle.dump(winner, f)

  print('\nBest genome:\n{!s}'.format(winner))