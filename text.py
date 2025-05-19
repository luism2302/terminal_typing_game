import pygame
import sys

def display_text(display: pygame.Surface, font: pygame.font.Font, text: str, position: tuple):
	white = (255,255,255)
	rendered_text = font.render(text, True, white)
	pos_text = rendered_text.get_rect(x = position[0], y = position[1])  
	display.blit(rendered_text, pos_text)

def handle_initial_input(key_pressed: str):
	if key_pressed.lower() == 'n':
		return -1
	elif key_pressed.lower() == 'y':
		return 1	

