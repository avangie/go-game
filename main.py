import pygame


WIDTH, HEIGHT = 900, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Go Game")

FPS = 60
GREEN = (0, 51, 0)


def draw_window():
    WIN.fill(GREEN)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()