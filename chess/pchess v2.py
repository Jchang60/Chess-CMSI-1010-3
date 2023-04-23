import pygame


# Initalize pygame
pygame.init()

# Screen size
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Fonts and text
pygame.display.set_caption('PyChessV2')
font = pygame.font.Font('Walkway_Black.ttf', 20)
Mfont = pygame.font.Font('Walkway_Black.ttf', 40)
Lfont = pygame.font.Font('PlayfairDisplay-Black.otf', 50)

# Counter
clock = pygame.time.Clock()
fps = 60

# game variables and images
wh_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
wh_locs = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
bl_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
bl_locs = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
wh_cap = []
bl_cap = []


# 0 white turn: 1 white move: 2 black turn, 3 black move
turn_step = 0
selection = 100
valid_moves = []


# load piece images x 2
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
# check variables/ flashing counter
counter = 0
winner = ''
game_over = False


# draw game board
def draw_board():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'light gray', [700 - (column * 200), row * 100, 100, 100])
        pygame.draw.rect(screen, 'gray', [0, 800, WIDTH, 100])
        pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5)
        pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5)
        status_text = ['White: Select a Piece', 'White: Move the Piece',
                       'Black: Select a Piece', 'Black: Move the Piece']
        screen.blit(Lfont.render(status_text[turn_step], True, 'black'), (20, 820))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)
        screen.blit(Mfont.render('FORFEIT', True, 'black'), (810, 830))


# draw pieces on board
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


# Check all pieces valid opts
def check_opts(pieces, locs, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        loc = locs[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(loc, turn)
        elif piece == 'rook':
            moves_list = check_rook(loc, turn)
        elif piece == 'knight':
            moves_list = check_knight(loc, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(loc, turn)
        elif piece == 'queen':
            moves_list = check_queen(loc, turn)
        elif piece == 'king':
            moves_list = check_king(loc, turn)
        all_moves_list.append(moves_list)
    return all_moves_list


# Check king valid moves
def check_king(pos, color):
    moves_list = []
    if color == 'white':
        enemies_list = bl_locs
        friends_list = wh_locs
    else:
        friends_list = bl_locs
        enemies_list = wh_locs
    # King check for moving 1 square in any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (pos[0] + targets[i][0], pos[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


# Queen valid moves
def check_queen(pos, color):
    moves_list = check_bishop(pos, color)
    second_list = check_rook(pos, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list


# Bishop moves
def check_bishop(pos, color):
    moves_list = []
    if color == 'white':
        enemies_list = bl_locs
        friends_list = wh_locs
    else:
        friends_list = bl_locs
        enemies_list = wh_locs
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (pos[0] + (chain * x), pos[1] + (chain * y)) not in friends_list and \
                    0 <= pos[0] + (chain * x) <= 7 and 0 <= pos[1] + (chain * y) <= 7:
                moves_list.append((pos[0] + (chain * x), pos[1] + (chain * y)))
                if (pos[0] + (chain * x), pos[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


# Rook moves
def check_rook(pos, color):
    moves_list = []
    if color == 'white':
        enemies_list = bl_locs
        friends_list = wh_locs
    else:
        friends_list = bl_locs
        enemies_list = wh_locs
    for i in range(4):  # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (pos[0] + (chain * x), pos[1] + (chain * y)) not in friends_list and \
                    0 <= pos[0] + (chain * x) <= 7 and 0 <= pos[1] + (chain * y) <= 7:
                moves_list.append((pos[0] + (chain * x), pos[1] + (chain * y)))
                if (pos[0] + (chain * x), pos[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list


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


# Check valid knight moves
def check_knight(pos, color):
    moves_list = []
    if color == 'white':
        enemies_list = bl_locs
        friends_list = wh_locs
    else:
        friends_list = bl_locs
        enemies_list = wh_locs
    # Check for Knight's L shape moves
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (pos[0] + targets[i][0], pos[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


# Check for valid moves for selected
def check_valid_moves():
    if turn_step < 2:
        opts_list = wh_opts
    else:
        opts_list = bl_opts
    valid_opts = opts_list[selection]
    return valid_opts




# draw valid moves
def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)


# draw dead pieces on sidebar
def draw_captured():
    for i in range(len(wh_cap)):
        captured_piece = wh_cap[i]
        index = piece_list.index(captured_piece)
        screen.blit(bl_smimg[index], (825, 5 + 50 * i))
    for i in range(len(bl_cap)):
        captured_piece = bl_cap[i]
        index = piece_list.index(captured_piece)
        screen.blit(wh_smimg[index], (925, 5 + 50 * i))


# Flashing square if checked
def draw_check():
    if turn_step < 2:
        if 'king' in wh_pieces:
            king_index = wh_pieces.index('king')
            king_loc = wh_locs[king_index]
            for i in range(len(bl_opts)):
                if king_loc in bl_opts[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark red', [wh_locs[king_index][0] * 100 + 1,
                                                              wh_locs[king_index][1] * 100 + 1, 100, 100], 5)
    else:
        if 'king' in bl_pieces:
            king_index = bl_pieces.index('king')
            king_loc = bl_locs[king_index]
            for i in range(len(wh_opts)):
                if king_loc in wh_opts[i]:
                    if counter < 15:
                        pygame.draw.rect(screen, 'dark blue', [bl_locs[king_index][0] * 100 + 1,
                                                               bl_locs[king_index][1] * 100 + 1, 100, 100], 5)


# Game Over
def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))


# Main Loop
bl_opts = check_opts(bl_pieces, bl_locs, 'black')
wh_opts = check_opts(wh_pieces, wh_locs, 'white')
run = True
while run:
    clock.tick(fps)
    if counter < 30:
        counter += 1
    else:
        counter = 0
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    draw_captured()
    draw_check()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'
                if click_coords in wh_locs:
                    selection = wh_locs.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    wh_locs[selection] = click_coords
                    if click_coords in bl_locs:
                        bl_piece = bl_locs.index(click_coords)
                        wh_cap.append(bl_pieces[bl_piece])
                        if bl_pieces[bl_piece] == 'king':
                            winner = 'white'
                        bl_pieces.pop(bl_piece)
                        bl_locs.pop(bl_piece)
                    bl_opts = check_opts(bl_pieces, bl_locs, 'black')
                    wh_opts = check_opts(wh_pieces, wh_locs, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
                if click_coords in bl_locs:
                    selection = bl_locs.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    bl_locs[selection] = click_coords
                    if click_coords in wh_locs:
                        wh_piece = wh_locs.index(click_coords)
                        bl_cap.append(wh_pieces[wh_piece])
                        if wh_pieces[wh_piece] == 'king':
                            winner = 'black'
                        wh_pieces.pop(wh_piece)
                        wh_locs.pop(wh_piece)
                    bl_opts = check_opts(bl_pieces, bl_locs, 'black')
                    wh_opts = check_opts(wh_pieces, wh_locs, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_RETURN:
                game_over = False
                winner = ''
                wh_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                wh_locs = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                bl_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                bl_locs = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                wh_cap = []
                bl_cap = []
                turn_step = 0
                selection = 100
                valid_moves = []
                bl_opts = check_opts(bl_pieces, bl_locs, 'black')
                wh_opts = check_opts(wh_pieces, wh_locs, 'white')
    if winner != '':
        game_over = True
        draw_game_over()
    pygame.display.flip()
pygame.quit()