import re
import gptprac

answer = ('''1. [ポケモン最高！] ("Pokemon saikou!")
2. [俺もジムリーダー目指す！] ("Ore mo Jimu Ridaa mezasu!")
3. [ピカチュウ可愛すぎる！] ("Pikachuu kawaisugiru!")
4. [対戦で負けた…反省する。] ("Taisen de maketa... hansei suru.")
5. [ルカリオ大好き！] ("Lucario daisuki!")
6. [新ポケモンのデザインはどうだろう？] ("Shin Pokemon no dezain wa dou darou?")
7. [サトシがリーグ優勝するといいな。] ("Satoshi ga Rigu yuushou suru to ii na.")
8. [豆知識：ニドキングは世界最強のポケモンの一つだ。] ("Mame chishiki: Nidokingu wa sekai saikyou no Pokemon no hitotsu da.")
9. [あのポケモンはどこで手に入るの？] ("Ano Pokemon wa doko de te ni hairu no?")
10. [シンジ大好き！] ("Shinji daisuki!")''')
answer = gptprac.answer.splitlines()
print(answer)
answers = []
for i in range(len(answer)):
    new_answers = re.sub("\[.+?\]", "", answer[i])
    new_answers = re.sub("^[0-9]*.", "",new_answers)
    new_answers = re.sub("^\s", "",new_answers)
    new_answers = re.sub("\"|\"", "", new_answers)
    answers.append(new_answers)
print(answers)
print("aaa") 
for i in range(len(answers)):
    if answers[i].find(str(i+1)+'.  ') != -1:
        answers[i] = answers[i].replace(str(i+1)+'.  ','')
print(answers)