import pygame

# Initialize Pygame
pygame.init()

# Set up the screen size
screen_width = 1000
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
#fonts for text
font = pygame.font.Font('Walkway_Black.ttf',20)
Lfont = pygame.font.Font('PlayfairDisplay-Black.otf', 50)
#text
pygame.display.set_caption('2P PyChess ')
#timer
clock = pygame.time.Clock()
fps = 60
# Load images for the pieces and board
board_img = pygame.image.load("board.png")
    #black pieces
bpawn_img = pygame.image.load("bl_pawn.png")
bpawn_img = pygame.transform.scale(bpawn_img, (80,80))
bpawn_imgsmall = pygame.transform.scale(bpawn_img, (45,45))

brook_img = pygame.image.load("bl_rook.png")
brook_img = pygame.transform.scale(brook_img, (80,80))
brook_imgsmall = pygame.transform.scale(brook_img, (45,45))

bknight_img = pygame.image.load("bl_knight.png")
bknight_img = pygame.transform.scale(bknight_img, (80,80))
bknight_imgsmall = pygame.transform.scale(bknight_img, (45,45))

bbishop_img = pygame.image.load("bl_bishop.png")
bbishop_img = pygame.transform.scale(bbishop_img, (80,80))
bbishop_imgsmall = pygame.transform.scale(bbishop_img, (45,45))

bqueen_img = pygame.image.load("bl_queen.png")
bqueen_img = pygame.transform.scale(bqueen_img, (80,80))
bqueen_imgsmall = pygame.transform.scale(bqueen_img, (45,45))

bking_img = pygame.image.load("bl_king.png")
bking_img = pygame.transform.scale(bking_img, (80,80))
bking_imgsmall = pygame.transform.scale(bking_img, (45,45))
bl_img = [bpawn_img, bqueen_img, bking_img, bknight_img, brook_img, bbishop_img]
bl_smimg = [bpawn_imgsmall, bqueen_imgsmall, bking_imgsmall, bknight_imgsmall, brook_imgsmall, bbishop_imgsmall]
    #white pieces
wpawn_img = pygame.image.load("wh_pawn.png")
wpawn_img = pygame.transform.scale(wpawn_img, (80,80))
wpawn_imgsmall = pygame.transform.scale(wpawn_img, (45,45))

wrook_img = pygame.image.load("wh_rook.png")
wrook_img = pygame.transform.scale(wrook_img, (80,80))
wrook_imgsmall = pygame.transform.scale(wrook_img, (45,45))

wknight_img = pygame.image.load("wh_knight.png")
wknight_img = pygame.transform.scale(wknight_img, (80,80))
wknight_imgsmall = pygame.transform.scale(wknight_img, (45,45))

wbishop_img = pygame.image.load("wh_bishop.png")
wbishop_img = pygame.transform.scale(wbishop_img, (80,80))
wbishop_imgsmall = pygame.transform.scale(wbishop_img, (45,45))

wqueen_img = pygame.image.load("wh_queen.png")
wqueen_img = pygame.transform.scale(wqueen_img, (80,80))
wqueen_imgsmall = pygame.transform.scale(wqueen_img, (45,45))

wking_img = pygame.image.load("wh_king.png")
wking_img = pygame.transform.scale(wking_img, (80,80))
wking_imgsmall = pygame.transform.scale(wking_img, (45,45))
wh_img = [wpawn_img, wqueen_img, wking_img, wknight_img,wrook_img, wbishop_img]
wh_smimg = [wpawn_imgsmall, wqueen_imgsmall, wking_imgsmall, wknight_imgsmall, wrook_imgsmall, wbishop_imgsmall]

# Piecelist
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']
# Variable checker and counter

# Variables
wh_pieces = ['rook','knight','bishop', 'king', 'queen', 'bishop', 'knight','rook', 
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
wh_locs = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
           (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1) ]
bl_pieces = ['rook','knight','bishop', 'king', 'queen', 'bishop', 'knight','rook', 
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
bl_locs = [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7),
           (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6) ]
wh_cap = []
bl_cap = []
# Who's turn is it? white = 0, black = 1 TURNS AND VALID MOVES
turn_step = 0
selection = 100
valid_moves = []

