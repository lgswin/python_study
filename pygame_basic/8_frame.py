import pygame

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


running = True
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임수

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하는가?
        if event.type == pygame.QUIT: # 종료 이벤트이면?
            running = False # running 종료 

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기

    pygame.display.update() # 게임 화면을 다시 그리기 (화면 갱신)

pygame.quit() # 종료