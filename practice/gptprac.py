import openai

KEY = "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"
openai.api_key = KEY

def Answer(question):
    

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": question,
        }]
    )

    response = completion.choices[0].message.content

    return response
question = "ポケモンに関してニコニコ動画で出てくるコメントを15文字程度で10個生成してください。ただしローマ字で答えてください.入力にShiftキーを使う必要がある文字と記号は使わないでください。さらにローマ字はダブルクウォーテーションのみでくくってください。"

#question = "ポケモンに関してニコニコ動画で出てくるコメントを15文字程度で10個生成してください。ただし日本語とローマ字一緒で答えてください.入力にShiftキーを使う必要がある文字と記号は使わないでください。さらに日本語は[]のみでくくってください。ローマ字はダブルクウォーテーションのみでくくってください。"

answer = Answer(question)

print(answer)
print("x")