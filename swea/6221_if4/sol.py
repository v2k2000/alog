import sys
sys.stdin = open('input.txt', encoding='utf-8')

man1 = input()
man2 = input()

game = [man1, man2]
win_game = [['가위', '바위'], ['바위', '보'], ['보', '가위']]

if game in win_game:
    print('Result : Man2 Win!')
elif man1 == man2:
    print('Result : Draw')
else:
    print('Result : Man1 Win!')