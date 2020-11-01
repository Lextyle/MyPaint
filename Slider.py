from pygame.draw import rect as draw_rect, circle as draw_circle
from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION
class Slider():
	def __init__(self, x, y, width, color):
		self.x = x
		self.y = y
		self.width = width
		self.height = 10
		self.color = color
		self.circle_radius = self.height
		self.circle_x = self.x
		self.circle_y = self.y + self.height // 2
		self.change_value = False
		self.value = 0
	def update(self, event, toolbar_x):
		if event.type == MOUSEBUTTONDOWN:
			if event.pos[0] - toolbar_x in range(self.x, self.x + self.width + 1) and event.pos[1] - 75 in range(self.circle_y - self.circle_radius, self.circle_y + self.circle_radius + 1):
				self.change_value = True
		if event.type == MOUSEBUTTONUP:
			self.change_value = False
		if event.type == MOUSEMOTION:
			if self.change_value:
				if event.pos[0] - toolbar_x in range(self.x, self.x + self.width + 1):
					self.circle_x = event.pos[0] - toolbar_x
					self.value = self.circle_x - self.x
	def draw(self, toolbar):
		draw_rect(toolbar, self.color, (self.x, self.y, self.width, self.height))
		draw_circle(toolbar, (self.color[0] - 40, self.color[1] - 40, self.color[2] - 40), (self.circle_x, self.circle_y), self.circle_radius)