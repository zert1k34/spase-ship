import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pygame Game")

clock = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 36)

# Player settings
player_size = 40
player_color = (0, 200, 0)
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 5

# Enemy settings
enemy_size = 40
enemy_color = (200, 0, 0)
# enemy_x = random.randint(0, WIDTH - enemy_size)
# enemy_y = -enemy_size
enemy_speed = 4
enemies = []
enemies.append([100,10])
enemies.append([150,11])

score = 0

def draw_text(text, x, y):
    img = FONT.render(text, True, (255, 255, 255))
    screen.blit(img, (x, y))

running = True
while running:

    clock.tick(60)  # 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_size:
        player_y += player_speed

    #enemy += enemies

    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    screen.fill((30, 30, 30))

    for enemy in enemies:
        enemy_y = enemy[1]
        enemy_x = enemy[0]
    # Move enemy
        enemy_y += enemy_speed
        
        # Respawn enemy and increase score
        if enemy_y > HEIGHT:
            enemy_y = -enemy_size
            
            enemy_x = random.randint(0, WIDTH - enemy_size)
            score += 1
            
        enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
        if player_rect.colliderect(enemy_rect):
            print("Game Over! Final score:", score)
            running = False
        pygame.draw.rect(screen, enemy_color, enemy_rect)
        enemy[1] = enemy_y
        enemy[0] = enemy_x

    # Collision detection
        

    # Player hit
   


    # Drawing
    pygame.draw.rect(screen, player_color, player_rect)



    draw_text(f"Score: {score}", 10, 10)
    pygame.display.flip()

pygame.quit()
sys.exit()