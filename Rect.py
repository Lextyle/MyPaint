from pygame.draw import rect as draw_rect
class Rect():
	def __init__(self, x, y, brush_size, color):
		self.x = x
		self.y = y
		self.brush_size = brush_size
		self.color = color
	def draw(self, canvas):
		draw_rect(canvas, self.color, (self.x, self.y, self.brush_size, self.brush_size))