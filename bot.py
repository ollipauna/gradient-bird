from random import random
from box import Box
import neat

class Bots:
  def __init__(self, genomes, config, screen, gravity, box_initial_x, box_initial_y):
    self.genomes = genomes
    self.nets = []
    self.bots = []
    self.left = box_initial_x
    self.remaining_bots = len(genomes)

    for id, g in genomes:
      net = neat.nn.FeedForwardNetwork.create(g, config)
      self.nets.append(net)
      g.fitness = 0

      self.bots.append(Bot(screen, gravity, box_initial_x, box_initial_y))
  
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
  def __init__(self, screen, gravity, box_initial_x, box_initial_y):
    self.box = Box(screen, gravity, box_initial_x, box_initial_y)
    self.dead = False
    self.score = 0

  def perceive(self, obstacles):
    obstacle_x, obstacle_y = obstacles[0].rect_lower.topleft
    box_y = self.box.rect.top
    return [obstacle_x, obstacle_y, box_y]

  def boost(self):
      self.box.boost()
    
  def update(self):
    self.score += 1 / 10000
    self.box.update()

  def get_reward(self):
    return self.score

    
  def die(self):
    self.dead = True
  