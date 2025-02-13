import pygame
import random
import time

pygame.init()





class Button:
	def __init__(self,
		id = None,
		x = 0,
		y = 0,
		dx = 50,
		dy = 50,
		mode='one_touch',
		border_size = 3,
		color_border = (100,100,100),
		color_border_covered = (210,80,80),
		color_border_selected = (255,0,0),
		color_fill = (255,255,255),
		color_fill_covered = (220,180,180),
		color_fill_selected = (255,140,140),
		text = '',
		icon = None,
		icon_covered = None,
		icon_selected = None,
		visible=True):

		if id == None:
			random.seed(time.time())
			id = str(random.randint(10000000,99999999))
		self.id = id
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.mode = mode
		self.border_size = border_size
		self.color_border = color_border
		self.color_border_covered = color_border_covered
		self.color_border_selected = color_border_selected
		self.color_fill = color_fill
		self.color_fill_covered = color_fill_covered
		self.color_fill_selected = color_fill_selected
		self.text = text

		self.icon = pygame.transform.scale(icon,(self.dx,self.dy))
		self.icon_selected = pygame.transform.scale(icon_selected,(self.dx,self.dy))
		self.icon_covered = pygame.transform.scale(icon_covered,(self.dx,self.dy))

		self.selected_left = False
		self.selected_right = False
		self.covered = False

		self.visible = visible

		


	def get_value(self):
		return self.selected_left, self.selected_right




	def blit(self, screen, mode='default'):
		scr = screen
		if mode == 'default':
			pygame.draw.rect(scr,self.color_fill,(self.x, self.y, self.dx, self.dy), 0)
			if self.icon != None:
				scr.blit(self.icon,(self.x,self.y))
			pygame.draw.rect(scr,self.color_border,(self.x, self.y, self.dx, self.dy), self.border_size)

		if mode == 'covered':
			pygame.draw.rect(scr,self.color_fill_covered,(self.x, self.y, self.dx, self.dy), 0)
			if self.icon_covered != None:
				scr.blit(self.icon_covered,(self.x,self.y))
			pygame.draw.rect(scr,self.color_border_covered,(self.x, self.y, self.dx, self.dy), self.border_size)

		if mode == 'selected':
			pygame.draw.rect(scr,self.color_fill_selected,(self.x, self.y, self.dx, self.dy), 0)
			if self.icon_selected != None:
				scr.blit(self.icon_selected,(self.x,self.y))
			pygame.draw.rect(scr,self.color_border_selected,(self.x, self.y, self.dx, self.dy), self.border_size)

		return scr
	
	def is_covered(self, mouse_x, mouse_y):
		return mouse_x > self.x and mouse_x < self.x + self.dx and mouse_y > self.y and mouse_y < self.y + self.dy




class Scale:
	def __init__(self,
		id = None,
		x = 0,
		y = 0,
		dx = 200,
		dy = 20,
		value=0,
		value_max=100,
		direction='right',
		no_border=False,
		border_size=3,
		color_border=(100,100,100),
		color_fill=(255,255,255),
		color_filled=(255,140,140),
		visible=True,

		):

		if id == None:
			random.seed(time.time())
			id = str(random.randint(10000000,99999999))
		self.id = id

		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.value = value
		self.value_max = value_max
		self.direction = direction
		self.no_border = no_border
		self.border_size = border_size
		self.color_border = color_border
		self.color_fill = color_fill
		self.color_filled = color_filled

		self.visible = visible


	def get_value(self):
		return self.value


	def set_value(self, value):
		self.value = value
		if self.value > self.value_max:
			self.value = self.value_max
		elif self.value < 0:
			self.value = 0

		return self.value


	def blit(self, screen):
		scr = screen
		pygame.draw.rect(scr,self.color_fill,(self.x, self.y, self.dx, self.dy), 0)


		k_x = 1
		k_y = 1

		add_y = 0
		add_x = 0

		k = (self.value/self.value_max)

		if self.direction == 'right':
			k_x = k
		elif self.direction == 'left':
			k_x = k
			add_x = self.dx-self.dx*k
		elif self.direction == 'up':
			k_y = k
			add_y = self.dy-self.dy*k
		elif self.direction == 'down':
			k_y = k


		pygame.draw.rect(scr,self.color_filled,(self.x + add_x, self.y + add_y, self.dx*k_x, self.dy*k_y), 0)

		if not self.no_border:
			pygame.draw.rect(scr,self.color_border,(self.x, self.y, self.dx, self.dy), self.border_size)

		return scr



