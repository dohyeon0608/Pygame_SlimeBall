import pygame
from player import Player
from stage import Stage
from block import Block

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
FPS = 60

# 화면 타이틀 설정
pygame.display.set_caption("Slime Ball")




running = True
moving_dir = []

test_map: Stage = Stage.from_stage_file(file='maps/testmap_old', start_point=(3, 13))
print(test_map.blocks)



blocks = test_map.get_game_blocks()
block_group = pygame.sprite.Group(blocks)

player = Player(position=(100, 300), block_group=block_group, item_group=pygame.sprite.Group(), speed=0.05)
players = pygame.sprite.Group(player)  
player.teleport(Stage.pos_converter(pos=test_map.start_point))

game_font = pygame.font.SysFont('Noto Sans KR ExtraBold', 60)
info_font = pygame.font.SysFont('Noto Sans KR', 15)
is_cleared = False

while running:
    dt = clock.tick(FPS) # 게임 화면의 초당 프레임 수를 설정

    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_dir.append(Player.LEFT)
            elif event.key == pygame.K_RIGHT:
                moving_dir.append(Player.RIGHT)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_dir.remove(Player.LEFT)
            elif event.key == pygame.K_RIGHT:
                moving_dir.remove(Player.RIGHT)

    for dir in moving_dir:
        player.move(dir, FPS)

    # 바닥 충돌 감지
    player.rect.y += player.velocity
    player.update()

    Fnet = player.force
    player.velocity += Fnet 

    screen.fill((255, 255, 255))
    block_group.draw(screen)
    players.draw(screen)

    if (player.rect.y > screen_height or player.energy <= 0):
        render = game_font.render("게임 오버!", True, (255, 0, 0))
        player.velocity = 20 if player.velocity > 20 else player.velocity
        screen.blit(render, (screen_width / 2, screen_height / 2))
    
    if player.energy > 0: player.energy -= 0.1 # 실전에서는 더 느리게
    if player.energy <= 0: player.energy = 0
    collisions: list[Block] = pygame.sprite.spritecollide(player, block_group, False)
    for collision in collisions:
        if collision.type == 1:
            A = player.rect.bottom > collision.rect.top
            B = player.rect.top > collision.rect.bottom
            if A:
                player.velocity = -5 * (player.energy / 100)
                player.rect.y = collision.rect.top - 30
                
                print(player.velocity)
            if  player.rect.left < collision.rect.right:
                player.rect.right = collision.rect.left - 1

            if  player.rect.right > collision.rect.left:
                player.rect.left = collision.rect.right + 1
            if B:
                player.velocity = 0.3
        if collision.type == 2:
            block_group.remove(collision)
            is_cleared = True

    if is_cleared:
        render = game_font.render("클리어 ㅊㅊ", True, (234, 191, 21))
        screen.blit(render, (screen_width / 2, screen_height / 2))

    screen.blit(info_font.render("ENERGY: {:.1f}%".format(player.energy), True, (0, 0, 0)), (10, 10))

    pygame.display.update() # 게임 화면을 다시 그리기