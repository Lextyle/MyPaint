import pygame
from pyautogui import size, screenshot
from Button import *
from Slider import *
from Rect import *
from EntryField import *
from Image import *
from os import listdir, mkdir
try:
	listdir("Pictures")
except:
	mkdir("Pictures")
pygame.init()
# VARIABLES
window_width = size()[0]
window_height = size()[1]
window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
def load():
	black_surface = pygame.Surface((window_width, window_height))
	black_surface.fill((0, 0, 0))
	black_surface.set_alpha(150)
	window.blit(black_surface, (0, 0))
	max_size = [500, 250]
	size = [0, 0]
	font = pygame.font.Font("SFPixelate.ttf", 20)
	buttons = []
	filenames = listdir("Pictures")
	image_width = max_size[0] // 5
	letter_example = font.render("Q", True, (0, 0, 0))
	image_height = 50
	x = 10
	y = 0
	for filename in filenames:
		if filename[-4:len(filename)] == ".png" or filename[-4:len(filename)] == ".jpg":
			image = pygame.transform.scale(pygame.image.load(f"Pictures\{filename}"), (image_width, image_height))
			buttons.append([pygame.image.load(f"Pictures\{filename}"), font.render(filename, True, (0, 0, 0)), pygame.Surface((image_width, image_height)), (x, y), Button(0, 0, image, image, (window_width // 2 - max_size[0] // 2) + x, (window_height // 2 - max_size[1] // 2) + y)])
			if buttons[-1][1].get_width() > image_width:
				buttons[-1][1] = font.render(filename[0:image_width // letter_example.get_width() - 3] + "...", True, (0, 0, 0))
			x += image_width + 10
			if x + image_width > max_size[0]:
				x = 10
				y += image_height + 10
	while True:
		surface = pygame.Surface(size)
		surface.fill((60, 60, 60))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			for button in buttons:
				button[-1].update(event)
			if event.type == pygame.MOUSEBUTTONDOWN:
				if not (event.pos[0] in range(window_width // 2 - surface.get_width() // 2, (window_width // 2 - surface.get_width() // 2) + surface.get_width()) and event.pos[1] in range(window_height // 2 - surface.get_height() // 2, (window_height // 2 - surface.get_height() // 2) + surface.get_height())):
					return "DON'T LOAD"
		size[0] += 6
		size[1] += 3
		if size[0] > max_size[0]:
			size[0] = max_size[0]
		if size[1] > max_size[1]:
			size[1] = max_size[1]
		for button in buttons:
			if button[-1].pressed:
				return button[0]
			button[-1].draw(button[2])
			button[2].blit(button[1], (0, button[-1].image.get_height() // 2 - button[1].get_height() // 2))
			surface.blit(button[2], (button[3][0], button[3][1]))
		window.blit(surface, (window_width // 2 - surface.get_width() // 2, window_height // 2 - surface.get_height() // 2))
		pygame.display.flip()
def save(canvas):
	black_surface = pygame.Surface((window_width, window_height))
	black_surface.fill((0, 0, 0))
	black_surface.set_alpha(150)
	window.blit(black_surface, (0, 0))
	max_size = [500, 250]
	size = [0, 0]
	font = pygame.font.Font("SFPixelate.ttf", 50)
	filename_entry_filed = EntryField(max_size[0] // 2 - 250 // 2, 50, 250, 62, font, (30, 30, 30), (255, 255, 255))
	cancel_button_image = pygame.transform.scale(pygame.image.load(r"images\cancel_button_image.png"), (pygame.image.load(r"images\cancel_button_image.png").get_width() * 2, pygame.image.load(r"images\cancel_button_image.png").get_height() * 2))
	save_button_image = pygame.transform.scale(pygame.image.load(r"images\save_button_image.png"), (pygame.image.load(r"images\save_button_image.png").get_width() * 2, pygame.image.load(r"images\save_button_image.png").get_height() * 2))
	cancel_button = Button(max_size[0] // 2 + 10, filename_entry_filed.y + filename_entry_filed.surface.get_height() + 50, cancel_button_image, cancel_button_image, window_width // 2 - max_size[0] // 2, window_height // 2 - max_size[1] // 2) 
	save_button = Button((max_size[0] // 2 - save_button_image.get_width()) - 10, filename_entry_filed.y + filename_entry_filed.surface.get_height() + 50, save_button_image, save_button_image, window_width // 2 - max_size[0] // 2, window_height // 2 - max_size[1] // 2)
	while True:
		surface = pygame.Surface(size)
		filename_entry_filed.x, filename_entry_filed.y = size[0] // 2 - 250 // 2, 50
		cancel_button.x, cancel_button.y = size[0] // 2 + 10, filename_entry_filed.y + filename_entry_filed.surface.get_height() + 50
		save_button.x, save_button.y = (size[0] // 2 - save_button_image.get_width()) - 10, filename_entry_filed.y + filename_entry_filed.surface.get_height() + 50
		surface.fill((60, 60, 60))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			filename_entry_filed.update(event)
			cancel_button.update(event)
			save_button.update(event)
		if cancel_button.pressed:
			break
		if save_button.pressed:
			if filename_entry_filed.text[-4:len(filename_entry_filed.text)] == ".png" or filename_entry_filed.text[-4:len(filename_entry_filed.text)] == ".jpg":
				pygame.image.save(canvas, f"Pictures\{filename_entry_filed.text}")
			break
		size[0] += 6
		size[1] += 3
		if size[0] > max_size[0]:
			size[0] = max_size[0]
		if size[1] > max_size[1]:
			size[1] = max_size[1]
		filename_entry_filed.draw(surface)
		cancel_button.draw(surface)
		save_button.draw(surface)
		window.blit(surface, (window_width // 2 - surface.get_width() // 2, window_height // 2 - surface.get_height() // 2))
		pygame.display.flip()
toolbar_width = 300
toolbar_height = window_height - 75
toolbar = pygame.Surface((toolbar_width, toolbar_height))
canvas_x = 0
canvas_y = 75
canvas = pygame.Surface((window_width - toolbar_width, toolbar_height))
brush_size = 10
color = [0, 0, 0]
draw = False
rects = []
last_rects_num = 0
font = pygame.font.Font("SFPixelate.ttf", 20)
save_button_image = pygame.image.load(r"images\save_button_image.png")
load_button_image = pygame.image.load(r"images\load_button_image.png")
r_slider = Slider((toolbar_width // 2 - 255 // 2), 40, 255, (200, 40, 40))
g_slider = Slider((toolbar_width // 2 - 255 // 2), r_slider.circle_y + r_slider.circle_radius + 10, 255, (40, 200, 40))
b_slider = Slider((toolbar_width // 2 - 255 // 2), g_slider.circle_y + g_slider.circle_radius + 10, 255, (40, 40, 200))
brush_size_slider = Slider((toolbar_width // 2 - 100 // 2), ((b_slider.circle_y +  b_slider.circle_radius + 10) + font.render(f"{color}", True, (255, 255, 255)).get_height() + 60) + font.render(f"Brush Size", True, (255, 255, 255)).get_height() + 5, 100, (150, 150, 150))
all_versions_of_canvas = [rects.copy()]
save_button = Button(0, 75 - save_button_image.get_height(), save_button_image, save_button_image, 0, 0)
load_button = Button(save_button_image.get_width() + 10, 75 - load_button_image.get_height(), load_button_image, load_button_image, 0, 0)
# GAME LOOP
while True:
	window.fill((60, 60, 60))
	# GETING INPUTS
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_z:
				if len(all_versions_of_canvas) > 1:
					rects = all_versions_of_canvas[-1]
					all_versions_of_canvas = all_versions_of_canvas[0:-1]
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if event.pos[0] in range(canvas_x, canvas_x + canvas.get_width()) and event.pos[1] in range(canvas_y, canvas_y + canvas.get_height()):
					draw = True
					all_versions_of_canvas.append(rects.copy())
			if event.button == 2:
				screenshot_image = screenshot()
				color = screenshot_image.getpixel(event.pos)
				r_slider.circle_x = color[0] + r_slider.x
				g_slider.circle_x = color[1] + r_slider.x
				b_slider.circle_x = color[2] + r_slider.x
				r_slider.value = color[0]
				g_slider.value = color[1]
				b_slider.value = color[2]
		if event.type == pygame.MOUSEBUTTONUP:
			draw = False
			last_rects_num = 0
		if event.type == pygame.MOUSEMOTION:
			if draw:
				rects.append(Rect((event.pos[0] - canvas_x) - (event.pos[0] - canvas_x) % brush_size, (event.pos[1] - canvas_y) - (event.pos[1] - canvas_y) % brush_size, brush_size, color))
				last_rects_num += 1
		r_slider.update(event, canvas_x + canvas.get_width())
		g_slider.update(event, canvas_x + canvas.get_width())
		b_slider.update(event, canvas_x + canvas.get_width())
		brush_size_slider.update(event, canvas_x + canvas.get_width())
		save_button.update(event)
		load_button.update(event)
	canvas.fill((255, 255, 255))
	toolbar.fill((30, 30, 30))
	color = [r_slider.value, g_slider.value, b_slider.value]
	brush_size = brush_size_slider.value + 10
	# DRAW
	for rect in rects:
		rect.draw(canvas)
	rgb_color_render = font.render(f"{color}", True, (255, 255, 255))
	r_slider.draw(toolbar)
	g_slider.draw(toolbar)
	b_slider.draw(toolbar)
	brush_size_slider.draw(toolbar)
	toolbar.blit(rgb_color_render, (toolbar_width // 2 - rgb_color_render.get_width() // 2, b_slider.circle_y + b_slider.circle_radius + 10))
	pygame.draw.rect(toolbar, color, (toolbar_width // 2 - 40 // 2, (b_slider.circle_y +  b_slider.circle_radius + 10) + rgb_color_render.get_height() + 10, 40, 40))
	pygame.draw.rect(toolbar, (0, 0, 0), (toolbar_width // 2 - 40 // 2, (b_slider.circle_y +  b_slider.circle_radius + 10) + rgb_color_render.get_height() + 10, 40, 40), 5)
	toolbar.blit(font.render(f"Colors", True, (255, 255, 255)), (toolbar_width // 2 - font.render(f"Colors", True, (255, 255, 255)).get_width() // 2, r_slider.circle_y - r_slider.circle_radius - font.render(f"Colors", True, (255, 255, 255)).get_height()))
	toolbar.blit(font.render(f"Brush Size", True, (255, 255, 255)), (toolbar_width // 2 - font.render(f"Brush Size", True, (255, 255, 255)).get_width() // 2, (b_slider.circle_y +  b_slider.circle_radius + 10) + rgb_color_render.get_height() + 60))
	pygame.draw.rect(toolbar, (0, 0, 0), (toolbar_width // 2 - brush_size // 2, (brush_size_slider.circle_y + brush_size_slider.circle_radius + 120) - brush_size // 2, brush_size, brush_size))
	window.blit(canvas, (canvas_x, canvas_y))
	window.blit(toolbar, (canvas_x + canvas.get_width(), canvas_y))
	save_or_not = save_button.pressed
	load_or_not = load_button.pressed
	save_button.draw(window)
	load_button.draw(window)
	if save_or_not:
		save(canvas)
	if load_or_not:
		image = load()
		if image != "DON'T LOAD":
			rects = [Image(0, 0, image)]
	pygame.display.flip()