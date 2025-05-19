import pygame
from text import display_text, handle_initial_input, choose_word, check_typed_word, handle_word_input
from button import Button

def main():
    #Initialize some pygame variables
    pygame.init()
    screen = pygame.display.set_mode((600,300))
    clock = pygame.time.Clock()
    running = True
    word_box = pygame.Surface((400,80))
    word_box.fill((197,211,232))
    word_box_pos = word_box.get_rect(x = 100, y = 95)
    #Initial buttons
    start_button = Button((170,200), "Start", "start")
    again_button = Button((170,200), "Again", "start")
    quit_button = Button((350,200), "Quit", "quit")
    #Variables for logic and stuff
    stage = 0
    countdown_nums = [3,2,1]
    start_countdown = None
    completed = True
    typed_word = ""
    remaining_seconds = 60
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    clicked_cursor = None
    words_typed = 0

    while running:
        screen.fill((166,174,191))
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False 
                case pygame.KEYDOWN:
                    if stage == 2:
                        typed_word = handle_word_input(typed_word, event.unicode)
                case pygame.MOUSEBUTTONDOWN:
                    clicked_cursor = pygame.mouse.get_pos()
                    if stage == 0:
                        start_countdown = pygame.time.get_ticks()
                        stage = start_button.pressed(clicked_cursor, stage)
                        stage = quit_button.pressed(clicked_cursor, stage)
                    if stage == 3:
                        stage = again_button.pressed(clicked_cursor, stage)
                        stage = quit_button.pressed(clicked_cursor, stage)
                        completed = True
                        typed_word = ""
                        remaining_seconds = 60
                        words_typed = 0
                        start_countdown = pygame.time.get_ticks()
                case pygame.USEREVENT:
                    if stage == 2:
                        remaining_seconds -= 1

        match stage:
            case 0:
                display_text(screen, 34, "Welcome to my typing game!", (0,10), "center")
                start_button.display_button(screen)
                quit_button.display_button(screen)
                start_button.check_hover(pygame.mouse.get_pos())
                quit_button.check_hover(pygame.mouse.get_pos())

            case 1:
                elapsed = (pygame.time.get_ticks() - start_countdown) // 1000 
                if elapsed < len(countdown_nums):
                    if elapsed == 0:
                        display_text(screen, 28, f"Get ready! The first word will appear in ...{countdown_nums[elapsed]}", (10,20))
                    else:
                        display_text(screen, 28, f"...{countdown_nums[elapsed]}", (10,20))
                else:
                    stage = 2

            case 2:
                screen.blit(word_box,word_box_pos)
                display_seconds = remaining_seconds % 60
                display_minutes = int(remaining_seconds / 60) % 60
                display_text(screen, 24, f"Words Typed: {words_typed}",(10,0))
                if display_seconds > 0 or display_minutes > 0:
                    display_text(screen, 24, f"Timer: {display_minutes:02}:{display_seconds:02}",(450,0))
                    if completed:
                        chosen_word = choose_word()
                        typed_word = ""
                    display_text(screen, 44, chosen_word, (0,100), "center")
                    display_text(screen, 34, typed_word, (0, 180), "center")
                    completed = check_typed_word(chosen_word, typed_word)
                    if completed:
                        words_typed += 1
                else:
                    stage = 3

            case 3:
                display_text(screen, 34, f"Time's Up: You typed {words_typed} words", (10,20))
                again_button.display_button(screen)
                quit_button.display_button(screen) 
                again_button.check_hover(pygame.mouse.get_pos())
                quit_button.check_hover(pygame.mouse.get_pos())
            case -1:
                running = False

        clicked_cursor = None
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
