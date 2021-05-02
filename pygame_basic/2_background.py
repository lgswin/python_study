import pygame

pygame.init() # 초기화

# 화면크기 설정
screen_width = 480 # 가로
screen_hight = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_hight))

# 화면 타이틀
pygame.display.set_caption("GS game") 

# 배경이미지 불러오기
background = pygame.image.load("C:\\pythonWorkspace\\pygame_basic\\background.png") # \ 하나는 탈출문자 (개행) 으로 처리되므로 \\ 로 해주거나 / 로 바꿔줘야함

# 이벤트 루프
running = True
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하는가?
        if event.type == pygame.QUIT: # 종료 이벤트이면?
            running = False # running 종료 

    screen.blit(background, (0,0)) # 배경 그리기
    #screen.fill((0,0,255)) # 백그라운드 색상 채우기로도 배경색을 정할 수 있다.

    pygame.display.update() # 게임 화면을 다시 그리기 (화면 갱신)

pygame.quit() # 종료