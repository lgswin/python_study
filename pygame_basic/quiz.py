import pygame
import random
#############################################################################################
# 기본 초기화 (반드시 해야하는것들)
pygame.init() # 초기화

# 화면크기 설정
screen_width = 480 # 가로
screen_hight = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_hight))

# 화면 타이틀
pygame.display.set_caption("GS game") 

# FPS
clock = pygame.time.Clock()
#############################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임이미지, 좌표, 폰트 등)
background = pygame.image.load("C:\\pythonWorkspace\\pygame_basic\\background.png")
character = pygame.image.load("C:\\pythonWorkspace\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width- character_width) / 2  # 화면 가로의 절반 크기의 위치에 
character_y_pos = screen_hight - character_height  # 맨 밑에 위치

# 이동할 좌표
to_x = 0
character_speed = 10

# 똥 만들기
ddong = pygame.image.load("C:\\pythonWorkspace\\pygame_basic\\enemy.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0] # 캐릭터의 가로 크기
ddong_height = ddong_size[1] # 캐릭터의 세로 크기
ddong_x_pos = random.randint(0, screen_width-ddong_width)
ddong_y_pos = 0
ddong_speed = 10


running = True
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임수

    # 2. 이벤트 처리 (키보드, 마우스 등)

    for event in pygame.event.get(): # 어떤 이벤트가 발생하는가?
        if event.type == pygame.QUIT: # 종료 이벤트이면?
            running = False # running 종료 


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    ddong_y_pos += ddong_speed

    if ddong_y_pos > screen_hight:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos # 실제 character위치 정보로 갱신
    character_rect.top = character_y_pos # 실제 character위치 정보로 갱신
    
    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos # 위치가 고정이지만 한번이라도 위치값 반영이 있어야 아래 위치 체크 조건에 걸림. 
    ddong_rect.top = ddong_y_pos

    if character_rect.colliderect(ddong_rect):
        print("충돌했어요")
        running = False

    # 5. 화면에 그리기

    screen.blit(background, (0,0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))

    pygame.display.update() # 게임 화면을 다시 그리기 (화면 갱신)

pygame.quit() # 종료