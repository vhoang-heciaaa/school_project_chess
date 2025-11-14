import pygame
from data import SQ


def handle_click(board, position, selected, current_turn, valid_moves):
    """
    Xử lý sự kiện click chuột và trả về trạng thái mới
    """
    row, col = position
    captured_piece = None

    if selected is None:
        # chọn quân
        if board[row][col] != "":
            # Kiểm tra quân cờ có thuộc lượt hiện tại không
            piece = board[row][col]
            if (current_turn == "white" and piece.isupper()) or (current_turn == "black" and piece.islower()):
                selected = (row, col)
                # Lấy các nước đi hợp lệ
                from rule import get_valid_moves
                valid_moves = get_valid_moves(board, selected, current_turn)
    else:
        # Kiểm tra nước đi hợp lệ
        if (row, col) in valid_moves:
            start_row, start_col = selected
            target_piece = board[row][col]

            # Ghi nhận quân bị ăn
            if target_piece:
                captured_piece = target_piece

            # Thực hiện nước đi
            from rule import make_move
            success, new_turn = make_move(board, selected, (row, col), current_turn)
            if success:
                current_turn = new_turn

        # Reset selection
        selected = None
        valid_moves = []

        # Nếu click vào quân cờ khác cùng màu, chọn ngay
        if board[row][col] != "":
            piece = board[row][col]
            if (current_turn == "white" and piece.isupper()) or (current_turn == "black" and piece.islower()):
                selected = (row, col)
                from rule import get_valid_moves
                valid_moves = get_valid_moves(board, selected, current_turn)

    return selected, current_turn, valid_moves, captured_piece