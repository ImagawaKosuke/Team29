import gpt
import re

#ChatGPTでで促す文
question = '''ポケモンに関してニコニコ動画で出てくるコメントを10個生成してください。ただし日本語とローマ字一緒で答えてください.
さらに日本語は[]のみでくくってください。ローマ字はダブルクォーテーションのみでくくってください。'''

#サンプルの返答
answer_sample = ('''1. [ポケモン最高！] ("Pokemon saikou!")
2. [俺もジムリーダー目指す！] ("Ore mo Jimu Ridaa mezasu!")
3. [ピカチュウ可愛すぎる！] ("Pikachuu kawaisugiru!")
4. [対戦で負けた…反省する。] ("Taisen de maketa... hansei suru.")
5. [ルカリオ大好き！] ("Lucario daisuki!")
6. [新ポケモンのデザインはどうだろう？] ("Shin Pokemon no dezain wa dou darou?")
7. [サトシがリーグ優勝するといいな。] ("Satoshi ga Rigu yuushou suru to ii na.")
8. [豆知識：ニドキングは世界最強のポケモンの一つだ。] ("Mame chishiki: Nidokingu wa sekai saikyou no Pokemon no hitotsu da.")
9. [あのポケモンはどこで手に入るの？] ("Ano Pokemon wa doko de te ni hairu no?")
10. [シンジ大好き！] ("Shinji daisuki!")''')

def message_processing(question): #返答を処理する関数
    answer = gpt.Answer(question) #ChatGPTで文章を得る
    answer = answer.splitlines() #改行で分けて配列化する
    new_answers = []
    answers = [] #出力させるべき配列
    Japanese_answers = []
    JAns = []
    for i in range(len(answer)):
        Japanese_answers = re.sub("\".+?\"", "", answer[i])
        Japanese_answers = re.sub("\(.+?\)", "", answer[i])
        JAns.append(Japanese_answers)
        new_answers = re.sub("\[.+?\]", "", answer[i]) #日本語を消す
        new_answers = re.sub("\"|\"", "", new_answers) #ローマ字の文章のダブルクォーテーションを消す
        answers.append(new_answers) # answersに入れる

    return answers, JAns

#メッセージを出力する
sentence = message_processing(question)

roma_ji_sentence = sentence[0] #ローマ字
japanese_sentence = sentence[1] #日本語

print(roma_ji_sentence)
