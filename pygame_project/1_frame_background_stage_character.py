import pygame
import os

#############################################################################################
# 기본 초기화 (반드시 해야하는것들)
pygame.init() # 초기화

# 화면크기 설정
screen_width = 640 # 가로
screen_hight = 480 # 세로
screen = pygame.display.set_mode((screen_width, screen_hight))

# 화면 타이틀
pygame.display.set_caption("GS game 01") 

# FPS
clock = pygame.time.Clock()
#############################################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임이미지, 좌표, 폰트 등)
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# stage 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지의 높이 위에 캐릭터를 두기 위해 사용

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0] 
character_height = character_size[1]
character_x_pos = screen_width/2 - character_width/2
character_y_pos = screen_hight - character_height - stage_height

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
    screen.blit(background, (0,0))
    screen.blit(stage, (0, screen_hight-stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 게임 화면을 다시 그리기 (화면 갱신)

pygame.quit() # 종료