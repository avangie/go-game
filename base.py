import pygame
import sys
import subprocess

import back
from pygame.constants import K_ESCAPE, KEYDOWN, MOUSEBUTTONDOWN
from assets.constans import *
FPS = 60


class Board(back.Board):
    def __init__(self):
        """
        Create and initialize an empty board. 
        Outline is a rectangle which is used as a collidebox.
        Call a function to draw a board.
        """
        super().__init__()
        self.collide_rect = pygame.rect.Rect(25,25, 720,720)
        self.outline = pygame.rect.Rect(25, 25, 780, 780)
        self.draw_board()

    def propert_u(self, stone=None):
        for group in self.get_set():
            if stone:
                if group == stone.get_set():
                    continue
            group.properties_w()
        if stone:
            stone.get_set().properties_w()

    def ooutline(self):
        return self.collide_rect

    def draw_board(self):
        """
        Put an image as the background.
        The board is drawn as follows:
            - lines as contour of the board,
            - all of the 361 tiles (19x19),
            - 9 star points (small dots).
        Blit it to the screen.
        
        """
        pygame.draw.rect(IMAGE, BLACK, self.ooutline(), 4)
        for rows in range(18):
                for columns in range(18):
                    rectangle = pygame.Rect(25 + (40*columns), 25 + (40*rows), 40, 40)
                    pygame.draw.rect(IMAGE, BLACK, rectangle, 1)
        for row in range(3):
            for col in range(3):
                xy = (145 + (240*col), 145 + (240*row))
                pygame.draw.circle(IMAGE, BLACK, xy, 4, 0)
        WIN.blit(IMAGE, (55,55))
        pygame.display.update()



class Stone(back.Stone):
    def __init__(self, color, point, board, image):
        """
        Create and initialize a stone, 
        count its coordinates,
        draw it as a black or white circle.
        """
        super().__init__(color, point, board)
        self._coords = ((self.coordy()[0])*40, (self.coordy()[1])*40)
        self.image = image
        self.draw_stone()

    def coords(self):
        return self._coords

    def get_image(self):
        return self.image

    def draw_stone(self):
        """
        Draw the stone.
        """
        pygame.draw.circle(WIN, self.get_color(), self.coords(), 18, 0)
        pygame.display.update()

    def remove(self):
        """
        Remove the stone from the board.
        """
        coord = self.coords()[0] - 20, self.coords()[1] - 20
        place = pygame.Rect((coord[0]-55, coord[1]-55), (40,40))
        WIN.blit(self.get_image(), coord, place)
        super().remove_stone()
        pygame.display.update()


def set_player_name(player):
    font = pygame.font.Font(FONT, 50)
    move_label = font.render(f'Player {player} ', True, LIGHT_YELLOW, GREEN)
    WIN.blit(move_label, (960, 230))


def main_game_screen():
    pygame.display.set_caption("Go Game")
    WIN.fill(GREEN)
    rect = IMAGE.get_rect()
    rect.center = (440, 440)
    WIN.blit(IMAGE, rect)
    BOARD = Board()

    set_player_name(1)
    font = pygame.font.Font(FONT, FONT_SIZE)
    move_label = font.render("- your turn ", True, LIGHT_YELLOW, GREEN)
    WIN.blit(move_label, (1050, 300))
    
    counter = 0
    click = 0
    run = True
    while run:
        font = pygame.font.Font(FONT, START_OPTIONS_FONT_SIZE)    
        button_instructions = pygame.Rect(920, 700, 200, 50)
        label = font.render("Instructions", 1, BLACK)
        pygame.draw.rect(WIN, LIGHT_YELLOW, button_instructions)
        label_rect = label.get_rect(center=(1020, 725))
        WIN.blit(label, label_rect)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if button_instructions.collidepoint((mouse_x, mouse_y)):
            if click:
                subprocess.Popen(['xdg-open', 'images/go_rules.txt'])
        pygame.display.update()

        clock.tick(FPS)
        click = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()   
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = 1
                if BOARD.outline.collidepoint(event.pos) and event.button == 1:
                    pos_x = int(round((event.pos[0]) / 40))         #pierwszy to (2,2)
                    pos_y = int(round((event.pos[1]) / 40))
                    position_of_stone = (pos_x, pos_y)
                    if pos_x < 2 or pos_y < 2 or pos_x > 20 or pos_y > 20:    
                        continue
                    is_stone = BOARD.find(coord = position_of_stone)
                    if is_stone:
                        pass
                    elif not is_stone:
                        stone = Stone(BOARD.whose_turn(), (pos_x, pos_y), BOARD, IMAGE)
                        counter += 1
                        print(stone.neighbours())
                        set_player_name((counter%2)+1)
                    
                    BOARD.propert_u(stone)

def draw_buttons_start_page(button_start, button_quit, button_instructions):
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


def start_screen():
    pygame.display.set_caption("Go Game - start game")
    click = False
    start = True
    while start:
        WIN.fill(GREEN)
        set_start_title_game()
        set_start_image()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        button_start = pygame.Rect(500, 500, 200, 50)
        button_quit = pygame.Rect(500, 575, 200, 50)
        button_instructions = pygame.Rect(500, 650, 200, 50)
        draw_buttons_start_page(button_start, button_quit, button_instructions)

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


def set_start_title_game():
    font = pygame.font.Font(FONT, START_TITLE_FONT_SIZE)
    label = font.render("Go Game", 1, LIGHT_YELLOW)
    label_rect = label.get_rect(center=(WIDTH/2, HEIGHT/2 - 250))
    WIN.blit(label, label_rect)

def set_start_image():
    IMAGE = pygame.image.load(ICON).convert_alpha()
    IMAGE = pygame.transform.scale(IMAGE, (150, 150))
    WIN.blit(IMAGE, (525,275))


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    IMAGE = pygame.image.load(BOARD_BACKGROUND).convert()
    IMAGE = pygame.transform.scale(IMAGE, (770, 770))
    start_screen()
