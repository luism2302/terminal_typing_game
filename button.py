import pygame

class Button:
	def __init__(self, pos: tuple, text: str, type: str):
		self.black = (0,0,0)
		self.white = (255,255,255)
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.background = pygame.image.load("assets/button2.png")
		self.rect = self.background.get_rect(x = pos[0], y = pos[1])
		self.font = pygame.font.Font("assets/Outfit-Regular.ttf", 18)
		self.text = text
		self.rendered_text = self.font.render(self.text, True, self.black)
		self.text_rect = self.background.get_rect(x = pos[0] + 20 , y = pos[1] + 25)
		self.type = type

	def display_button(self, display: pygame.Surface):
		display.blits([(self.background,self.rect),(self.rendered_text,self.text_rect)])

	def check_hover(self, cursor: tuple):
		cursor_inside = self.rect.collidepoint(cursor[0], cursor[1])
		if cursor_inside:
			self.rendered_text = self.font.render(self.text, True, self.white)
			return True
		else:
			self.rendered_text = self.font.render(self.text, True, self.black)
			return False

	def pressed(self, cursor: tuple, stage: int):
		cursor_inside = self.rect.collidepoint(cursor[0], cursor[1])
		match self.type:
			case "start":
				if cursor_inside:
					return 1
				else:
					return stage
			case "quit":
				if cursor_inside:
					return -1
				else:
					return stage