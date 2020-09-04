class GameStats:
	'''track statistic for alien invasions'''
	def __init__(self, ai_game):
		'''initialize statistic'''
		self.stat_settings =  ai_game.game_setting
		self.reset_stats()
		self.game_active= False

		#high score should never be reset
		self.high_score = 0

	def reset_stats(self):
		'''initialize statistic that can change during the game'''
		self.ships_left = self.stat_settings.ship_limit
		self.score_board = 0
		self.level = 1