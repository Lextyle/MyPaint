from pygame.draw import line as draw_line
class Line():
	def __init__(self, x_1, y_1, x_2, y_2, color, brush_size):
		self.x_1 = x_1
		self.y_1 = y_1
		self.x_2 = x_2
		self.y_2 = y_2
		self.color = color
		self.brush_size = brush_size
	def draw(self, canvas):
		draw_line(canvas, self.color, (self.x_1, self.y_1), (self.x_2, self.y_2), self.brush_size)