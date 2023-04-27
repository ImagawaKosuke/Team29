import openai


KEY = "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" #APIキー
openai.api_key = KEY

def Answer(question): #chatGPTで返答する関数
    

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": question,
        }]
    )

    response = completion.choices[0].message.content

    return response



question = "ポケモンに関してニコニコ動画で出てくるコメントを10個生成してください。ただし日本語とローマ字一緒で答えてください.\nさらに日本語は[]のみでくくってください。ローマ字はダブルクォーテーションのみでくくってください。"

answer = Answer(question) #呼び出し※answer[0]: ローマ字, answer[1]:日本語

print(answer[1])
