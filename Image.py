from pygame.image import load as load_image
class Image():
	def __init__(self, x, y, image):
		self.x = x
		self.y = y 
		self.image = image
	def draw(self, window):
		window.blit(self.image, (self.x, self.y))