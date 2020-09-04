import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
	'''a class to make a sindle alien in the fleet'''
	def __init__(self,ai_game):

		super().__init__()
		self.screen = ai_game.screen
		self.alien_setting =  ai_game.game_setting

		#load the alien's image
		self.image= pygame.image.load('C:/Dev/python_game/alien.png')
		self.rect= self.image.get_rect()

		#start each new alien in top left
		self.rect.x = self.rect.width #jarak antara 1 dgn yg lainnya = gambar punya lebar
		self.rect.y = self.rect.height # 		-----||-----		 = gambar punya tinggi	

		#store alien's exact horizontal position
		self.x = float(self.rect.x) #unknown self.rect.width's value

	def check_edges(self): #baru 8/15
		'''return true if alien is at edge of screen'''
		screen_rect = self.screen.get_rect()

		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True

	def update(self): #baru 8/15
		'''move the alien to the right'''
		#(bf) self.x += self.alien_setting.alien_speed
		self.x += (self.alien_setting.alien_speed * self.alien_setting.fleet_direction)
		self.rect.x = self.x

