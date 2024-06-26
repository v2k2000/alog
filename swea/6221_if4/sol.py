import sys
sys.stdin = open('input.txt', encoding='utf-8')

man1 = input()
man2 = input()

if (man1, man2) == ('가위', '바위') or ('바위', '보') or ('보', '가위'):
    print('Result : Man2 Win!')
elif 'man1' == 'man2':
    print('Result : Draw')
else:
    print('Result : Man1 Win!')