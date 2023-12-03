from obstacle import Obstacle
import random


class ObstacleGenerator:
	def __init__(self, screenwidth, screenheight):
		self.frames_since_last = 0
		self.wait_time = 120
		self.screenwidth = screenwidth
		self.screenheight = screenheight

	def add_obstacle(self):
		if self.frames_since_last > self.wait_time:
			z = random.random()
			if z > 0.70:
				self.frames_since_last = 0
				return Obstacle(self.screenwidth, self.screenheight)


	def update(self):
		self.frames_since_last += 1

	

class Obstacles:
	def __init__(self, screenwidth, screenheight):
		self.obstacles = []
		self.generator = ObstacleGenerator(screenwidth, screenheight)

	def update(self, screen):
		self.generator.update()
		new_obstacle = self.generator.add_obstacle()

		if new_obstacle:
			self.obstacles.append(new_obstacle)

		for obstacle in self.obstacles:
			obstacle.update()
			if obstacle.x < -500:
				obstacle.kill()
				del obstacle
			else:
				screen.blit(obstacle.image, (obstacle.rect_upper.x, obstacle.rect_upper.y))
				screen.blit(obstacle.image, (obstacle.rect_lower.x, obstacle.rect_lower.y))