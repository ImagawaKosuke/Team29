import openai
import re

KEY = "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" #APIキー
openai.api_key = KEY

def Answer(question): #chatGPTで返答する関数です
    

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": question,
        }]
    )

    response = completion.choices[0].message.content

    return response

def message_processing(question): #返答を処理する関数です
    answer = Answer(question) #ChatGPTで文章を得る
    answer = answer.splitlines() #改行で分けて配列化する
    new_answers = []
    answers = [] #出力させるべき配列
    Japanese_answers = []
    JAns = []
    for i in range(len(answer)):
        Japanese_answers = re.sub("\".+?\"", "", answer[i])
        JAns.append(Japanese_answers)
        new_answers = re.sub("\[.+?\]", "", answer[i]) #日本語を消す
        new_answers = re.sub("\"|\"", "", new_answers) #ローマ字の文章のダブルクォーテーションを消す
        answers.append(new_answers) # answersに入れる

    '''    
    for i in range(len(answers)):
        if answers[i].find(str(i+1)+'.  ') != -1:
            answers[i] = answers[i].replace(str(i+1)+'.  ','')
    '''
    return answers, JAns

question = "ポケモンに関してニコニコ動画で出てくるコメントを10個生成してください。ただし日本語とローマ字一緒で答えてください.\nさらに日本語は[]のみでくくってください。ローマ字はダブルクォーテーションのみでくくってください。"

answer = message_processing(question) #呼び出し※answer[0]: ローマ字, answer[1]:日本語

print(answer[1])