import sys
from typing import Union
import pygame as pg  # Pygameをpgという名前でインポート


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
    # テキストの描画(表示物, (x座標, y座標))
    screen.blit(txt, (
        (WIDTH / 2) - (txt.get_width() / 2),
        (HEIGHT / 2) - (txt.get_height() / 2)
    ))
    txt_give = ''  # 確定(Enter)された文字列を保持する変数
    txt_words = []  # 入力された文字を保持するリスト
    txt_tmp = ''  # 入力された1文字を一時的に保持する変数
    #
    # イベント処理
    #
    is_running = True  # イベント処理のトリガー
    pg.display.update()  # 画面更新
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
                    txt_give = ''.join(txt_words)  # 文字列に直して保持
                    txt_words = []  # 初期化
                    txt_tmp = ''  # 初期化
                    print('input \'Enter\'')  # ログ
                elif event.key == pg.K_BACKSPACE:  # BackSpace押下？
                    if not len(txt_words) == 0:  # 入力中の文字が存在するか？
                        txt_words.pop()  # 最後の文字を取り出す(削除)
                else:  # 上記以外のキーが押された時
                    txt_tmp = jud_key(event.key)
                    if not txt_tmp == None:  # 入力可能な文字？
                        txt_words.append(txt_tmp)  # 入力可能であれば保持する
                #
                # テキスト入力処理(描画)
                #
                # 上書き(塗りつぶし) rect値(x, y, width, height)
                screen.fill(BLACK, (
                    (WIDTH / 2) - (txt.get_width() / 2),
                    (HEIGHT / 2) - (txt.get_height() / 2),
                    txt.get_width(),
                    txt.get_height()
                ))
                if not len(txt_words) == 0:  # 入力中のテキストがあるか？
                    txt = font.render(''.join(txt_words) + '|', True, WHITE)  # テキストとカーソルを表示
                else:
                    txt = font.render('|', True, WHITE)  # カーソルだけを表示
                # テキストの描画(表示物, (x座標, y座標))
                screen.blit(txt, (
                    (WIDTH / 2) - (txt.get_width() / 2),
                    (HEIGHT / 2) - (txt.get_height() / 2)
                ))
                pg.display.update()  # 画面更新
                print('txt_give : ', txt_give)  # ログ
                print('txt_words : ', txt_words)  # ログ
                print('txt_tmp : ', txt_tmp)  # ログ
                print('-------------------------')  # ログ


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