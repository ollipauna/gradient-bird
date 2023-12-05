from obstacle import Obstacles
from box import Ball
from bot import Bots
import pygame


class Generation:
	def __init__(self, n, genomes, config, screen, screenwidth, screenheight, box_initial_x, box_initial_y, gravity):
		self.screenheight = screenheight
		self.screen = screen
		self.bots = Bots(genomes, config, screen, gravity, box_initial_x, box_initial_y)
		self.obstacles = Obstacles(screen, screenwidth, screenheight)
		self.upcomingObstacles = self.obstacles.obstacles
		self.score = 0
		self.gen = n

	def checkForEnd(self):
		for bot in self.bots.bots:
			bot_rect = bot.box.rect	
			if (bot_rect.y > self.screenheight or bot_rect.y < -200):
				bot.die()

			for obstacle in self.obstacles.obstacles:
				obs_upper = obstacle.rect_upper
				obs_lower = obstacle.rect_lower

				if (bot_rect.colliderect(obs_lower) or bot_rect.colliderect(obs_upper)):
					bot.die()

		for bot in self.bots.bots:
			if not bot.dead:
				return False
		
		return True
	
	def updatescore(self):
		self.upcomingObstacles = []
		for obstacle in self.obstacles.obstacles:
			obs_edge = obstacle.rect_upper.right
			if (obs_edge < self.bots.left):
				if not obstacle.ScoreLogged:
					self.score += 1
					obstacle.pass_obstacle()
			else:
				self.upcomingObstacles.append(obstacle)

	

		largeFont = pygame.font.SysFont('comicasans', 30)
		text = largeFont.render(f'Generation: {self.gen} Score: ' + str(self.score), 1, (255,255,255))
		self.screen.blit(text, (700, 10))

	def update(self):
		self.obstacles.update()
		#self.bot.perceive(self.upcomingObstacles)
		self.bots.update(self.upcomingObstacles)
		self.updatescore()