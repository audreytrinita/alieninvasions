import pygame

class Settings:
	def __init__(self):
		#ship settings
		self.screen_width = 1000 
		self.screen_height = 650
		self.bg_color = (230,230,230)
		self.ship_limit = 3

		#bullet settings
		self.bullet_width= 200
		self.bullet_height= 15
		self.bullet_color= (60,60,60)
		self.bullet_allowed= 3

		#aliens speed , baru 8/15
		self.fleet_drop_speed = 60 #kecepatan fleet alien turun kebawah
			#fleet_direction of 1 go to the right; -1 go to the left

		#how quickly the game speeds up
		self.speedup_scale = 1.1

		#how qiuckly the alien point increase
		self.score_scale = 1.5

		self.dynamic_settings()


	def dynamic_settings(self): #settings awal mula semua object
		self.ship_speed = 5.5
		self.bullet_speed = 5.5
		self.alien_speed = 1.0

		#fleet direction
		self.fleet_direction = 1

		#dynamic score
		self.alien_points= 50

	def increase_speed(self):
		"""increase the speed settings and alien point values"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed + self.speedup_scale

		self.alien_points = int(self.alien_points * self.score_scale)