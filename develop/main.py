#!/usr/bin/python

import pygame
from pygame.locals import *
import sys
import typying as ty
import time
from typing import Union
import threading
import random
import gpt

BLACK = (0, 0, 0)  # 黒色
WHITE = (255, 255, 255)  # 白色
RED = (255, 0, 0) 
WIDTH = 1000  # ウィンドウ横幅
HEIGHT = 600  # ウィンドウ縦幅
question_height = 0

#ゲームの詳細
score = 0
bonus = 1
miss = 0

pygame.init()
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))    # サイズを指定して画面を作成
pygame.display.set_caption("Live Typing")    # タイトル文字を指定
background = pygame.image.load("./develop/nikoniko.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background2 = pygame.transform.chop(background, pygame.Rect(0,0,WIDTH, 500))
title = pygame.image.load("./develop/title.png")
font = pygame.font.SysFont('hgpｺﾞｼｯｸm', 30)  # 使用するフォントの設定

question = '''ニコニコ動画で出てくるコメントを15文字程度で10個生成してください。
条件:
・ローマ字のみで答えてください.
・入力にShiftキーを使う必要がある文字と記号(!や~など)は使わないでください。
・アルファベットとスペースのみの返答でお願いします。
・ローマ字はダブルクウォーテーションのみでくくってください。'''

answer_res = gpt.Answer(question)
print(answer_res)
# スタート画面の描画
def draw_start_screen():
    
    SURFACE.blit(background, (0, 0))
    SURFACE.blit(title, (0, 0))
    text_surface = font.render("Press Space to Start", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(WIDTH/2, HEIGHT/2))
    SURFACE.blit(text_surface, text_rect)

# ゲーム画面の描画
def draw_game_screen(score,bonus,miss):
    SURFACE.fill(WHITE)
    #SURFACE.blit(background, (0, 0))
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
    # イベント処理

    count = 0
    score = 0
    bonus = 1
    miss = 0
    question_height = 0
    questions = ty.message_processing(answer_res)
    player_input = font.render('', True, RED)
    question = font.render('', True, BLACK)
    txt_give = ''
    txt_words = []  # 入力された文字を保持するリスト
    txt_tmp = ''  # 入力された1文字を一時的に保持する変数
    
    start = 0
    str_x = 9999
    draw_game_screen(score,bonus,miss)
    pygame.display.update()  # 画面更新
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
                    start = pygame.time.get_ticks()
                    txt_give = questions[count]
                    txt_words = [' ']  # 初期化
                    txt_tmp = ''  # 初期化
                    str_x = SURFACE.get_width()
                    question_height = random.uniform(-200, 200)
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
                        print(txt_tmp)
                        if (txt_tmp != None):
                            txt_words.pop(-1)
                    if len(txt_words) == len(txt_give):
                        start = pygame.time.get_ticks()
                        score += int(10 * bonus)
                        bonus += 0.1
                        question_height = random.uniform(-200, 200)
                        print("ok")
                        txt_words = [' ']
                        count+=1
                        if count == len(questions):
                            print("おめ")
                            print(score)
                            sys.exit(0)
                        txt_give = questions[count]
                # テキスト入力処理(描画)

                if not len(txt_words) == 0:  # 入力中のテキストがあるか？
                    player_input = font.render(''.join(txt_words), True, RED)  # テキストとカーソルを表示
                else:
                    player_input = font.render('', True, RED)
                
                pygame.display.update()
                # テキストの描画(表示物, (x座標, y座標))
            
                print('txt_give : ', txt_give)  # ログ
                print('txt_words : ', txt_words)  # ログ
                print('txt_tmp : ', txt_tmp)  # ログ
                print('-------------------------')  # ログ
                #
                # 上書き(塗りつぶし) rect値(x, y, width, height)
        SURFACE.blit(background2, (0, 0, 0, 0))
        question = font.render(''.join(txt_give), True,BLACK)
        SURFACE.blit(question, (
            str_x ,
            (HEIGHT / 2 -100) - (question.get_height() / 2 + question_height)
        ))
        
        SURFACE.blit(player_input, (
            str_x ,
            (HEIGHT / 2 - 100) - (player_input.get_height() / 2 + question_height)
        ))
        str_x -= 0.1
        
        pygame.display.update()  # 画面更新
        if str_x < question.get_width() * -1:
            print("カッスやなｗ")
            sys.exit(0)
            # 残り時間の計算と表示
        elapsed_time = time.time() - start_time
        remaining_time = max(0, 180 - elapsed_time)
        time_surface = font.render(f'TIME: {(pygame.time.get_ticks() - start)//1000}', True, (0, 0, 0))
        #time_rect = time_surface.get_rect(center=(screen_width/2, screen_height/2 + 50))
        time_rect = time_surface.get_rect(center=(900, 568))
        
        pygame.draw.line(SURFACE, (0,0,250), (0,510), ((elapsed_time)*1000/10,510), 38)
        
        SURFACE.blit(time_surface, time_rect)

        # ゲーム終了判定
        if remaining_time <= 0:
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
        
        


def main() -> None:
    scene=0
    # 表示更新ループ
    while True:
        if scene==0:
            draw_start_screen()
        elif scene==1:
            tgame()
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
    elif key == pygame.K_COMMA:
        return ','
    elif key == pygame.K_MINUS:
        return '-'
    else:  # 例外？
        return None
        
if __name__ == '__main__':
    main()