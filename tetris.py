import pygame
import random

# Константы
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
BOARD_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
BOARD_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (255, 255, 0),  # Yellow
    (255, 165, 0),  # Orange
    (128, 0, 128),  # Purple
    (0, 255, 255)  # Cyan
]

# Фигуры тетромино
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
]

class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = BOARD_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

class Tetris:
    def __init__(self):
        self.board = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
        self.current_tetromino = Tetromino()
        self.score = 0

    def collide(self, dx, dy):
        for y, row in enumerate(self.current_tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.current_tetromino.x + x + dx
                    new_y = self.current_tetromino.y + y + dy
                    if new_x < 0 or new_x >= BOARD_WIDTH or new_y >= BOARD_HEIGHT or self.board[new_y][new_x]:
                        return True
        return False

    def merge_tetromino(self):
        for y, row in enumerate(self.current_tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.current_tetromino.y + y][self.current_tetromino.x + x] = self.current_tetromino.color

    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.board) if all(row)]
        for i in lines_to_clear:
            del self.board[i]
            self.board.insert(0, [0] * BOARD_WIDTH)
            self.score += 100

    def drop(self):
        if not self.collide(0, 1):
            self.current_tetromino.y += 1
        else:
            self.merge_tetromino()
            self.clear_lines()
            self.current_tetromino = Tetromino()
            if self.collide(0, 0):
                return True  # Игра окончена
        return False

    def move(self, dx):
        if not self.collide(dx, 0):
            self.current_tetromino.x += dx

    def rotate(self):
        self.current_tetromino.rotate()
        if self.collide(0, 0):
            self.current_tetromino.rotate()  # Вернуть назад, если столкновение

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.tetris = Tetris()
        self.running = True

    def draw_board(self):
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                if self.tetris.board[y][x]:
                    pygame.draw.rect(self.screen, self.tetris.board[y][x],
                                     (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        for y, row in enumerate(self.tetris.current_tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, self.tetris.current_tetromino.color,
                                     ((self.tetris.current_tetromino.x + x) * BLOCK_SIZE,
                                      (self.tetris.current_tetromino.y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.tetris.move(-1)
                    if event.key == pygame.K_RIGHT:
                        self.tetris.move(1)
                    if event.key == pygame.K_DOWN:
                        self.tetris.drop()
                    if event.key == pygame.K_UP:
                        self.tetris.rotate()

            self.tetris.drop()
            self.screen.fill(BLACK)
            self.draw_board()
            pygame.display.flip()
            self.clock.tick(2)

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()