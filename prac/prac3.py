import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# 배경 이미지 불러오기
background = pygame.image.load('C:/Users/김도현/Desktop/VSC Projects/PyGame/prac/background.png')

# 캐릭터(스프타리트) 불러오기
character = pygame.image.load('C:/Users/김도현/Desktop/VSC Projects/PyGame/prac/character.png')
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width)/ 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치



# 이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프
is_running = True

while is_running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            is_running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 1
            elif event.key == pygame.K_RIGHT:
                to_x += 1
            elif event.key == pygame.K_UP:
                to_y -= 1
            elif event.key == pygame.K_DOWN:
                to_y += 1
        
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                to_x = 0
            elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    # 가로 경곗값
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # screen.fill((0, 255, 255))
    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 게임 화면을 다시 그리기

# pygame 종료
pygame.quit()