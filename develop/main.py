#!/usr/bin/python

import pygame
from pygame.locals import *
import sys
import typying as ty
import time

BLACK = (0, 0, 0)  # 黒色
WHITE = (255, 255, 255)  # 白色
WIDTH = 1000  # ウィンドウ横幅
HEIGHT = 600  # ウィンドウ縦幅

pygame.init()
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))    # サイズを指定して画面を作成
pygame.display.set_caption("ニコニコタイピング")    # タイトル文字を指定

background = pygame.image.load("./develop/nikoniko.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
font = pygame.font.SysFont('hgpｺﾞｼｯｸm', 30)  # 使用するフォントの設定
font2 = pygame.font.SysFont('hgpｺﾞｼｯｸm', 23)  # 使用するフォントの設定

# スタート画面の描画
def draw_start_screen():
    
    SURFACE.blit(background, (0, 0))

    text_surface = font.render("Press Space to Start", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(WIDTH/2, HEIGHT/2))
    SURFACE.blit(text_surface, text_rect)

# ゲーム画面の描画
def draw_game_screen():
    SURFACE.fill((0, 0, 0))
    SURFACE.blit(background, (0, 0))
    pygame.draw.line(SURFACE, (50,50,50), (0,510), (1000,510), 38)
    pygame.draw.line(SURFACE, (250,250,250), (0,570), (1000,570), 60)
    text_surface = font.render("TIME:", True, (0, 0, 0))
    text_surface1 = font.render("SCORE:", True, (0, 0, 0))
    text_surface2 = font.render("BONUS:", True, (0, 0, 0))

    text_rect = text_surface.get_rect(center=(800, 568))
    text_rect1 = text_surface1.get_rect(center=(80, 568))
    text_rect2 = text_surface2.get_rect(center=(300, 568))
    SURFACE.blit(text_surface, text_rect)
    SURFACE.blit(text_surface1, text_rect1)
    SURFACE.blit(text_surface2, text_rect2)

# ゲームの処理
def game():
    roma_ji = ty.roma_ji_sentence
    japanese_sentence = ty.japanese_sentence
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
        
        pygame.draw.line(SURFACE, (0,0,250), (0,510), ((elapsed_time)*1000/10,510), 38)
        
        SURFACE.blit(time_surface, time_rect)

        # ゲーム終了判定
        if remaining_time <= 0:
            SURFACE.fill((255, 255, 255))
            SURFACE.blit(background, (0, 0))
            text_surface = font.render("TIME UP", True, (0, 0, 0))
            score_surface = font.render("SCORE:", True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(WIDTH/2, 250))
            score_rect = text_surface.get_rect(center=(WIDTH/2, 350))
            SURFACE.blit(text_surface, text_rect)
            SURFACE.blit(score_surface, score_rect)
            
            pygame.display.update()
            pygame.time.wait(2000)
            break

        # 画面の更新
        pygame.display.update()


def main():
    scene=0
    # 表示更新ループ
    while True:
        if scene==0:
            draw_start_screen()
        elif scene==1:
            draw_game_screen()
        pygame.display.update()            # 画面更新
        
        # イベントを処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了（画面を閉じる）
                sys.exit()          # プログラムの終了
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_SPACE and scene==0:
                    scene=1
                    game()
                    
        
if __name__ == '__main__':
    main()