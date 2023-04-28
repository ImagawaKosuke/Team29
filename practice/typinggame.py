import pygame
import time

# 初期化
pygame.init()

# 画面の大きさ
screen_width = 1000
screen_height = 600

# ウィンドウの設定
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Typing Game")

# フォントの設定
font = pygame.font.Font(None, 50)
background = pygame.image.load("./develop/nikoniko.jpg")

# スタート画面の描画
def draw_start_screen():
    screen.fill((255, 255, 255))
    
    screen.blit(background, (0, 0))

    text_surface = font.render("Press Space to Start", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(screen_width/2, screen_height/2))
    screen.blit(text_surface, text_rect)

# ゲーム画面の描画
def draw_game_screen():
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    pygame.draw.line(screen, (50,50,50), (0,510), (1000,510), 38)
    pygame.draw.line(screen, (250,250,250), (0,570), (1000,570), 60)
    text_surface = font.render("TIME:", True, (0, 0, 0))
    text_surface1 = font.render("SCORE:", True, (0, 0, 0))
    text_surface2 = font.render("BONUS:", True, (0, 0, 0))
    #text_rect = text_surface.get_rect(center=(screen_width/2, screen_height/2 - 50))

    '''
    WIDTH = 1000  # ウィンドウ横幅
    HEIGHT = 600  # ウィンドウ縦幅
    '''

    text_rect = text_surface.get_rect(center=(800, 568))
    text_rect1 = text_surface1.get_rect(center=(80, 568))
    text_rect2 = text_surface2.get_rect(center=(300, 568))
    screen.blit(text_surface, text_rect)
    screen.blit(text_surface1, text_rect1)
    screen.blit(text_surface2, text_rect2)

# ゲームの処理
def game():
    start_time = time.time()
    while True:
        # イベントの処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        # ゲーム画面の描画
        draw_game_screen()

        # 残り時間の計算と表示
        elapsed_time = time.time() - start_time
        remaining_time = max(0, 10 - elapsed_time)
        time_surface = font.render("{:.2f}".format(remaining_time), True, (0, 0, 0))
        #time_rect = time_surface.get_rect(center=(screen_width/2, screen_height/2 + 50))
        time_rect = time_surface.get_rect(center=(900, 568))
        
        pygame.draw.line(screen, (0,0,250), (0,510), ((elapsed_time)*1000/10,510), 38)
        
        screen.blit(time_surface, time_rect)

        # ゲーム終了判定
        if remaining_time <= 0:
            screen.fill((255, 255, 255))
            screen.blit(background, (0, 0))
            text_surface = font.render("TIME UP", True, (0, 0, 0))
            score_surface = font.render("SCORE:", True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(screen_width/2, 250))
            score_rect = text_surface.get_rect(center=(screen_width/2, 350))
            screen.blit(text_surface, text_rect)
            screen.blit(score_surface, score_rect)
            
            pygame.display.update()
            pygame.time.wait(2000)
            break

        # 画面の更新
        pygame.display.update()

# スタート画面の描画
draw_start_screen()
pygame.display.update()

# スペースキーの待機
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            elif event.key == pygame.K_SPACE:
                game()