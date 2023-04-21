import time, random,string

def random_string_generator(size=20, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

validator = False
sentence = "何文字にチャレンジしますか？-> "
while not validator:
    char_size = input(sentence)
    try:
        char_size = int(char_size)
        if char_size <= 50:
            validator = True
        else:
            sentence = "問題は50文字以内で入力下さい -> "
    except:
        sentence = "数値を入力下さい"

question = random_string_generator(size=char_size)
print(question)
q_sentence = "上記の文字を入力 -> "
try_num = 1
start = time.time()
game_done = False
while not game_done:
    answer = input(q_sentence)
    if answer == question:
        game_done = True
    else:
        try_num += 1
        print(question)
        q_sentence = f"再チャレンジ({try_num}回目)-> " 
finish = time.time()
total_time = finish-start
rounded_time = round(total_time, 2)

last_sentence = ""
if try_num ==1:
    last_sentence = f"一度も間違えずにできました。{rounded_time}秒でクリアしました！"
else:
    last_sentence = f"{try_num}回目のチャレンジで成功！{rounded_time}秒でクリアしました！"
print(last_sentence)
