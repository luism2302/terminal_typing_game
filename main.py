import sys
import time
import pygame
import random
from text import display_text, handle_initial_input

def main():
    #Initialize some pygame variables
    pygame.init()
    screen = pygame.display.set_mode((800,800))
    clock = pygame.time.Clock()
    pygame.event.set_blocked([pygame.MOUSEMOTION])
    font = pygame.font.Font(None, 40)
    running = True
    #Variables for logica and stuff
    stage = 0
    countdown_nums = [3,2,1]
    start_countdown = None

    while running:
        screen.fill("black")
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False 
                case pygame.KEYDOWN:
                    if stage == 0:
                        stage = handle_initial_input(event.unicode)
                        start_countdown = pygame.time.get_ticks()

        if stage == 0: 
            display_text(screen, font, "Welcome to my typing game!", (10,20))
            display_text(screen, font, "(Y) Start", (10,80))
            display_text(screen, font, "(N) Quit", (10,120))
        elif stage == 1:
            elapsed = (pygame.time.get_ticks() - start_countdown) // 1000 
            if elapsed < len(countdown_nums):
                if elapsed == 0:
                    display_text(screen, font, f"Get ready! The first word will appear in ...{countdown_nums[elapsed]}", (10,20))
                else:
                    display_text(screen, font, f"...{countdown_nums[elapsed]}", (10,20))

        if stage == -1:
            running = False
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
