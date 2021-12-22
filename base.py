import pygame
import sys
#from assets.constans import BOARD_BACKGROUND, HEIGHT, WIDTH, BLACK, WHITE, GREEN, FONT, FONT_SIZE, FONT_COLOR, START_FONT_SIZE
from assets.constans import *
FPS = 60


# class Button:
#     def __init__(self, text, position):
#         self._text = text
#         self.x, self.y = position
#         self.font = pygame.font.Font(FONT, FONT_SIZE)

#     def mouse_click(self, event):
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if pygame.mouse.get_pressed()[0]:
#                 print(self)


#     def mouse_on_button(self):
#         x, y = pygame.mouse.get_pos()
#         if self.rect



class Board():
    def __init__(self, image):
        """
        Create and initialize an empty board. 
        Call a function to draw a board.
        """
        self.outerline = pygame.Rect(20, 20, 720, 720)
        self.IMAGE = image
        self.draw_board()

    def draw_board(self):
        """
        Put an image as the background.
        The board is drawn as follows:
            - outline,
            - all of the 361 tiles (19x19),
            - 9 star points (small dots).
        Blit it to the screen.
        
        """

        rect = self.IMAGE.get_rect()
        rect.center = (450, 490)
        pygame.draw.rect(self.IMAGE, BLACK, self.outerline, 4)
        for rows in range(18):
                for columns in range(18):
                    rectangle = pygame.Rect(20 + (40*columns), 20 + (40*rows), 40, 40)
                    pygame.draw.rect(self.IMAGE, BLACK, rectangle, 1)
        for row in range(3):
            for col in range(3):
                xy = (140 + (240*col), 140 + (240*row))
                pygame.draw.circle(self.IMAGE, BLACK, xy, 4, 0)
        WIN.blit(self.IMAGE, rect)
        pygame.display.update()


# class Window():
#     def __init__(self):
#         pass

#     def draw_window():
#         WIN.fill(GREEN)
#         font = pygame.font.Font(FONT, FONT_SIZE)
#         move_label = font.render("Player 1 - your turn", 1, FONT_COLOR)
#         WIN.blit(move_label, (100, 50))


def draw_window():
    WIN.fill(GREEN)
    front = pygame.font.Font(FONT, FONT_SIZE)
    move_label = front.render("Player 1 - your turn", 1, FONT_COLOR)
    WIN.blit(move_label, (100, 50))


def main_game_screen():
    # WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    # pygame.display.set_caption("Go Game")
    IMAGE = pygame.image.load(BOARD_BACKGROUND).convert()
    IMAGE = pygame.transform.scale(IMAGE, (760, 760))
    # clock = pygame.time.Clock()
    run = True
    while run:
        draw_window()
        BOARD = Board(IMAGE)
        clock.tick(FPS)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
    pygame.quit()
    quit()


def start_screen():
    start = True
    while start:
        WIN.fill(GREEN)
        draw_label_starting_screen()
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
    

    pygame.quit()
    # quit()
    # return player1_name, player2_name


def draw_button():
    return pygame.Rect(400, 400, 100, 100)


def draw_label_starting_screen():
    font = pygame.font.Font(FONT, START_FONT_SIZE)
    label = font.render("Go Game", 1, FONT_COLOR)
    label_rect = label.get_rect(center=(WIDTH/2, HEIGHT/2 - 150))
    WIN.blit(label, label_rect)
    button = draw_button()
    run = True
    while run:
        for event in pygame.event.get():
            print('gona')
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = event.pos

                if button.collidepoint(mouse_position):
                    # print('button was pressed at {0}'.format(mouse_position))
                    run = False
        pygame.draw.rect(WIN, LIGHT_YELLOW, button)
        pygame.display.update()
        #clock.tick(FPS)
    pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Go Game - start game")
    start_screen()

    pygame.init()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Go Game")
    main_game_screen()