class Slider:
	def __init__(self,
		id = None,
		x = 0,
		y = 0,
		dx = 200,
		dy = 20,
		value=0,
		value_max=100,
		direction='right',
		no_border=False,
		border_size=3,
		circle_size=20,
		color_border=(100,100,100),
		color_fill=(255,255,255),
		color_filled=(255,140,140),
		color_circle=(255,90,90),
		color_circle_covered=(255,60,60),
		color_circle_selected=(255,0,0),
		visible=True


		):

		if id == None:
			random.seed(time.time())
			id = str(random.randint(10000000,99999999))
		self.id = id

		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.value = value
		self.value_max = value_max
		self.direction = direction
		self.no_border = no_border
		self.border_size = border_size
		self.circle_size = circle_size
		self.color_border = color_border
		self.color_fill = color_fill
		self.color_filled = color_filled
		self.color_circle = color_circle
		self.color_circle_covered = color_circle_covered
		self.color_circle_selected = color_circle_selected

		self.selected = False
		self.covered = False

		self.visible = visible


	def get_value(self):
		return self.value


	def add_value(self, d_value):
		self.value += d_value
		if self.value > self.value_max:
			self.value = self. value_max
		if self.value < 0:
			self.value = 0

	def set_value(self, value):
		self.value = value
		if self.value > self.value_max:
			self.value = self.value_max
		elif self.value < 0:
			self.value = 0

		return self.value


	def blit(self, screen, mode):
		scr = screen
		pygame.draw.rect(scr,self.color_fill,(self.x, self.y, self.dx, self.dy), 0)


		self.k_x = 1
		self.k_y = 1

		self.add_y = 0

		self.add_x_circle = 0
		self.add_y_circle = 0

		self.k = (self.value/self.value_max)

		if self.direction == 'right':
			self.k_x = self.k
			self.add_x_circle = self.dx*self.k
			self.add_y_circle = self.dy//2
		elif self.direction == 'up':
			self.k_y = self.k
			self.add_y = self.dy-self.dy*self.k
			self.add_x_circle = self.dx//2
			self.add_y_circle = self.dy-self.dy*self.k


		pygame.draw.rect(scr,self.color_filled,(self.x, self.y+self.add_y, self.dx*self.k_x, self.dy*self.k_y), 0)

		if not self.no_border:
			pygame.draw.rect(scr,self.color_border,(self.x, self.y, self.dx, self.dy), self.border_size)



		
		if mode == 'default':
			pygame.draw.circle(scr,self.color_circle,(self.x+self.add_x_circle, self.y+self.add_y_circle), self.circle_size)
			
			
		if mode == 'covered':
			pygame.draw.circle(scr,self.color_circle_covered,(self.x+self.add_x_circle, self.y+self.add_y_circle), self.circle_size)
			
			
		if mode == 'selected':
			pygame.draw.circle(scr,self.color_circle_selected,(self.x+self.add_x_circle, self.y+self.add_y_circle), self.circle_size)



		return scr
	
	


	def is_covered(self, mouse_x, mouse_y):
		
		return pow((mouse_x-self.x-self.add_x_circle)**2 + (mouse_y-self.y-self.add_y_circle)**2, 0.5) < self.circle_size


class Text:
	def __init__(self,
		id=None,
		x=0,
		y=0,
		font_size=24,
		color=(0,0,0),
		value='',
		font=None,
		visible=True
		):


		if id == None:
			random.seed(time.time())
			id = str(random.randint(10000000,99999999))
		self.id = id

		self.x = x
		self.y = y
		self.font_size = font_size
		self.color = color
		self.value = value
		self.font = font

		self.fontt = [0]*128
		for i in range(2,128):
			self.fontt[i] = pygame.font.Font(font,i)


		self.visible = visible




	def get_value(self):
		return self.value

	def set_value(self, value):
		self.value = value

		return self.value


	def blit(self, screen):
		scr = screen

		out = self.fontt[self.font_size].render(str(self.value), 1, self.color)
		scr.blit(out,(self.x, self.y))

		return scr




