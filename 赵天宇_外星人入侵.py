import pygame
import random

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("外星人入侵")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

player_width = 100
player_height = 20
player_speed = 5

alien_width = 50
alien_height = 30
alien_speed = 3
alien_drop_speed = 10

bullet_width = 5
bullet_height = 10
bullet_speed = 7

player_img = pygame.Surface((player_width, player_height))
player_img.fill(white)

alien_img = pygame.Surface((alien_width, alien_height))
alien_img.fill(red)

bullet_img = pygame.Surface((bullet_width, bullet_height))
bullet_img.fill(white)

def draw_player(x, y):
    screen.blit(player_img, (x, y))

def draw_alien(x, y):
    screen.blit(alien_img, (x, y))

def draw_bullet(x, y):
    screen.blit(bullet_img, (x, y))

def game_loop():
    # 玩家初始化
    player_x = (screen_width - player_width) / 2
    player_y = screen_height - player_height - 10
    player_x_change = 0

    # 外星人初始化
    alien_x = random.randint(0, screen_width - alien_width)
    alien_y = 0
    alien_x_change = alien_speed
    alien_y_change = alien_drop_speed

    # 子弹初始化
    bullet_x = -1
    bullet_y = player_y
    bullet_state = "ready"

    # 游戏
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # 控制玩家移动
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_SPACE] and bullet_state == "ready":
            bullet_x = player_x + (player_width / 2) - (bullet_width / 2)
            bullet_y = player_y
            bullet_state = "fire"

        # 更新玩家位置
        player_x = max(0, min(player_x, screen_width - player_width))

        # 更新外星人位置
        alien_x += alien_x_change
        if alien_x <= 0 or alien_x >= screen_width - alien_width:
            alien_x_change *= -1
            alien_y += alien_y_change

        # 更新子弹位置
        if bullet_state == "fire":
            bullet_y -= bullet_speed
            draw_bullet(bullet_x, bullet_y)
            if bullet_y <= 0:
                bullet_state = "ready"

        # 碰撞检测
        if (alien_x < bullet_x < alien_x + alien_width or alien_x < bullet_x + bullet_width < alien_x + alien_width) and (alien_y < bullet_y < alien_y + alien_height):
            alien_x = random.randint(0, screen_width - alien_width)
            alien_y = 0
            bullet_state = "ready"

        # 绘制游戏对象
        draw_player(player_x, player_y)
        draw_alien(alien_x, alien_y)

        pygame.display.update()
        clock.tick(30)

game_loop()
