import pygame
from pygame.sprite import Sprite 

class Bullet(Sprite): #sprite= super class
	'''a class to manage bullet fired from the ship'''

	def __init__(self,ai_game):
		'''create a bullet object at the ship's current position'''
		super().__init__()
		self.screen = ai_game.screen
		self.bullet_setting= ai_game.game_setting
		self.color= self.bullet_setting.bullet_color

		#create a bullet rect at (0,0) and then set correct position
		self.rect= pygame.Rect(0,0,self.bullet_setting.bullet_width,self.bullet_setting.bullet_height) #membuat bentuk bullet dgn bentuk rect(angle),& posisi semenatara (0,0)
		self.rect.midtop = ai_game.ship.rect.midtop #ganti pposisi

		#store the bullet's positions as a decimal value
		self.y = float(self.rect.y)

	def update(self): #pergerakan bullet
		'''move the bullet up the screen'''
		#update the decimal position of the bullet'''
		self.y -= self.bullet_setting.bullet_speed #(-=) menyuruh si bullet melalui sumbu y untuk mengurangi(-), agar peluru gerak ke atas
		self.rect.y = self.y

	def draw_bullet(self): #munculkan bullet
		'''draw the bullet to the screen'''
		pygame.draw.rect(self.screen, self.color, self.rect) #draw.rect() mengisi bullet's behaviour