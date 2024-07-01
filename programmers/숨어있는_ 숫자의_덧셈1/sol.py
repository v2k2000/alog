# 실패
my_string = "aAb1B2cC34oOp"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

answer = 0

for num in my_string:
    intnum = int(num)
    if intnum in numbers:
        answer += intnum

print(answer)