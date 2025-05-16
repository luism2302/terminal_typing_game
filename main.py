import sys
import time
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,800))
    clock = pygame.time.Clock()
    running = True
    font = pygame.font.Font(None, 40)
    #Welcome message
    welcome_txt = font.render("Welcome to my typing game", True, (255,255,255))
    welcome_pos = welcome_txt.get_rect(centerx = screen.get_width()/2, y = 20)
    #Start the game input
    start_txt = font.render("(Y) Start (N) Quit", True ,(255,255,255))
    start_pos = welcome_txt.get_rect(centerx = screen.get_width()/2, y = 100)
    stage = 0

    while running:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.TEXTINPUT and stage == 0:
                match event.text:
                    case "y":
                        stage += 1
                    case "n":
                        running = False
        if stage == 0: 
            screen.blit(welcome_txt, welcome_pos)
            screen.blit(start_txt,start_pos)
        elif stage == 1:
            get_ready_txt1 = font.render("Get ready! The first word will appear in ...3", True ,(255,255,255))
            get_ready_txt2 = font.render("...2", True ,(255,255,255))
            get_ready_txt3 = font.render("...3", True ,(255,255,255))
            get_ready_txt1_pos = welcome_txt.get_rect(centerx = screen.get_width()/2, y = 100)
            get_ready_txt2_pos = welcome_txt.get_rect(centerx = screen.get_width()/2, y = 120)
            get_ready_txt3_pos = welcome_txt.get_rect(centerx = screen.get_width()/2, y = 140)
            screen.blit(get_ready_txt1 , get_ready_txt1_pos)
            pygame.time.delay(1000)
            screen.blit(get_ready_txt2 , get_ready_txt2_pos)
            pygame.time.delay(1000)
            screen.blit(get_ready_txt3 , get_ready_txt3_pos)

        pygame.display.flip()
if __name__ == "__main__":
    main()
