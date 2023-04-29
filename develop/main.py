#!/usr/bin/python

import pygame
from pygame.locals import *
import sys
import typying as ty
import time
from typing import Union
import threading

BLACK = (0, 0, 0)  # 黒色
WHITE = (255, 255, 255)  # 白色
RED = (255, 0, 0) 
WIDTH = 1000  # ウィンドウ横幅
HEIGHT = 600  # ウィンドウ縦幅

#ゲームの詳細
score = 0
bonus = 1
miss = 0

pygame.init()
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))    # サイズを指定して画面を作成
pygame.display.set_caption("ニコニコタイピング")    # タイトル文字を指定

background = pygame.image.load("./develop/nikoniko.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
font = pygame.font.SysFont('hgpｺﾞｼｯｸm', 30)  # 使用するフォントの設定
font2 = pygame.font.SysFont('hgpｺﾞｼｯｸm', 23)  # 使用するフォントの設定
font3 = pygame.font.SysFont(None, 100)
font4 = pygame.font.SysFont(None, 50)
start_button_surface = font4.render("Start", True, (255, 255, 255))
start_button_rect = start_button_surface.get_rect(center=(WIDTH/2, 400))

# 説明画面の描画
def draw_pre_screen():
    
    SURFACE.blit(background, (0, 0))
    start_message_surface = font3.render("Live Typing", True, (0, 255, 0))
    start_message_rect = start_message_surface.get_rect(center=(WIDTH/2, 200))
    explanation_surface = font2.render("制限時間は2分",True,(0,0,0))
    explanation_rect = explanation_surface.get_rect(center=(WIDTH/2,HEIGHT/2))
    pygame.draw.rect(SURFACE, RED, [400, 375, 200, 50])
    SURFACE.blit(start_message_surface, start_message_rect)
    SURFACE.blit(start_button_surface, start_button_rect)
    SURFACE.blit(explanation_surface, explanation_rect)

# スタート画面の描画
def draw_start_screen():
    
    SURFACE.blit(background, (0, 0))

    text_surface = font4.render("Press Space to Start", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(WIDTH/2, HEIGHT/2))
    SURFACE.blit(text_surface, text_rect)

# ゲーム画面の描画
def draw_game_screen(score,bonus,miss):
    SURFACE.fill((0, 0, 0))
    SURFACE.blit(background, (0, 0))
    pygame.draw.line(SURFACE, (50,50,50), (0,510), (1000,510), 38)
    pygame.draw.line(SURFACE, (250,250,250), (0,570), (1000,570), 60)
    text_surface = font.render(f"MISS:{miss}", True, (0, 0, 0))
    text_surface1 = font.render(f"SCORE:{score}", True, (0, 0, 0))
    text_surface2 = font.render(f"BONUS:×{bonus}", True, (0, 0, 0))

    text_rect = text_surface.get_rect(center=(500, 568))
    text_rect1 = text_surface1.get_rect(center=(80, 568))
    text_rect2 = text_surface2.get_rect(center=(300, 568))
    SURFACE.blit(text_surface, text_rect)
    SURFACE.blit(text_surface1, text_rect1)
    SURFACE.blit(text_surface2, text_rect2)

# ゲームの処理
def tgame():
    
    
    
    start_time = time.time()
    txt = font.render('|', True, BLACK)# 描画するテキスト(文字列, アンチエイリアスの有無, 色)
    
    # イベント処理
        # テキストの描画(表示物, (x座標, y座標))
    SURFACE.blit(txt, (
        (WIDTH / 2) - (txt.get_width() / 2),
        (HEIGHT / 2) - (txt.get_height() / 2)
    ))

    count = 0
    score = 0
    bonus = 1
    miss = 0
    japanese_sentence = ty.japanese_sentence
    question = ty.roma_ji_sentence
    txt_give = ''
    txt_words = []  # 入力された文字を保持するリスト
    txt_tmp = ''  # 入力された1文字を一時的に保持する変数
    # ゲーム画面の描画
    draw_game_screen(score,bonus,miss)
    pygame.display.update()  # 画面更新
    start = pygame.time.get_ticks()
    while True:
        # イベントの処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # ウィンドウの閉じるボタン押下？
                pygame.quit()  # 全てのpygameモジュールの初期化を解除
                sys.exit(0)  # プログラムを終了
            #
            # テキスト入力処理(キー検知と判別)
            #
            if event.type == pygame.KEYDOWN:  # キー入力検知？
                if event.key == pygame.K_RETURN:  # Enter押下？
                    txt_give = question[count]  # 文字列に直して保持
                    txt_words = []  # 初期化
                    txt_tmp = ''  # 初期化
                    print('input \'Enter\'')  # ログ
                elif event.key == pygame.K_BACKSPACE:  # BackSpace押下？
                    if not len(txt_words) == 0:  # 入力中の文字が存在するか？
                        txt_words.pop()  # 最後の文字を取り出す(削除)
                else:  # 上記以外のキーが押された時
                    txt_tmp = jud_key(event.key)
                    if not txt_tmp == None:  # 入力可能な文字？
                        txt_words.append(txt_tmp)  # 入力可能であれば保持する
                    if txt_give[len(txt_words) - 1:len(txt_words)] != txt_tmp:
                        print("カッスやなｗ")
                        bonus = 1
                        miss += 1
                        txt_words.pop(-1)
                    if len(txt_words) == len(txt_give):
                        start = pygame.time.get_ticks()
                        score += int(10 * bonus)
                        bonus += 0.1
                        print("ok")
                        txt_words = []
                        count+=1
                        if count == len(question):
                            print("おめ")
                            print(score)
                            sys.exit(0)
                        txt_give = question[count]
                # テキスト入力処理(描画)
                #
                # 上書き(塗りつぶし) rect値(x, y, width, height)
                txt = font.render(''.join(txt_give), True, BLACK)
                SURFACE.blit(txt, (
                    (WIDTH / 2) ,
                    (HEIGHT / 2 -100) - (txt.get_height() / 2)
                ))
                if not len(txt_words) == 0:  # 入力中のテキストがあるか？
                    txt = font.render(''.join(txt_words), True, RED)  # テキストとカーソルを表示
                else:
                    txt = font.render('', True, RED)
                SURFACE.blit(txt, (
                    (WIDTH / 2) ,
                    (HEIGHT / 2 - 100) - (txt.get_height() / 2)
                ))
                    # 残り時間の計算と表示
        elapsed_time = time.time() - start_time
        remaining_time = max(0, 180 - elapsed_time)
        time_surface = font.render("TIME:{:.2f}".format(remaining_time), True, (0, 0, 0))
        #time_rect = time_surface.get_rect(center=(screen_width/2, screen_height/2 + 50))
        time_rect = time_surface.get_rect(center=(900, 568))

        
        pygame.draw.line(SURFACE, (0,0,250), (0,510), ((elapsed_time)*1000/10,510), 38)
        
        SURFACE.blit(time_surface, time_rect)

        # ゲーム終了判定
        if remaining_time <= 0:
            SURFACE.fill((255, 255, 255))
            SURFACE.blit(background, (0, 0))
            text_surface = font.render("TIME UP", True, (0, 0, 0))
            score_surface = font.render(f"SCORE:{score}", True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(WIDTH/2, 250))
            score_rect = text_surface.get_rect(center=(WIDTH/2, 350))
            SURFACE.blit(text_surface, text_rect)
            SURFACE.blit(score_surface, score_rect)
            
            pygame.display.update()
            pygame.time.wait(2000)
            break

        # 画面の更新
        pygame.display.update()


def main() -> None:
    scene=0
    # 表示更新ループ
    while True:
        if scene==0:
            draw_pre_screen()
        elif scene==1:
            draw_start_screen()
        elif scene==2:
            tgame()
        pygame.display.update()            # 画面更新
        
        # イベントを処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了（画面を閉じる）
                sys.exit()          # プログラムの終了
            elif event.type == pygame.MOUSEBUTTONDOWN and start_button_rect.collidepoint(event.pos) and scene==0:
                # スタートボタンが押されたら、ゲームのスタート画面を表示する
                   scene=1    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_SPACE and scene==1:
                    scene=2
                    

def jud_key(key: int) -> Union[str, None]:
    """
    入力されたキーに対応する文字を返す関数
    扱えないキーが入力された場合はNoneを返す
    Pygameのキーは定数(整数)が割り当てられているので引数はint型になる
    扱える文字は以下の通り
    ・アルファベット(A-Z, a-z)
    ・数字(0-9)
    ・半角スペース
    """
    if (key >= pygame.K_a)and(key <= pygame.K_z):  # アルファベットが入力された？
        if pygame.key.get_mods() & pygame.KMOD_SHIFT:  # Shiftキーが入力された？
            return pygame.key.name(key).upper()  # 大文字
        else:
            return pygame.key.name(key)  # 小文字
    elif ((key >= pygame.K_0)and(key <= pygame.K_9)):  # 0-9が入力された？
        if pygame.key.get_mods() & pygame.KMOD_SHIFT:  # Shiftキーが入力された？
            return None
        else:
            return pygame.key.name(key)
    elif key == pygame.K_SPACE:  # スペースが入力された？
        return ' '
    elif key == pygame.K_PERIOD:
        return '.'
    elif key == pygame.K_LEFTPAREN:
        return '('
    elif key == pygame.K_RIGHTPAREN:
        return ')'
    else:  # 例外？
        return None
        
if __name__ == '__main__':
    main()