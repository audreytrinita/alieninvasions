import pygame.font

class lv_label:
	def __init__(self,ai_game,msg):
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.label_settings = ai_game.game_setting

		#button props
		self.width, self.height = 10,20
		self.button_color = self.label_settings.bg_color
		self.text_color = (255,125,2)
		self.font = pygame.font.SysFont(None,25)

		#location
		self.rect = pygame.Rect(0,0,self.width,self.height)
		self.rect.right = self.screen_rect.right - 75
		self.rect.y = self.screen_rect.y + 75

		self.prep_label(msg)

	def prep_label(self,msg):
		self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.right = self.screen_rect.right - 50
		self.msg_image_rect.y= self.screen_rect.y + 75
	def draw_label(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)