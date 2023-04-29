import sys
from typing import Union
import pygame as pg  # Pygameをpgという名前でインポート
import threading
import random
import modify_array


def main() -> None:
    """
    Pygameのテキスト入力処理のサンプル
    扱えるキーはアルファベット(a-z)と数字(0-9), Space, Enterのみ
    記号等は扱えない
    """
    #
    # 初期設定
    #
    pg.init()  # 全てのpygameモジュールの初期化
    WIDTH = 800  # ウィンドウ横幅
    HEIGHT = 600  # ウィンドウ縦幅
    BLACK = (0, 0, 0)  # 黒色
    WHITE = (255, 255, 255)  # 白色
    RED = (255, 0, 0)  
    question_height = 0
    #
    # ウィンドウの設定
    #
    screen = pg.display.set_mode((WIDTH, HEIGHT))  # ウィンドウの横縦を800*600に設定
    pg.display.set_caption('text input sample')  # キャプションの設定
    font = pg.font.SysFont('arial', 60)  # 使用するフォントの設定
    screen.fill(BLACK)  # ウィンドウを黒で塗りつぶす
    #
    # テキスト入力処理の初期設定
    #
    txt = font.render('|', True, WHITE)# 描画するテキスト(文字列, アンチエイリアスの有無, 色)
    player_input = font.render('', True, RED)
    question = font.render('', True, WHITE)
    # テキストの描画(表示物, (x座標, y座標))
    screen.blit(txt, (
        (WIDTH / 2) - (txt.get_width() / 2),
        (HEIGHT / 2) - (txt.get_height() / 2)
    ))
    questions = ["Aiueokakikukeko","flagchan","123467890"]  # 確定(Enter)された文字列を保持する変数
    txt_give = ''
    count = 0
    score = 0
    bonus = 1
    miss = 0
    txt_words = []  # 入力された文字を保持するリスト
    txt_tmp = ''  # 入力された1文字を一時的に保持する変数
    #
    # イベント処理
    #
    is_running = True  # イベント処理のトリガー
    pg.display.update()  # 画面更新
    start = 0
    str_x = 9999
    questions = modify_array.answers
    while questions == []:
        questions = modify_array.answers
    while(is_running):
        for event in pg.event.get():
            if event.type == pg.QUIT:  # ウィンドウの閉じるボタン押下？
                pg.quit()  # 全てのpygameモジュールの初期化を解除
                sys.exit(0)  # プログラムを終了
            #
            # テキスト入力処理(キー検知と判別)
            #
            if event.type == pg.KEYDOWN:  # キー入力検知？
                if event.key == pg.K_RETURN:  # Enter押下？
                    start = pg.time.get_ticks()
                    txt_give = questions[count]  # 文字列に直して保持
                    txt_words = []  # 初期化
                    txt_tmp = ''  # 初期化
                    str_x = screen.get_width()
                    question_height = random.uniform(-200, 200)
                    print('input \'Enter\'')  # ログ
                elif event.key == pg.K_BACKSPACE:  # BackSpace押下？
                    if not len(txt_words) == 0:  # 入力中の文字が存在するか？
                        txt_words.pop()  # 最後の文字を取り出す(削除)
                else:  # 上記以外のキーが押された時
                    txt_tmp = jud_key(event.key)
                    print(pg.key.name(event.key))
                    print(txt_tmp)
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
                            str_x = screen.get_width()
                            start = pg.time.get_ticks()
                            score += int(10 * bonus)
                            bonus += 0.1
                            question_height = random.uniform(-200, 200)
                            print("ok")
                            txt_words = []
                            count+=1
                            if count == len(questions):
                                print("おめ")
                                print(score)
                                sys.exit(0)
                            txt_give = questions[count]
                        
                #
                # テキスト入力処理(描画)
                #
                # 上書き(塗りつぶし) rect値(x, y, width, height)
                screen.fill((0,0,0,0))
                if not len(txt_words) == 0:  # 入力中のテキストがあるか？
                    player_input = font.render(''.join(txt_words), True, RED)  # テキストとカーソルを表示
                else:
                    player_input = font.render('', True, RED)
                
                pg.display.update()
                # テキストの描画(表示物, (x座標, y座標))
            
                print('txt_give : ', txt_give)  # ログ
                print('txt_words : ', txt_words)  # ログ
                print('txt_tmp : ', txt_tmp)  # ログ
                print('-------------------------')  # ログ
        screen.fill((0,0,0,0))
        question = font.render(''.join(txt_give), True, WHITE)
        screen.blit(question, (
            str_x ,
            (HEIGHT / 2 -100) - (question.get_height() / 2 + question_height)
        ))
        screen.blit(player_input, (
            str_x ,
            (HEIGHT / 2 - 100) - (player_input.get_height() / 2 + question_height)
        ))
        txt = font.render(f'score: {score}', True, WHITE)
        screen.blit(txt, (
            (WIDTH -500) ,
            (HEIGHT -100) - (txt.get_height() / 2)
        ))
        txt = font.render(f'bonus:× {bonus:.1f}', True, WHITE)
        screen.blit(txt, (
            (WIDTH -500) ,
            (HEIGHT -150) - (txt.get_height() / 2)
        ))
        txt = font.render(f'miss: {miss}', True, WHITE)
        screen.blit(txt, (
            (WIDTH -500) ,
            (HEIGHT -200) - (txt.get_height() / 2)
        ))
        txt = font.render(f'あ: {(pg.time.get_ticks() - start)//1000}', True, WHITE)
        screen.blit(txt, (
            (WIDTH-500) ,
            (HEIGHT -100) - (txt.get_height() / 2)
        ))
        str_x -= 0.1
        pg.display.update()  # 画面更新
        #print(screen.get_width())
        #print(str_x)
        if str_x < question.get_width() * -1:
            print("カッスやなｗ")
            sys.exit(0)


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
    if (key >= pg.K_a)and(key <= pg.K_z):  # アルファベットが入力された？
        if pg.key.get_mods() & pg.KMOD_SHIFT:  # Shiftキーが入力された？
            return pg.key.name(key).upper()  # 大文字
        else:
            return pg.key.name(key)  # 小文字
    elif ((key >= pg.K_0)and(key <= pg.K_9)):  # 0-9が入力された？
        if pg.key.get_mods() & pg.KMOD_SHIFT:  # Shiftキーが入力された？
            return None
        else:
            return pg.key.name(key)
    elif key == pg.K_SPACE:  # スペースが入力された？
        return ' '
    else:  # 例外？
        return None


if __name__ == '__main__':
    main()