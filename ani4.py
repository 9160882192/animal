import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake setup
block_size = 20
snake = [(WIDTH // 2, HEIGHT // 2)]
snake_dir = (0, 0)

# Food setup
food = (random.randint(0, (WIDTH // block_size) - 1) * block_size,
        random.randint(0, (HEIGHT // block_size) - 1) * block_size)

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, block_size):
        snake_dir = (0, -block_size)
    if keys[pygame.K_DOWN] and snake_dir != (0, -block_size):
        snake_dir = (0, block_size)
    if keys[pygame.K_LEFT] and snake_dir != (block_size, 0):
        snake_dir = (-block_size, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-block_size, 0):
        snake_dir = (block_size, 0)

    # Update snake
    if snake_dir != (0, 0):
        new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
        snake.insert(0, new_head)
        if new_head == food:
            food = (random.randint(0, (WIDTH // block_size) - 1) * block_size,
                    random.randint(0, (HEIGHT // block_size) - 1) * block_size)
        else:
            snake.pop()

        # Check collision
        if (new_head[0] < 0 or new_head[0] >= WIDTH or
                new_head[1] < 0 or new_head[1] >= HEIGHT or
                new_head in snake[1:]):
            print("Game Over!")
            running = False

    # Draw everything
    screen.fill(BLACK)
    for block in snake:
        pygame.draw.rect(screen, GREEN, (*block, block_size, block_size))
    pygame.draw.rect(screen, RED, (
