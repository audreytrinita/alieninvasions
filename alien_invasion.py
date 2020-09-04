import sys

from time import sleep

import pygame

from settings import Settings

from game_stats import GameStats

from scoreboard import Scoreboard

from button import Button

from hs_label import label

from level_label import lv_label

from ship import Ship 

from bullet import Bullet 

from mediumlevel_button import medlevel

from alien import Alien

class AlienInvasion:

	def __init__(self):
		pygame.init()
		self.game_setting = Settings()

		self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
		self.game_setting.screen_width= self.screen.get_rect().width
		self.game_setting.screen_height= self.screen.get_rect().height


		#create an instance to store game statistic
		self.stats= GameStats(self) #baru 8/18

		#self.screen = pygame.display.set_mode((self.game_setting.screen_width, self.game_setting.screen_height))

		self.ship = Ship(self)

		self.bullets = pygame.sprite.Group() #bikin self.bullet ini menjadi SEBUAH GROUP KOSONG
		self.aliens = pygame.sprite.Group()

		self.create_fleet()

		#make button
		self.play_button = Button(self, "Play")
		self.med_button = medlevel(self,"Medium")

		#score board
		self.sb = Scoreboard(self)
		self.hs = label(self,"high score")
		self.lv = lv_label(self,"Lv.")

	def run(self):
		while True:
			self.check_events()

			if self.stats.game_active:
				self.ship.update()
				self.update_aliens()
				self.update_bullet()
				
			self.update_screen()
			

	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self.check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self.check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self.check_play_button(mouse_pos)

	def check_play_button(self,mouse_pos):
		'''start a new game when player click Play'''
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		medium_clicked = self.med_button.rect.collidepoint(mouse_pos)
		#(bf) self.play_button.rect.collidepoint(mouse_pos):
		if button_clicked and not self.stats.game_active: #and game_active lagi Mati/False:
			#reset the game statics
			self.game_setting.dynamic_settings()
			self.stats.game_active= True 

			self.stats.reset_stats()
			self.sb.prep_score()

			#remove any remaining aliens and bullets
			self.aliens.empty()
			self.bullets.empty()

			#create new fleet
			self.create_fleet()
			self.ship.center_ship()

			#re-set score
			self.sb.prep_score()
			self.sb.prep_level()
			self.sb.prep_ships()

		elif medium_clicked and not self.stats.game_active:
			self.game_setting.increase_speed()
			self.stats.game_active = True

		#hide the mouse cursor
		pygame.mouse.set_visible(False)

	def play_game(self):
		self.stats.reset_stats()
		self.stats.game_active = True

		#delete remaining obj
		self.aliens.empty()
		self.bullets.empty()

		#re-new obj
		self.create_fleet()
		self.ship.center_ship()

		#hide the cursor
		pygame.mouse.set_visible(False)

	def check_keydown_events(self,event):
			if event.key == pygame.K_RIGHT:
				self.ship.moving_right= True
			elif event.key == pygame.K_LEFT:
				self.ship.moving_left= True
			elif event.key ==pygame.K_q:
				sys.exit()
			elif event.key == pygame.K_SPACE: 
				self.fire_bullet()
			elif event.key == pygame.K_p:
				self.play_game()

	def check_keyup_events(self,event):
			if event.key == pygame.K_RIGHT:
				self.ship.moving_right = False
			elif event.key == pygame.K_LEFT:
				self.ship.moving_left = False


	def fire_bullet(self):
		'''create a new bullet and add it to the bullets group'''
		if len(self.bullets) < self.game_setting.bullet_allowed:
			new_bullet= Bullet(self) #manggil bullet class and its instances
			self.bullets.add(new_bullet) #masukin the bullet ke grup self.bullets diatas


	def update_bullet(self): 
		'''update position of bullets and delete the old bullet'''
		self.bullets.update() #manggil update() sbg petunjuk arah pergerakan y

		#delete the bullet that have disappeared
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0: #jika bullet bagian bawah udh di angka 0:
				self.bullets.remove(bullet)
		print(len(self.bullets))

		self.check_alien_bullet_collisions()

	def check_alien_bullet_collisions(self):
		#check any bullet that have hit aliens, if so, remove the alien and the bullet
		collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True) #baru 8/18

		if not self.aliens:
			#destroy existing bullets and create new fleet
			self.bullets.empty()
			self.create_fleet()
			self.game_setting.increase_speed()

			#increase level
			self.stats.level += 1
			self.sb.prep_level()

		if collisions:
			for aliens in collisions.values():
				self.stats.score_board += self.game_setting.alien_points * len(aliens)
			#self.stats.score_board += self.game_setting.alien_points
			self.sb.prep_score()
			self.sb.check_high_score()

	def update_aliens(self): 
		'''check if the fleet is at an edge, then update the positions of all aliens in the fleet'''
		self.check_fleet_edges()
		self.aliens.update() #ambil dr aliens.group()

		#look for alien-ship collisions
		if pygame.sprite.spritecollideany(self.ship, self.aliens): #baru 8/18
			self.ship_hit()
			print('Ship hit!!!')

		#look for aliens hitting screen bottom
		self.check_aliens_bottom()

	def check_aliens_bottom(self):
		screen_rect = self.screen.get_rect()

		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
				#treat same as if the ship got hit
				self.ship_hit()
				break

	def ship_hit(self): #baru 8/18
		'''respond to the ship being hit by alien'''
		if self.stats.ships_left > 0:
			#decrement ship left and update score board
			self.stats.ships_left -= 1
			self.sb.prep_ships()
		
			#remove all of remaining aliens and bullets
			self.aliens.empty()
			self.bullets.empty()
			

			#create a new fleet and center the ship
			self.create_fleet()
			self.ship.center_ship()

			#pause
			sleep(0.5)
			
		else:
			self.stats.game_active = False
			pygame.mouse.set_visible(True)


	def create_fleet(self):
		'''create the fleet(armada) of aliens'''
		#(bf)alien = Alien(self) #bikin alien untuk di tampilkan
		#(bf)self.aliens.add(alien) #masukin ke grup self.aliens

		#create an alien and find the number of aliens in a row
		#x coor
		alien= Alien(self)
		alien_width, alien_height= alien.rect.size 
		available_space_x= self.game_setting.screen_width - (2 * alien_width) #menghitung sisa layar sblh kanan
		number_aliens_x = available_space_x // (2 * alien_width) #menghitung berapa biji alien yang akan tertampil

		#y coor
		ship_height=self.ship.rect.height
		available_space_y= (self.game_setting.screen_height - (3 * alien_height) - ship_height)
		number_rows= available_space_y // (2 * alien_height)

		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				self.create_alien(alien_number, row_number)


	def create_alien(self,alien_number,row_number):
			#create an alien and place it in the row
			alien= Alien(self)
			alien_width, alien_height= alien.rect.size
			alien.x= alien_width + 2 * alien_width * alien_number
			alien.rect.x= alien.x

			alien.rect.y= alien_height + 2 * alien_height * row_number
			self.aliens.add(alien)

	def check_fleet_edges(self): #baru 8/15, langkah pertama
		'''respond appropriately if any aliens have reached an edge'''
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self.change_fleet_direction()
				break

	def change_fleet_direction(self): #baru 8/15
		'''drop the entire fleet and change the fleet's direction'''
		for alien in self.aliens.sprites():
			alien.rect.y += self.game_setting.fleet_drop_speed
		self.game_setting.fleet_direction *= -1 #// (*) kalo edgenya di arah lain(kiri, krn yg di set kanan), maka = -1


	def update_screen(self): #yang tertempel dilayar, selalu call di terkahir
		self.screen.fill(self.game_setting.bg_color)
		self.ship.blitme()

		for bullet in self.bullets.sprites():
			bullet.draw_bullet() #mengeluarkan BENTUK BULLET

		self.aliens.draw(self.screen)

		#draw score
		self.sb.show_score()
		self.hs.draw_label()
		self.lv.draw_label()

		#draw play button if the fame is inactive
		if not self.stats.game_active:
			self.play_button.draw_button()
			self.med_button.draw_button()

		pygame.display.flip()



if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run()