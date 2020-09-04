import pygame.font

class label:
	def __init__(self,ai_game,msg):
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.label_settings = ai_game.game_setting

		#button props
		self.width, self.height = 10,20
		self.button_color = self.label_settings.bg_color
		self.text_color = (255,0,0)
		self.font = pygame.font.SysFont(None,25)

		#location
		self.rect = pygame.Rect(0,0,self.width,self.height)
		self.rect.centerx = self.screen_rect.centerx
		self.rect.top = self.screen_rect.top

		self.prep_label(msg)

	def prep_label(self,msg):
		self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.centerx = self.screen_rect.centerx
		self.msg_image_rect.top = self.screen_rect.top

	def draw_label(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)
