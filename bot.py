from random import random
from ball import Ball
import neat

class Bots:
  def __init__(self, genomes, config, screen, gravity, ball_initial_x, ball_initial_y):
    self.genomes = genomes
    self.nets = []
    self.bots = []
    self.left = ball_initial_x
    self.remaining_bots = len(genomes)

    for id, g in genomes:
      net = neat.nn.FeedForwardNetwork.create(g, config)
      self.nets.append(net)
      g.fitness = 0

      self.bots.append(Bot(screen, gravity, ball_initial_x, ball_initial_y))
  
  def update(self, obstacles):
    for i, bot in enumerate(self.bots):
      output = self.nets[i].activate(bot.perceive(obstacles))
      if output[0] > 0.5:
        bot.boost()

    self.remaining_bots = 0
    for i, bot in enumerate(self.bots):
        if (not bot.dead):
          bot.update()
          self.remaining_bots += 1
          self.genomes[i][1].fitness += bot.get_reward()


class Bot:
  def __init__(self, screen, gravity, ball_initial_x, ball_initial_y):
    self.ball = Ball(screen, gravity, ball_initial_x, ball_initial_y)
    self.dead = False
    self.score = 0

  def perceive(self, obstacles):
    obstacle_x, obstacle_y = obstacles[0].rect_lower.topleft
    ball_y = self.ball.rect.top
    return [obstacle_x, obstacle_y, ball_y]

  def boost(self):
      self.ball.boost()
    
  def update(self):
    self.score += 1 / 10000
    self.ball.update()

  def get_reward(self):
    return self.score

    
  def die(self):
    self.dead = True
  