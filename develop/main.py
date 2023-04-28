#!/usr/bin/python

import pygame
from pygame.locals import *
import sys
import typying as ty

BLACK = (0, 0, 0)  # 黒色
WHITE = (255, 255, 255)  # 白色
WIDTH = 900  # ウィンドウ横幅
HEIGHT = 600  # ウィンドウ縦幅

pygame.init()
SURFACE = pygame.display.set_mode((900, 600))    # サイズを指定して画面を作成
pygame.display.set_caption("ニコニコタイピング")    # タイトル文字を指定

roma_ji = ty.roma_ji_sentence
japanese_sentence = ty.japanese_sentence

def main():
    # 表示更新ループ
    while True:
        SURFACE.fill(WHITE)          # 背景
        pygame.draw.line(SURFACE, (0,0,250), (0,493), (1000,493), 7)
        font = pygame.font.SysFont('hgpｺﾞｼｯｸm', 30)  # 使用するフォントの設定
        txt_romaji = font.render(str(roma_ji[0]), True, BLACK)
        font2 = pygame.font.SysFont('hgpｺﾞｼｯｸm', 23)  # 使用するフォントの設定
        txt_japanese = font2.render(str(japanese_sentence[0]), True, BLACK)
        # テキストの描画(表示物, (x座標, y座標))
        SURFACE.blit(txt_romaji, (
            (WIDTH / 2) - (txt_romaji.get_width() / 2),
            (HEIGHT / 2) - (txt_romaji.get_height() / 2)
        ))
        SURFACE.blit(txt_japanese, (
            (WIDTH / 2) - (txt_japanese.get_width() / 2),
            (HEIGHT / 2) - (txt_japanese.get_height() / 2)-60
        ))
        pygame.display.update()            # 画面更新
        
        # イベントを処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了（画面を閉じる）
                sys.exit()          # プログラムの終了
        
if __name__ == '__main__': main()