import pygame
import sys
import subprocess

import back
from pygame.constants import K_ESCAPE, KEYDOWN, MOUSEBUTTONDOWN
from assets.constans import *
FPS = 60

# mozna, ale mijaloby sie to z celem - kazdy button mialby inna funkcje, ktora triggeruje wiec dla kazdego oddzielna klasa? 
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



class Board(back.Board):
    # hmuch = 0
    def __init__(self, image):
        """
        Create and initialize an empty board. 
        Call a function to draw a board.
        """
        super(Board, self).__init__()
        self.outline = pygame.Rect(30, 30, 720, 720)
        self.IMAGE = image
        # Board.hmuch += 1
        self.draw_board()

    
    # @classmethod
    # def much(cls):
    #     return cls.hmuch


    def draw_board(self):
        """
        Put an image as the background.
        The board is drawn as follows:
            - lines as contour of the board,
            - all of the 361 tiles (19x19),
            - 9 star points (small dots).
        Blit it to the screen.
        
        """
        #self.outline.inflate_ip(20, 20)
        rect = self.IMAGE.get_rect()
        rect.center = (450, 490)
        pygame.draw.rect(self.IMAGE, BLACK, self.outline, 4)
        for rows in range(18):
                for columns in range(18):
                    rectangle = pygame.Rect(30 + (40*columns), 30 + (40*rows), 40, 40)
                    pygame.draw.rect(self.IMAGE, BLACK, rectangle, 1)
        for row in range(3):
            for col in range(3):
                xy = (150 + (240*col), 150 + (240*row))
                pygame.draw.circle(self.IMAGE, BLACK, xy, 4, 0)
        WIN.blit(self.IMAGE, rect)
        pygame.display.update()


class Stone(back.Stone):
    def __init__(self, color, point, board):
        """
        Create and initialize a stone, draw as a black or white circle.
        """
        super().__init__(color, point, board)
        self._coordinates = (self._coordinates[0]*40, self._coordinates[1]*40)
        self.draw()

    def draw(self):
        """
        Draw the stone.
        """
        pygame.draw.circle(WIN, self._color, self._coordinates, 18, 0)
        pygame.display.update()

    def remove(self):
        """
        Remove the stone from the board.
        """
        pass



def draw_background():
    """
    Draws background for the main game screen.
    """
    WIN.fill(GREEN)
    # front = pygame.font.Font(FONT, FONT_SIZE)
    # move_label = front.render("Player 1 - your turn", 1, LIGHT_YELLOW)
    # WIN.blit(move_label, (100, 50))
    pygame.display.update()


def main_game_screen():
    pygame.display.set_caption("Go Game")
    draw_background()
    IMAGE = pygame.image.load(BOARD_BACKGROUND).convert()
    IMAGE = pygame.transform.scale(IMAGE, (780, 780))
    BOARD = Board(IMAGE)
    pygame.display.update()
    run = True
    while run:
        clock.tick(FPS)
        #pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()   
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if BOARD.outline.collidepoint(event.pos) and event.button == 1:
                    pos_x = int(round((event.pos[0]) / 40))
                    pos_y = int(round((event.pos[1]) / 40))
                    print(pos_x, pos_y)
                    stone = Stone(BOARD.whose_turn(), (pos_x, pos_y), BOARD)




    pygame.quit()
    quit()



def start_screen():
    pygame.display.set_caption("Go Game - start game")
    click = False
    start = True
    while start:
        WIN.fill(GREEN)
        set_start_title_game()
        set_start_image()


        mouse_x, mouse_y = pygame.mouse.get_pos()
        button_start = pygame.Rect(350, 500, 200, 50)
        button_quit = pygame.Rect(350, 575, 200, 50)
        button_instructions = pygame.Rect(350, 650, 200, 50)

        if button_start.collidepoint((mouse_x, mouse_y)):
            if click:
                main_game_screen()
        elif button_quit.collidepoint((mouse_x, mouse_y)):
            if click:
                pygame.quit()
                sys.exit()
        elif button_instructions.collidepoint((mouse_x, mouse_y)):
            if click:
                subprocess.Popen(['xdg-open', 'images/go_rules.txt'])
        

        font = pygame.font.Font(FONT, START_OPTIONS_FONT_SIZE)
        label = font.render("Start game", 1, BLACK)
        pygame.draw.rect(WIN, LIGHT_YELLOW, button_start)
        label_rect = label.get_rect(center=(WIDTH/2, 525))
        WIN.blit(label, label_rect)
        label = font.render("Quit game", 1, BLACK)
        pygame.draw.rect(WIN, LIGHT_YELLOW, button_quit)
        label_rect = label.get_rect(center=(WIDTH/2, 600))
        WIN.blit(label, label_rect)
        label = font.render("Instructions", 1, BLACK)
        pygame.draw.rect(WIN, LIGHT_YELLOW, button_instructions)
        label_rect = label.get_rect(center=(WIDTH/2, 675))
        WIN.blit(label, label_rect)


        clock.tick(FPS)
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()

    

    # pygame.quit()
    # quit()
    # return player1_name, player2_name



def set_start_title_game():
    font = pygame.font.Font(FONT, START_TITLE_FONT_SIZE)
    label = font.render("Go Game", 1, LIGHT_YELLOW)
    label_rect = label.get_rect(center=(WIDTH/2, HEIGHT/2 - 250))
    WIN.blit(label, label_rect)

def set_start_image():
    IMAGE = pygame.image.load(ICON).convert_alpha()
    IMAGE = pygame.transform.scale(IMAGE, (150, 150))
    WIN.blit(IMAGE, (375,275))


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    start_screen()


#funkcja na zmienianie playera 1 na 2
#mozliwosc wpisania nazw graczy i wypisywanie ich zamiast player 1 2