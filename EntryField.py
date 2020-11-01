from pygame import Surface, KEYDOWN, K_BACKSPACE
class EntryField():
	def __init__(self, x, y, width, height, font, color, text_color):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.surface = Surface((self.width, self.height))
		self.font = font
		self.color = color
		self.text_color = text_color
		self.text = ""
	def update(self, event):
		if event.type == KEYDOWN:
			if event.key == K_BACKSPACE:
				self.text = self.text[0:-1]
			else:
				self.text += event.unicode
	def draw(self, window):
		self.surface.fill((self.color))
		text_render = self.font.render(self.text, True, self.text_color)
		if text_render.get_width() > self.width:
			self.surface.blit(text_render, ((text_render.get_width() - self.width) * -1, self.height - self.font.render("f", True, self.text_color).get_height()))
		else:
			self.surface.blit(text_render, (0, self.height - self.font.render("f", True, self.text_color).get_height()))
		window.blit(self.surface, (self.x, self.y))