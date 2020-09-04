import pygame.font

class medlevel:
	def __init__(self,ai_game,msg):
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()

		#button props
		self.width, self.height = 100,50
		self.button_color = (255,247,0)
		self.text_color = (0,0,0)
		self.font = pygame.font.SysFont(None,25)

		#location
		self.rect = pygame.Rect(0,0,self.width,self.height)
		self.rect.x = 1250
		self.rect.y = 10

		self.prep_button(msg)

	def prep_button(self,msg):
		self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.x = 1270
		self.msg_image_rect.y = 25

	def draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)
