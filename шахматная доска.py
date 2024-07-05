import tkinter as tk
from tkinter import ttk
import chess

class ChessApp:
    def __init__(self, master):
        self.master = master
        master.title("Chess")

        self.board = chess.Board()

        self.frame = tk.Frame(master)
        self.frame.pack()

        self.squares = []
        for row in range(8):
            for col in range(8):
                square = tk.Button(self.frame, width=4, height=2, command=lambda row=row, col=col: self.square_clicked(row, col))
                square.grid(row=row, column=col)
                self.squares.append(square)

        self.update_board()

    def square_clicked(self, row, col):
        square_index = row * 8 + col
        algebraic_notation = chess.square_name(square_index)

        if self.board.is_legal(chess.Move.from_uci(algebraic_notation)):
            self.board.push(chess.Move.from_uci(algebraic_notation))
            self.update_board()

    def update_board(self):
        for i, square in enumerate(self.squares):
            piece = self.board.piece_at(i)
            if piece is not None:
                if piece.color == chess.WHITE:
                    if piece.piece_type == chess.KING:
                        square.config(text="♔", bg="white", fg="black")
                    elif piece.piece_type == chess.QUEEN:
                        square.config(text="♕", bg="white", fg="black")
                    elif piece.piece_type == chess.ROOK:
                        square.config(text="♖", bg="white", fg="black")
                    elif piece.piece_type == chess.BISHOP:
                        square.config(text="♗", bg="white", fg="black")
                    elif piece.piece_type == chess.KNIGHT:
                        square.config(text="♘", bg="white", fg="black")
                    elif piece.piece_type == chess.PAWN:
                        square.config(text="♙", bg="white", fg="black")
                else:
                    if piece.piece_type == chess.KING:
                        square.config(text="♚", bg="black", fg="white")
                    elif piece.piece_type == chess.QUEEN:
                        square.config(text="♛", bg="black", fg="white")
                    elif piece.piece_type == chess.ROOK:
                        square.config(text="♜", bg="black", fg="white")
                    elif piece.piece_type == chess.BISHOP:
                        square.config(text="♝", bg="black", fg="white")
                    elif piece.piece_type == chess.KNIGHT:
                        square.config(text="♞", bg="black", fg="white")
                    elif piece.piece_type == chess.PAWN:
                        square.config(text="♟", bg="black", fg="white")
            else:
                if (i // 8 + i % 8) % 2 == 0:
                    square.config(text="", bg="white")
                else:
                    square.config(text="", bg="black")

root = tk.Tk()
app = ChessApp(root)
root.mainloop()