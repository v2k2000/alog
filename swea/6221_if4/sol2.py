import sys
sys.stdin = open('input.txt', encoding='utf-8')

man1 = input()
man2 = input()


rcp = ['바위', '가위', '보']
#       0       1      2

man1_idx = rcp.index(man1)
man2_idx = rcp.index(man2)

result = man1_idx - man2_idx

if result == 0:
    print('Result : Draw')
elif result == -1 or 2:
    print('Result : Man2 Win!')
elif result == 1 or 2:
    print('Result : Man1 Win!')