import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
	def __init__(self,ai_game):
		self.ai_game = ai_game
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.score_settings = ai_game.game_setting
		self.stats = ai_game.stats

		#board props
		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None,40)

		#prep board
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		#jadiin image dulu
		rounded_score = round(self.stats.score_board, -1)
		score_str = "{:,}".format(rounded_score)
		#score_str = str(self.stats.score_board) #angkanya jadiin string
		self.score_image = self.font.render(score_str, True, self.text_color, self.score_settings.bg_color) #self.text_color = warna text itu self.text_color ;; self.score_settings.bg_color = bg color nya sama kek settings.bg_color
		
		#location
		self.score_rect = self.score_image.get_rect()
		self.score_rect.left = self.screen_rect.left + 20
		self.score_rect.top = 20

	def check_high_score(self):
		'''check if there is a new score'''
		if self.stats.score_board > self.stats.high_score:
			self.stats.high_score = self.stats.score_board
			self.prep_high_score()

	def prep_high_score(self):
		'''bikin image lg'''
		high_score= round(self.stats.score_board, -1)
		high_score_str = "{:,}".format(high_score)

		self.high_score_img = self.font.render(high_score_str, True, self.text_color, self.score_settings.bg_color)
		#lokasi
		self.high_score_rect = self.high_score_img.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def prep_level(self):
		#jadiin string dl
		level_str = str(self.stats.level)
		self.level_img= self.font.render(level_str,True,self.text_color,self.score_settings.bg_color)

		#lokasi
		self.level_img_rect = self.level_img.get_rect()
		self.level_img_rect.right = self.screen_rect.right - 20
		self.level_img_rect.top = self.screen_rect.top + 70

	def prep_ships(self):
		#show how many ships are left
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_game)
			ship.rect.right = self.screen_rect.right
			ship.rect.y = 200 + ship_number * ship.rect.width
			self.ships.add(ship)

	def show_score(self):
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_img, self.high_score_rect)
		self.screen.blit(self.level_img, self.level_img_rect)
		self.ships.draw(self.screen)