import sys
import time
import pygame
import random

all_words = []
with open("words.txt", "r") as f:
    for line in f:
        all_words.append(line.strip())


def main():
    pygame.init()
    screen = pygame.display.set_mode((800,800))
    clock = pygame.time.Clock()
    running = True
    font = pygame.font.Font(None, 40)
    #Welcome message
    welcome_txt = font.render("Welcome to my typing game", True, (255,255,255))
    welcome_pos = welcome_txt.get_rect(x = 10, y = 20)
    #Start the game input
    start_y = font.render("(Y) Start", True ,(255,255,255))
    start_y_pos = start_y.get_rect(x = 10, y = 80)
    start_n = font.render("(N) Quit", True ,(255,255,255))
    start_n_pos = start_n.get_rect(x = 10, y = 120)
    #Variables for the different stages of the game
    stage = 0
    countdown_nums = [3,2,1]
    start_countdown = None
    chosen_word = None
    typed_word = ""

    while running:
        screen.fill("black")
        for event in pygame.event.get():
            print(event)
            match event.type:
                case pygame.QUIT:
                    running = False
                case pygame.TEXTINPUT:
                    if stage == 0:
                        match event.text:
                            case "y":
                                stage += 1
                                start_countdown = pygame.time.get_ticks()
                            case "n":
                                running = False
                    if stage == 2:
                        pass
        if stage == 0: 
            screen.blit(welcome_txt, welcome_pos)
            screen.blit(start_y, start_y_pos)
            screen.blit(start_n, start_n_pos)

        elif stage == 1:
            elapsed = (pygame.time.get_ticks() - start_countdown) // 1000 
            if elapsed < len(countdown_nums):
                if elapsed == 0:
                    get_ready_txt1 = font.render(f"Get ready! The first word will appear in ...{countdown_nums[elapsed]}", True ,(255,255,255))
                else:
                    get_ready_txt1 = font.render(f"...{countdown_nums[elapsed]}", True ,(255,255,255))
                get_ready_txt1_pos = welcome_txt.get_rect(x = 10, y = elapsed)
                screen.blit(get_ready_txt1 , get_ready_txt1_pos)
            else:
                stage += 1
        elif stage == 2:
            if chosen_word is None or typed_word == chosen_word:
                chosen_word = random.choice(all_words)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
