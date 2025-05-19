import pygame
import random

all_words = []
with open("words.txt", "r") as f:
	for line in f:
		all_words.append(line.strip())

def display_text(display: pygame.Surface, size: int, text: str, position: tuple, where:str = "left"):
	font = pygame.font.Font("assets/Outfit-Regular.ttf", size)
	black = (0,0,0)
	rendered_text = font.render(text, True, black)
	match where:
		case "left":
			pos_text = rendered_text.get_rect(x = position[0], y = position[1])  
		case "center":
			pos_text = rendered_text.get_rect(centerx = display.get_width() // 2, y = position[1])  

	display.blit(rendered_text, pos_text)

def handle_initial_input(key_pressed: str):
	match key_pressed.lower():
		case 'n':
			return -1
		case 'y':
			return 1
		case _:
			return 0

def handle_word_input(curr_typed_word: str, inp: str):
	if inp == "\x08":
		if curr_typed_word == "":
			return ""
		else:
			return curr_typed_word[:-1]
	else:
		return curr_typed_word + inp

def choose_word(word_list: list[str] = all_words):
	return random.choice(word_list)

def check_typed_word(chosen_word: str, typed_word: str):
	return chosen_word == typed_word
	
