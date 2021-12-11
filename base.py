import pygame
from pygame.draw import circle
from assets.constans import BOARD_BACKGROUND, HEIGHT, WIDTH, BLACK, WHITE, GREEN

FPS = 60


class Board():
    def __init__(self):
        """
        Creates an empty board.
        """
        self.outerline = pygame.Rect(20, 20, 720, 720)
        self.draw_board()

    def draw_board(self):
        """
        Puts an image as the background - board. 
        Draws lines on the board.
        
        """
        rect = IMAGE.get_rect()
        rect.center = (450, 490)
        WIN.blit(IMAGE, rect)
        pygame.draw.rect(IMAGE, BLACK, self.outerline, 4)
        for rows in range(18):
                for columns in range(18):
                    rectangle = pygame.Rect(20 + (40*columns), 20 + (40*rows), 40, 40)
                    pygame.draw.rect(IMAGE, BLACK, rectangle, 1)
        for row in range(3):
            for col in range(3):
                xy = (140 + (240*col), 140 + (240*row))
                pygame.draw.circle(IMAGE, BLACK, xy, 4, 0)
        pygame.display.update()


def draw_window():
    WIN.fill(GREEN)


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        draw_window()
        BOARD = Board()
        
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
    pygame.quit()


if __name__ == "__main__":
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Go Game")
    IMAGE = pygame.image.load(BOARD_BACKGROUND).convert()
    IMAGE = pygame.transform.scale(IMAGE, (760, 760))
    main()