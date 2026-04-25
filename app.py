from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

def create_board():
    return [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

def add_random_tile(board):
    empty_cells = [(r, c) for r in range(4) for c in range(4) if board[r][c] ==0]
    if empty_cells :
        r, c = random.choice(empty_cells)
        board[r][c] = 2 if random.random() < 0.9 else 4

def move_row_left(row):
    new_row = [num for num in row if num !=0]

    i = 0
    while i < len(new_row) - 1:
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row.pop(i + 1)
            i += 1

    new_row = [num for num in new_row if num != 0]

    while len(new_row) < 4:
        new_row.append(0)
    return new_row

def move_left(board):
    for r in range(4):
        board[r] = move_row_left(board[r])

def move_right(board):
    for r in range(4):
        board[r] = move_row_left(board[r][::-1])[::-1]

def transpose(board):
    return [list(row) for row in zip(*board)]

def move_up(board):
    board[:] = transpose(board)
    for r in range(4):
        board[r] = move_row_left(board[r])
    board[:] = transpose(board)

def move_down(board):
    board[:] = transpose(board)
    for r in range(4):
        board[r] = move_row_left(board[r])
    board[:] = transpose(board)

board = create_board()
add_random_tile(board)
add_random_tile(board)

@app.route("/")
def index():
    return render_template("index.html", board=board)

@app.route("/move", methods=["POST"])
def move():
    global board

    direction = request.form.get("direction")

    old_board = [row[:] for row in board]

    if direction == "left":
        move_left(board)
    elif direction == "right":
        move_right(board)
    elif direction == "up":
        move_up(board)
    elif direction == "down":
        move_down(board)
    
    if board != old_board:
        add_random_tile(board)

    return redirect("/", code=303)

if __name__ == "__main__":
    app.run(debug=False)