class Controls:
	def __init__(self, objs=dict()):
		self.objs = objs

		self.mouse_touching_l = False
		self.mouse_touching_r = False

		self.mouse_touching_l_last = False
		self.mouse_touching_r_last = False

		self.mouse_touching_l_lock = False
		self.mouse_touching_r_lock = False

		self.mouse_x = 0
		self.mouse_y = 0

		self.mouse_x_l = 0
		self.mouse_y_l = 0


	def add(self, objs):
		for obj in objs:
			self.objs[obj.id] = obj

	def get_value(self, obj):
		return self.objs[obj.id].get_value()


	def delete(self, obj):
		del self.objs[obj.id]

	def set_value(self, obj, value):
		return self.objs[obj.id].set_value(value)

	def show(self, obj):
		self.objs[obj.id].visible = True

	def hide(self, obj):
		self.objs[obj.id].visible = False



	def do_logic(self):
		for obj_id, obj in self.objs.items():
			if obj.visible:
				if type(self.objs[obj_id]) == Button:
					if self.objs[obj_id].mode == 'one_touch':
						self.objs[obj_id].selected_left = False
						self.objs[obj_id].selected_right = False

					if self.objs[obj_id].selected_left or self.objs[obj_id].selected_right:
						self.scr = self.objs[obj_id].blit(self.scr, 'selected')
					elif self.objs[obj_id].covered:
						self.scr = self.objs[obj_id].blit(self.scr, 'covered')
					else:
						self.scr = self.objs[obj_id].blit(self.scr, 'default')

					if self.objs[obj_id].is_covered(self.mouse_x, self.mouse_y):
						self.objs[obj_id].covered = True
						if self.mouse_touching_l:
							if self.objs[obj_id].mode == 'push':
									self.objs[obj_id].selected_left = True
							elif self.objs[obj_id].mode == 'toggle':
								
								if not self.mouse_touching_l_lock:
									self.objs[obj_id].selected_left ^= 1
									self.mouse_touching_l_lock = True
								self.mouse_touching_l_last = self.mouse_touching_l

							elif self.objs[obj_id].mode == 'one_touch':
								if not self.mouse_touching_l_lock:
									self.objs[obj_id].selected_left = True
									self.mouse_touching_l_lock = True
								self.mouse_touching_l_last = self.mouse_touching_l
								
						else:
							if self.mouse_touching_l_last != self.mouse_touching_l:
								self.mouse_touching_l_lock = False
							if self.objs[obj_id].mode == 'push':
								self.objs[obj_id].selected_left = False



						if self.mouse_touching_r:
							if self.objs[obj_id].mode == 'push':
									self.objs[obj_id].selected_right = True
							elif self.objs[obj_id].mode == 'toggle':
								
								if not self.mouse_touching_r_lock:
									self.objs[obj_id].selected_right ^= 1
									self.mouse_touching_r_lock = True
								self.mouse_touching_r_last = self.mouse_touching_r

							elif self.objs[obj_id].mode == 'one_touch':
								if not self.mouse_touching_r_lock:
									self.objs[obj_id].selected_right = True
									self.mouse_touching_r_lock = True
								self.mouse_touching_r_last = self.mouse_touching_r
								
						else:
							if self.mouse_touching_r_last != self.mouse_touching_r:
								self.mouse_touching_r_lock = False
							if self.objs[obj_id].mode == 'push':
								self.objs[obj_id].selected_right = False

					else:
						self.objs[obj_id].covered = False
						if not self.objs[obj_id].mode == 'toggle':
							self.objs[obj_id].selected_left = False
							self.objs[obj_id].selected_right = False



				elif type(self.objs[obj_id]) == Scale:
					self.scr = self.objs[obj_id].blit(self.scr)

				elif type(self.objs[obj_id]) == Slider:
					if self.objs[obj_id].selected:
						self.scr = self.objs[obj_id].blit(self.scr, 'selected')
					elif self.objs[obj_id].covered:
						self.scr = self.objs[obj_id].blit(self.scr, 'covered')
					else:
						self.scr = self.objs[obj_id].blit(self.scr, 'default')


					if self.objs[obj_id].is_covered(self.mouse_x, self.mouse_y):
						self.objs[obj_id].covered = True
						if self.mouse_touching_l:
							self.objs[obj_id].selected = True
						else:
							self.objs[obj_id].selected = False

					else:
						self.objs[obj_id].covered = False

					if self.mouse_touching_l and self.objs[obj_id].selected:
						if self.objs[obj_id].direction == 'right':
							add_value = (self.mouse_x-self.mouse_x_l)*(self.objs[obj_id].value_max/self.objs[obj_id].dx)
						elif  self.objs[obj_id].direction == 'up':
							add_value = -(self.mouse_y-self.mouse_y_l)*(self.objs[obj_id].value_max/self.objs[obj_id].dy)
						self.objs[obj_id].add_value(add_value)
					else:
						self.objs[obj_id].selected = False

				elif type(self.objs[obj_id]) == Text:
					self.scr = self.objs[obj_id].blit(self.scr)





		

				
	



	def render(self, screen, mouse_touching_l, mouse_touching_r):
		self.mouse_touching_l = mouse_touching_l
		self.mouse_touching_r = mouse_touching_r

		action = None
		self.scr = screen

		mouse_pos = pygame.mouse.get_pos()

		self.mouse_x_l = self.mouse_x
		self.mouse_y_l = self.mouse_y

		self.mouse_x = mouse_pos[0]
		self.mouse_y = mouse_pos[1]



		self.do_logic()
		pygame.display.flip()
			

		return self.scr

		



		



