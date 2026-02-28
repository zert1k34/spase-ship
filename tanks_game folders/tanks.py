import pygame
import sys
import random


pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("world of tanks(8 bit)")

clock = pygame.time.Clock()
FONT = pygame.font.SysFont(None, 36)

player_size = 20
player_color = (0, 20, 0)
player_x = width // 2 - player_size // 2
player_y = height - player_size - 10
player_speed = 5


enemy_size = 10
enemy_color = (200, 0, 0)
enemy_x = random.randint(200, width - enemy_size)
enemy_y = 50
enemy_speed = 1

score = 0

def draw_text(text, x, y):
    img = FONT.render(text, True, (255, 255, 255))
    screen.blit(img, (x, y))

close_time = True
while close_time:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_time = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < height - player_size:
        player_y += player_speed


    enemy_y += enemy_speed


    if enemy_y > height:
        enemy_y = -enemy_size
        enemy_x = random.randint(0, width - enemy_size)
        score += 1
        enemy_speed += 0.5
    

    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)

    if player_rect.colliderect(enemy_rect):
        print("Game over! Final score:", score)
        close_time = False


    screen.fill((30,30,30))
    pygame.draw.rect(screen, player_color, player_rect)
    pygame.draw.rect(screen, enemy_color, enemy_rect)
    draw_text(f"Score: {score}", 10, 10)



    pygame.display.flip()

pygame.quit()
sys.exit