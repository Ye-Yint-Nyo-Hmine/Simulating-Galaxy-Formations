# Galaxy Formation Simulation
import pygame
import sys

# initialize pygame
pygame.init()


# set window properties
SCREEN_SIZE_FACTOR = 80
WIDTH, HEIGHT = 16*SCREEN_SIZE_FACTOR, 9*SCREEN_SIZE_FACTOR
WIN_CENTER = (WIDTH/2, HEIGHT/2)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Formation Simulation")



def game_update(WIN):
    
    WIN.fill("black")
    pygame.display.update()


def main():
    
    
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    
    while run:
        for event in pygame.event.get():
            # quit pygame
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        game_update(WIN)
        clock.tick(FPS)
        









if __name__ == '__main__':
    main()