import pygame

# Initialize pygame
pygame.init()

# Define constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
SQUARE_SIZE = 80
BOARD_WIDTH = SQUARE_SIZE * 8
BOARD_HEIGHT = SQUARE_SIZE * 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60
#square color
LIGHT_SQUARE_COLOR = pygame.Color("white")
DARK_SQUARE_COLOR = pygame.Color("gray")
#piece images
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
PIECE_IMAGES = {
    "wp": wpawn_img,
    "bp": bpawn_img,
    "wr": wrook_img,
    "br": brook_img,
    "wk": wknight_img,
    "bk": bknight_img,
    "wb": wbishop_img,
    "bb": bbishop_img,
    "wq": wqueen_img,
    "bq": bqueen_img,
    "wki": wking_img,
    "bki": bking_img,
}
# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chess")

# Set up the clock
clock = pygame.time.Clock()
# Define Classes
class Board:
    def __init__(self):
        self.grid = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.move_functions = {"p": self.get_pawn_moves, "R": self.get_rook_moves, 
                               "N": self.get_knight_moves, "B": self.get_bishop_moves, 
                               "Q": self.get_queen_moves, "K": self.get_king_moves}
        self.white_to_move = True
        self.move_log = []

    def draw(self, screen):
        # Draw the chess board
        for row in range(8):
            for col in range(8):
                color = self.get_square_color(row, col)
                pygame.draw.rect(screen, color, pygame.Rect(col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                piece = self.grid[row][col]
                if piece != "--":
                    img = PIECE_IMAGES[piece]
                    screen.blit(img, pygame.Rect(col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def get_square_color(self, row, col):
        if row % 2 == 0:
            if col % 2 == 0:
                return LIGHT_SQUARE_COLOR
            else:
                return DARK_SQUARE_COLOR
        else:
            if col % 2 == 0:
                return DARK_SQUARE_COLOR
            else:
                return LIGHT_SQUARE_COLOR

    def get_all_valid_moves(self):
        moves = []
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                piece_color = self.grid[row][col][0]
                if (piece_color == "w" and self.white_to_move) or (piece_color == "b" and not self.white_to_move):
                    moves += self.get_valid_moves((row, col))
        return moves

    def get_valid_moves(self, square):
        row, col = square
        piece = self.grid[row][col]
        if piece == "--":
            return []
        piece_color = piece[0]
        if (piece_color == "w" and not self.white_to_move) or (piece_color == "b" and self.white_to_move):
            return []
        piece_type = piece[1]
        move_function = self.move_functions[piece_type]
        moves = move_function((row, col))
        return moves

    def get_pawn_moves(self, square):
        moves = []
        row, col = square
        if self.white_to_move:
            if self.grid[row-1][col] == "--":
                moves.append((row-1, col))
                if row == 6 and self.grid[row-2][col] == "--":
                    moves.append((row-1, col))
                if row == 6 and self.grid[row-2][col] == "--":
                    moves.append((row-2, col))
            if col-1 >= 0 and self.grid[row-1][col-1][0] == "b":
                moves.append((row-1, col-1))
            if col+1 <= 7 and self.grid[row-1][col+1][0] == "b":
                moves.append((row-1, col+1))
        else:
            if self.grid[row+1][col] == "--":
                moves.append((row+1, col))
                if row == 1 and self.grid[row+2][col] == "--":
                    moves.append((row+2, col))
            if col-1 >= 0 and self.grid[row+1][col-1][0] == "w":
                moves.append((row+1, col-1))
            if col+1 <= 7 and self.grid[row+1][col+1][0] == "w":
                moves.append((row+1, col+1))
        return moves

# Create the board
board = Board()

# Set up the main game loop
running = True
selected_piece = None
valid_moves = []
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            mouse_pos = pygame.mouse.get_pos()

            # Check if a piece has been selected
            if selected_piece is None:
                selected_piece = board.get_piece_at_pos(mouse_pos)

                if selected_piece is not None and selected_piece.color != "white":
                    selected_piece = None

            # Check if a square has been clicked
            else:
                square_pos = board.get_square_pos(mouse_pos)

                # Check if the move is valid
                if square_pos in valid_moves:
                    board.move_piece(selected_piece, square_pos)

                    # Reset the selected piece and valid moves
                    selected_piece = None
                    valid_moves = []
                else:
                    selected_piece = None

    # Draw the board and pieces
    board.draw(screen)

    # Highlight the valid moves
    if selected_piece is not None:
        valid_moves = board.get_valid_moves(selected_piece)
        board.highlight_squares(valid_moves, screen, (0, 255, 0))

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(FPS)

# Quit pygame
pygame.quit()
