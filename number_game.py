import random

def main():
print("=== 数当てゲーム ===")
number = random.randint(1, 20)
attempts = 0

while True:
guess = input("1から20までの数字を予想してね: ")
attempts += 1

# 入力チェック
if not guess.isdigit():
print("数字を入力してください！")
continue

guess = int(guess)
if guess < number:
print("もっと大きいよ！")
elif guess > number:
print("もっと小さいよ！")
else:
print(f"正解！ {attempts}回で当てたね！")
break

if __name__ == "__main__":
main()
