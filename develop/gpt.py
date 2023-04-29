import openai
import re

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
