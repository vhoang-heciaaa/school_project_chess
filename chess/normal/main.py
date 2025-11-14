import pygame
import sys
from data import WIDTH, HEIGHT, SQ, DEFAULT_BOARD
from UI import draw_board
from movement import handle_click
from game_state import create_game_state, draw_game_state

pygame.init()
# Tăng width để chừa chỗ cho bảng trạng thái
screen = pygame.display.set_mode((WIDTH + 200, HEIGHT))
pygame.display.set_caption("Chess với Bảng Trạng Thái")

board = [row[:] for row in DEFAULT_BOARD]
selected = None
valid_moves = []

# Khởi tạo game state
game_state = create_game_state()

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # Chỉ xử lý click trong vùng bàn cờ (không phải panel)
            if x < WIDTH:
                col = x // SQ
                row = y // SQ

                old_turn = game_state.current_turn
                # NHẬN ĐỦ 4 GIÁ TRỊ
                selected, new_turn, valid_moves, captured_piece = handle_click(
                    board, (row, col), selected, game_state.current_turn, valid_moves
                )

                # Xử lý quân bị ăn
                if captured_piece:
                    # Xác định người ăn (người vừa thực hiện nước đi)
                    captor_color = "white" if old_turn == "white" else "black"
                    game_state.add_captured_piece(captured_piece, captor_color)
                    print(f"{captor_color} ăn {captured_piece}")

                # Nếu lượt thay đổi, cập nhật game state
                if new_turn != old_turn:
                    game_state.switch_turn()

    # Cập nhật thời gian
    game_state.update_time()

    # Kiểm tra hết giờ
    if game_state.is_time_up():
        winner = game_state.get_winner()
        print(f"Game over! Người thắng: {winner}")
        running = False

    # Vẽ bàn cờ
    screen.fill((0, 0, 0))  # Clear screen
    draw_board(screen, board)

    # Vẽ selection và valid moves
    if selected:
        row, col = selected
        pygame.draw.rect(screen, (255, 0, 0), (col * SQ, row * SQ, SQ, SQ), 3)

    for move in valid_moves:
        row, col = move
        pygame.draw.circle(screen, (0, 255, 0),
                           (col * SQ + SQ // 2, row * SQ + SQ // 2), 8)

    # Vẽ bảng trạng thái
    draw_game_state(screen, game_state)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()