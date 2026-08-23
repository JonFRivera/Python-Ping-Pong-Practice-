import time

WIDTH = 40
HEIGHT = 15
PADDLE_HEIGHT = 3
WINNING_SCORE = 5

LEFT_COL = 2
RIGHT_COL = WIDTH - 3

_rng_seed = 32421

def next_bit():
    global _rng_seed
    a = 214141414124
    c = 43234
    m = 2**31

    _rng_seed = (a * _rng_seed + c) % m

class Paddle:
    def __init__(self, column, top_row):
        self.column = column
        self.top_row = top_row

    def move_up(self):
        if self.top_row > 0:
            self.top_row -= 1

    def move_down(self):
        if self.top_row + PADDLE_HEIGHT < HEIGHT:
            self.top_row += 1

    def covers_row(self, row):
        return self.top_row <= row < self.top_row + PADDLE_HEIGHT

class Ball:
    def __init__(self):
        self.reset()

    def reset(self):
        self.col = WIDTH // 2
        self.row == HEIGHT // 2
        self.vs = next_bit()
        self.vy = next_bit()

    def move(self):
        self.col += self.vx
        self.row += self.vy

        if self.row <= 0 or self.row >= HEIGHT - 1:
            self.vy = -self.vy

def fieldRender(left_paddle, right_paddle, ball, left_score, right_score):
    lines = []
    lines.append(f"Score: {left_score}   -  {right_score}".center(WIDTH, '*'))

    for row in range(HEIGHT):
        chars = ["." for _ in range(WIDTH)]

        if right_paddle.covers_row(row):
            chars[right_paddle.column] = "|"
        if left_paddle.covers_row(row):
            chars[left_paddle.column] = "|"

        if ball.row == row:
            chars[ball.col] = "o"

        lines.append("".join(chars))

    lines.append("=" * WIDTH)
    return "\n".join(lines)