# Board Drawing
def draw_board():
    for i in range(32):
        col = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [600 - (col * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'light gray', [700 - (col * 200), row * 100, 100, 100])
        pygame.draw.rect(screen, 'gray', [0, 800, screen_width, 100])
        pygame.draw.rect(screen, 'gold', [0, 800, screen_width, 100], 5)
        pygame.draw.rect(screen, 'gold', [800, 0, 200, screen_height], 5)
        textstate = ['White: Select a piece', 'White: Move',  
                     'Black: Select a piece', 'Black: Move']
        screen.blit(Lfont.render(textstate[turn_step], True, 'black'), (20, 820))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
# Piece Drawing
def draw_pieces():
    for i in range(len(wh_pieces)):
        index = piece_list.index(wh_pieces[i])
        if wh_pieces[i] == 'pawn':
            screen.blit(wpawn_img, (wh_locs[i][0] * 100 + 11, wh_locs[i][1] * 100 + 10))
        else:
            screen.blit(wh_img[index], (wh_locs[i][0] * 100 + 11, wh_locs[i][1] * 100 + 10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'red', [wh_locs[i][0] * 100 + 1, wh_locs[i][1] * 100 + 1, 100, 100], 2)
    for i in range(len(bl_pieces)):
        index = piece_list.index(bl_pieces[i])
        if wh_pieces[i] == 'pawn':
            screen.blit(bpawn_img, (bl_locs[i][0] * 100 + 11, bl_locs[i][1] * 100 + 10))
        else:
            screen.blit(bl_img[index], (bl_locs[i][0] * 100 + 11, bl_locs[i][1] * 100 + 10))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [bl_locs[i][0] * 100 + 1, bl_locs[i][1] * 100 + 1, 100, 100], 2)

# Check valid moves
def check_opt(pieces, locs, turn):
    moves_list = []
    all_moves = []
    for i in range((len(pieces))):
        loc = locs[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(locs, turn)
 
        all_moves.append(moves_list)
    return all_moves

# Check valid pawn moves
def check_pawn(pos, color):
    moves_list = []
    if color == 'white':
        if (pos[0], pos[1] + 1) not in wh_locs and \
                (pos[0], pos[1] + 1) not in bl_locs and pos[1] < 7:
            moves_list.append((pos[0], pos[1] + 1))
        if (pos[0], pos[1] + 2) not in wh_locs and \
                (pos[0], pos[1] + 2) not in bl_locs and pos[1] == 1:
            moves_list.append((pos[0], pos[1] + 2))
        if (pos[0] + 1, pos[1] + 1) in bl_locs:
            moves_list.append((pos[0] + 1, pos[1] + 1))
        if (pos[0] - 1, pos[1] + 1) in bl_locs:
            moves_list.append((pos[0] - 1, pos[1] + 1))
    else:
        if (pos[0], pos[1] - 1) not in wh_locs and \
                (pos[0], pos[1] - 1) not in bl_locs and pos[1] > 0:
            moves_list.append((pos[0], pos[1] - 1))
        if (pos[0], pos[1] - 2) not in wh_locs and \
                (pos[0], pos[1] - 2) not in bl_locs and pos[1] == 6:
            moves_list.append((pos[0], pos[1] - 2))
        if (pos[0] + 1, pos[1] - 1) in wh_locs:
            moves_list.append((pos[0] + 1, pos[1] - 1))
        if (pos[0] - 1, pos[1] - 1) in wh_locs:
            moves_list.append((pos[0] - 1, pos[1] - 1))
    return moves_list
# Check valid rook moves


# Check valid knight moves


# Check valid bishop moves


# Check valid king moves


# Check valid queen moves

# valid moves for selected
def check_valid():
    if turn_step < 2:
        opt_list = wh_opt
    else:
        opt_list = bl_opt
    valid_opt = opt_list[selection]
    return valid_opt
# Drawing valid moves
def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves [i][1] * 100 + 500), 5)

# Main Game Loop
bl_opt = check_opt(bl_pieces, bl_locs, 'black')
wh_opt = check_opt(wh_pieces, wh_locs, 'white')
run = True
while run:
    clock.tick(fps)
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    if selection != 100:
        valid_moves = check_valid()
        draw_valid(valid_moves)
# Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            xcoord = event.pos[0] // 100
            ycoord = event.pos[1] // 100
            clkcoord = (xcoord, ycoord)
            if turn_step <= 1:
                if clkcoord in wh_locs:
                    selection = wh_locs.index(clkcoord)
                    if turn_step == 0:
                        turn_step = 1
                if clkcoord in valid_moves and selection != 100:
                    wh_locs[selection] = clkcoord
                    if clkcoord in bl_locs:
                        bl_piece = bl_locs.index(clkcoord)
                        wh_cap.append(bl_pieces[bl_piece])
                        bl_pieces.pop(bl_piece)
                        bl_locs.pop(bl_piece)
                    bl_opt = check_opt(bl_pieces, bl_locs, 'black')
                    wh_opt = check_opt(wh_pieces, wh_locs, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if clkcoord in bl_locs:
                    selection = bl_locs.index(clkcoord)
                    if turn_step == 2:
                        turn_step = 3
                if clkcoord in valid_moves and selection != 100:
                    bl_locs[selection] = clkcoord
                    if clkcoord in wh_locs:
                        wh_piece = wh_locs.index(clkcoord)
                        bl_cap.append(wh_pieces[wh_piece])
                        wh_pieces.pop(wh_piece)
                        wh_locs.pop(wh_piece)
                    bl_opt = check_opt(bl_pieces, bl_locs, 'black')
                    wh_opt = check_opt(wh_pieces, wh_locs, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []                        
    pygame.display.flip()
pygame.quit