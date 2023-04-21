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

question = "ポケモンに関してニコニコ動画で出てくるコメントを10個生成してください"

answer = Answer(question)

print(answer)