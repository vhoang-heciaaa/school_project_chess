import pygame
from data import ROWS, COLS, SQ, WHITE_SQUARE, BROWN_SQUARE

# Sử dụng Unicode characters (giống trong HTML)
HTML_UNICODE_PIECES = {
    "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚", "p": "♟",
    "R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔", "P": "♙"
}


def draw_board(screen, board):
    """
    Vẽ bàn cờ và quân cờ sử dụng Unicode (như trong HTML)
    """
    # Khởi tạo font một lần
    if not hasattr(draw_board, 'font'):
        try:
            # Thử các font hỗ trợ Unicode
            fonts = ['Segoe UI Symbol', 'Arial Unicode MS', 'DejaVu Sans']
            for font_name in fonts:
                try:
                    draw_board.font = pygame.font.SysFont(font_name, 45)
                    break
                except:
                    continue
            else:
                draw_board.font = pygame.font.Font(None, 45)
        except:
            draw_board.font = pygame.font.Font(None, 45)

    # Vẽ các ô cờ
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE_SQUARE if (row + col) % 2 == 0 else BROWN_SQUARE
            pygame.draw.rect(screen, color, (col * SQ, row * SQ, SQ, SQ))

            # Vẽ quân cờ
            piece = board[row][col]
            if piece and piece in HTML_UNICODE_PIECES:
                piece_char = HTML_UNICODE_PIECES[piece]
                text_color = (0, 0, 0)  # Màu đen

                text = draw_board.font.render(piece_char, True, text_color)
                text_rect = text.get_rect(center=(col * SQ + SQ // 2, row * SQ + SQ // 2))
                screen.blit(text, text_rect)


def draw_selection_and_moves(screen, selected, valid_moves):
    """
    Vẽ ô được chọn và các nước đi hợp lệ
    """
    # Vẽ ô được chọn
    if selected:
        row, col = selected
        pygame.draw.rect(screen, (255, 0, 0), (col * SQ, row * SQ, SQ, SQ), 3)

    # Vẽ các nước đi hợp lệ
    for move in valid_moves:
        row, col = move
        pygame.draw.circle(screen, (0, 255, 0),
                           (col * SQ + SQ // 2, row * SQ + SQ // 2), 8)