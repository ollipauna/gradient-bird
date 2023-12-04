import pygame
import random

class Obstacle(pygame.sprite.Sprite):
  def __init__(self, speed, screenwidth, screenheight):
    super().__init__()
    self.passed = False
    self.image = pygame.image.load('images/obstacle.png')
    self.width = self.image.get_width()
    self.height = self.image.get_height()

    self.space = round(screenheight - 3.5*self.width)
    self.min_height = round(screenheight * 0.1)
    self.max_height = round(screenheight*0.9) - self.space

    self.x = screenwidth*1.1
    self.y_upper = random.randint(self.min_height, self.max_height)
    self.y_lower = self.y_upper + self.space

    self.x_velocity = -speed
    self.rect_upper = self.image.get_rect()
    self.rect_lower = self.image.get_rect()

    self.rect_upper.bottomleft = [self.x, self.y_upper]
    self.rect_lower.topleft = [self.x, self.y_lower]

  def update(self):
    self.x += self.x_velocity
    self.rect_upper.x = self.x
    self.rect_lower.x = self.x

  def pass_obstacle(self):
    self.passed = True

  @property
  def ScoreLogged(self):
    return self.passed
  

class ObstacleGenerator:
	def __init__(self, speed, screenwidth, screenheight):
		self.speed = speed
		self.frames_since_last = 0
		self.wait_time = 120 / (self.speed/5)
		self.screenwidth = screenwidth
		self.screenheight = screenheight

	def add_obstacle(self):
		if self.frames_since_last > self.wait_time:
			self.frames_since_last = 0
			return Obstacle(self.speed, self.screenwidth, self.screenheight)


	def update(self):
		self.frames_since_last += 1

	

class Obstacles:
	def __init__(self, speed, screen, screenwidth, screenheight):
		self.obstacles = [Obstacle(speed, screenwidth, screenheight)]
		self.generator = ObstacleGenerator(speed, screenwidth, screenheight)
		self.screen = screen
		self.speed = speed

	def update(self):
		self.generator.update()
		new_obstacle = self.generator.add_obstacle()

		if new_obstacle:
			self.obstacles.append(new_obstacle)

		self.obstacles = [obs for obs in self.obstacles if obs.x > -1000]

		for obstacle in self.obstacles:
				obstacle.update()
				self.screen.blit(obstacle.image, (obstacle.rect_upper.x, obstacle.rect_upper.y))
				self.screen.blit(obstacle.image, (obstacle.rect_lower.x, obstacle.rect_lower.y))