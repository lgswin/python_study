import pygame

pygame.init() # 초기화

# 화면크기 설정
screen_width = 480 # 가로
screen_hight = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_hight))

# 화면 타이틀
pygame.display.set_caption("GS game") 

# FPS
clock = pygame.time.Clock()

# 배경이미지 불러오기
background = pygame.image.load("C:\\pythonWorkspace\\pygame_basic\\background.png") # \ 하나는 탈출문자 (개행) 으로 처리되므로 \\ 로 해주거나 / 로 바꿔줘야함

# 캐릭터 불러오기
character = pygame.image.load("C:\\pythonWorkspace\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width- character_width) / 2  # 화면 가로의 절반 크기의 위치에 
character_y_pos = screen_hight - character_height  # 맨 밑에 위치

# 이동할 좌표
to_x = 0
to_y = 0

character_speed = 0.7

# 적 캐릭터 만들기
enemy = pygame.image.load("C:\\pythonWorkspace\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = (screen_width- enemy_width) / 2  # 화면 가로의 절반 크기의 위치에 
enemy_y_pos = (screen_hight - enemy_height) / 2  # 가운데 위치

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 게임 총 시간
total_time = 10

# 시간 계산
start_tikcs = pygame.time.get_ticks() # 시작 tick(시간) 을 받아옴


# 이벤트 루프
running = True
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임수

    # 10 fps : 1 초 동안 10번 동작 -> 1번에 몇만큼 이동? 10만큼 ! 10*10 = 100
    # 20 fps : 1 초 동안 20번 동작 -> 1번에 5만큼 ? 5*10 = 50

    print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get(): # 어떤 이벤트가 발생하는가?
        if event.type == pygame.QUIT: # 종료 이벤트이면?
            running = False # running 종료 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt # dt(delta) 를 곱해주면 fps 에 상관없이 이동 속도 보정이 됨 
    character_y_pos += to_y * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_hight - character_height:
        character_y_pos = screen_hight - character_height

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos # 실제 character위치 정보로 갱신
    character_rect.top = character_y_pos # 실제 character위치 정보로 갱신
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos # 위치가 고정이지만 한번이라도 위치값 반영이 있어야 아래 위치 체크 조건에 걸림. 
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False


    screen.blit(background, (0,0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # 타이머 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_tikcs) / 1000 # ms 이므로 1000으로 나누어 초단위로 변환
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255)) # 정수형으로 표현하기위해 int로 변환
    # 시간, Antialias(true), 글자색상 을 인자로 받음

    screen.blit(timer, (10, 10))

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update() # 게임 화면을 다시 그리기 (화면 갱신)

# 잠시 대기
pygame.time.delay(2000) # 들여쓰기 에 따라 상위에 종속되냐 아니냐가 달라짐 즉, delay를 들여쓰기하면 위 같은 column의 코드들이 다 영향을 받음.

pygame.quit() # 종료