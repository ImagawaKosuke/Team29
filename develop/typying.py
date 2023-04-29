import gpt
import re

#ChatGPTでで促す文
question = '''ポケモンに関してニコニコ動画で出てくるコメントを15文字程度で10個生成してください。
ただしローマ字のみで答えてください.入力にShiftキーを使う必要がある文字と記号は使わないでください。
アルファベットとスペースのみの記述でお願いします。さらにローマ字はダブルクウォーテーションのみでくくってください。'''

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

def message_processing(answer): #返答を処理する関数
    
    answer = answer.splitlines() #改行で分けて配列化する
    new_answers = []
    answers = [] #出力させるべき配列
    
    for i in range(len(answer)):
        if re.search(r'[ぁ-ん]+|[ァ-ヴー]+',answer[i]):
            answer = []
            break
        new_answers = re.sub("\[.+?\]", "", answer[i]) #日本語を消す
        new_answers = re.sub("^[0-9]*.", "",new_answers)
        new_answers = re.sub("[\!\.\?\~]", "",new_answers)
        new_answers = re.sub("^\s", "",new_answers)
        new_answers = re.sub("$\s", "",new_answers)
        new_answers = re.sub("\(|\)", "", new_answers)
        new_answers = re.sub("\"|\"", "", new_answers) #ローマ字の文章のダブルクォーテーションを消す
        answers.append(new_answers) # answersに入れる
        if answers[i].find(str(i+1)+'.  ') != -1:
            answers[i] = answers[i].replace(str(i+1)+'.  ','')
        if answers[i].find(str(i+1)+'! ') != -1:
            answers[i] = answers[i].replace(str(i+1)+'! ','')
    return answers


#メッセージを出力する
answer_res = gpt.Answer(question) #ChatGPTで文章を得る
roma_ji_sentence = message_processing(answer_res) #ローマ字

#roma_ji_sentence = message_processing(answer_sample) #ローマ字
#japanese_sentence = message_japanese(answer_sample) #日本語