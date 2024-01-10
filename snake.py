import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake and food variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (width // 10)) * 10,
            random.randrange(1, (height // 10)) * 10]
food_spawn = True

# Directions
direction = 'RIGHT'
change_to = direction

# Initial speed
speed = 15

# Score
score = 0

# Display Score function
def show_score(choice, color, font, size):

    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score: ' + str(score), True, color)
    score_rect = score_surface.get_rect()

    if choice == 1:
        score_rect.midtop = (width / 10, 15)
    else:
        score_rect.midtop = (width / 2, height / 1.25)

    screen.blit(score_surface, score_rect)

# Display Game Over and Restart Message
def show_game_over():
    over_font = pygame.font.SysFont('times new roman', 50)
    over_surface = over_font.render('Your Score is: ' + str(score), True, red)
    over_rect = over_surface.get_rect()
    over_rect.midtop = (width / 2, height / 4)
    screen.fill(black)
    screen.blit(over_surface, over_rect)

    restart_font = pygame.font.SysFont('times new roman', 30)
    restart_surface = restart_font.render('Press R to Restart', True, white)
    restart_rect = restart_surface.get_rect()
    restart_rect.midtop = (width / 2, height / 2)
    screen.blit(restart_surface, restart_rect)

# Main Function
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_r:
                # Restart the game when 'R' is pressed after game over
                snake_pos = [100, 50]
                snake_body = [[100, 50], [90, 50], [80, 50]]
                food_pos = [random.randrange(1, (width // 10)) * 10,
                            random.randrange(1, (height // 10)) * 10]
                food_spawn = True
                direction = 'RIGHT'
                change_to = direction
                speed = 15
                score = 0

    if not food_spawn:
        food_pos = [random.randrange(1, (width // 10)) * 10,
                    random.randrange(1, (height // 10)) * 10]
        food_spawn = True

    # Draw Snake
    screen.fill(black)
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw Food
    pygame.draw.rect(screen, white, pygame.Rect(
        food_pos[0], food_pos[1], 10, 10))

    
    # Moving the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > width - 10 or snake_pos[1] < 0 or snake_pos[1] > height - 10:
        show_game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            show_game_over()

    # Displaying score
    show_score(1, white, 'consolas', 20)

    # Refresh screen
    pygame.display.update()

    # Refresh rate
    pygame.time.Clock().tick(speed)
