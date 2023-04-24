import board
import pygame

# Initialize Pygame
pygame.init()

# Set up the screen size
screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Load images for the pieces and board
board_img = pygame.image.load("board.png")
bpawn_img = pygame.image.load("bl_pawn.png")
brook_img = pygame.image.load("bl_rook.png")
bknight_img = pygame.image.load("bl_knight.png")
bbishop_img = pygame.image.load("bl_bishop.png")
bqueen_img = pygame.image.load("bl_queen.png")
bking_img = pygame.image.load("bl_king.png")
wpawn_img = pygame.image.load("wh_pawn.png")
wrook_img = pygame.image.load("wh_rook.png")
wknight_img = pygame.image.load("wh_knight.png")
wbishop_img = pygame.image.load("wh_bishop.png")
wqueen_img = pygame.image.load("wh_queen.png")
wking_img = pygame.image.load("wh_king.png")


class Piece:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.has_moved = False

        # self.image = wpawn_img if color == 'white' else bpawn_img
        # self.rect = self.image.get_rect()
        # self.rect.x = x * 80
        # self.rect.y = y * 80

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.has_moved = True


class Knight(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.image = wknight_img if color == 'white' else bknight_img
        self.rect = self.image.get_rect()
        self.rect.x = x * 80
        self.rect.y = y * 80

    def is_valid_move(self, new_x, new_y):
        dx = abs(new_x - self.x)
        dy = abs(new_y - self.y)
        return (dx, dy) in [(1, 2), (2, 1)]


class Bishop(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.image = wbishop_img if color == 'white' else bbishop_img
        self.rect = self.image.get_rect()
        self.rect.x = x * 80
        self.rect.y = y * 80

    def is_valid_move(self, new_x, new_y):
        dx = abs(new_x - self.x)
        dy = abs(new_y - self.y)
        return dx == dy


class King(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.image = wking_img if color == 'white' else bking_img
        self.rect = self.image.get_rect()
        self.rect.x = x * 80
        self.rect.y = y * 80

    def is_valid_move(self, new_x, new_y):
        dx = abs(new_x - self.x)
        dy = abs(new_y - self.y)
        return (dx, dy) in [(0, 1), (1, 0), (1, 1)]


class Queen(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.image = wqueen_img if color == 'white' else bqueen_img
        self.rect = self.image.get_rect()
        self.rect.x = x * 80
        self.rect.y = y * 80

    def is_valid_move(self, new_x, new_y):
        dx = abs(new_x - self.x)
        dy = abs(new_y - self.y)
        return dx == dy or dx == 0 or dy == 0


class Rook(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.image = wrook_img if color == 'white' else brook_img
        self.rect = self.image.get_rect()
        self.rect.x = x * 80
        self.rect.y = y * 80

    def is_valid_move(self, new_x, new_y):
        dx = abs(new_x - self.x)
        dy = abs(new_y - self.y)
        return dx == 0 or dy == 0


class Pawn(Piece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.image = wpawn_img if color == 'white' else bpawn_img
        self.rect = self.image.get_rect()
        self.rect.x = x * 80
        self.rect.y = y * 80

        self.color = color

    def __str__(self):
        return 'Pawn'

    def get_valid_moves(self):
        if self.color == 'white':
            # white pawns can move one or two squares forward on their first move
            # and one square forward on subsequent moves
            if self.y == 1:
                return [(self.x, self.y + 1), (self.x, self.y + 2)]
            else:
                return [(self.x, self.y + 1)]
        else:
            # black pawns can move one or two squares forward on their first move
            # and one square forward on subsequent moves
            if self.y == 6:
                return [(self.x, self.y - 1), (self.x, self.y - 2)]
            else:
                return [(self.x, self.y - 1)]


white_pieces = [Pawn('white', 0, 1), Rook('white', 0, 0), Knight('white', 1, 0), Bishop('white', 2, 0),
                Queen('white', 3, 0), King('white', 4, 0)]

# Draw the board and pieces
board_x = 0
board_y = 0
square_size = 80

screen.blit(board_img, (0, 0))

for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 0:
            color = (255, 206, 158)
        else:
            color = (209, 139, 71)
        pygame.draw.rect(screen, color,
                         (board_x + col * square_size, board_y + row * square_size, square_size, square_size))
        if row == 0:
            if col == 0 or col == 7:
                screen.blit(brook_img, (board_x + col * square_size, board_y + row * square_size))
            elif col == 1 or col == 6:
                screen.blit(bknight_img, (board_x + col * square_size, board_y + row * square_size))
            elif col == 2 or col == 5:
                screen.blit(bbishop_img, (board_x + col * square_size, board_y + row * square_size))
            elif col == 3:
                screen.blit(bqueen_img, (board_x + col * square_size, board_y + row * square_size))
            elif col == 4:
                screen.blit(bking_img, (board_x + col * square_size, board_y + row * square_size))
        elif row == 1:
            screen.blit(bpawn_img, (board_x + col * square_size, board_y + row * square_size))
        elif row == 6:
            screen.blit(wpawn_img, (board_x + col * square_size, board_y + row * square_size))
        elif row == 7:
            if col == 0 or col == 7:
                screen.blit(wrook_img, (board_x + col * square_size, board_y + row * square_size))
            elif col == 1 or col == 6:
                screen.blit(wknight_img, (board_x + col * square_size, board_y + row * square_size))
            elif col == 2 or col == 5:
                screen.blit(wbishop_img, (board_x + col * square_size, board_y + row * square_size))
            elif col == 3:
                screen.blit(wqueen_img, (board_x + col * square_size, board_y + row * square_size))
            elif col == 4:
                screen.blit(wking_img, (board_x + col * square_size, board_y + row * square_size))
pygame.display.update()
running = True
selected_piece = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # 1025
            if event.button == 1: # 1
                # If no piece is selected, select a piece
                if not selected_piece:  # None
                    for piece in white_pieces:
                        print(piece.rect)  # top, bottom, right, left
                        if piece.rect.collidepoint(event.pos):
                            selected_piece = piece
                            print(selected_piece)
                            break
                # If a piece is selected, move it to the clicked square
                else:
                    square = board.find_square(event.pos)
                    if square and board.is_valid_move(selected_piece, square):
                        selected_piece.move(square.center)
                        selected_piece = None
                    else:
                        selected_piece = None


pygame.quit()
