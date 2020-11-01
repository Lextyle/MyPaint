from pygame.draw import circle as draw_circle
class Circle():
	def __init__(self, x, y, brush_size, color):
		self.x = x
		self.y = y
		self.brush_size = brush_size
		self.color = color
	def draw(self, canvas):
		draw_circle(canvas, self.color, (self.x, self.y), self.brush_size)