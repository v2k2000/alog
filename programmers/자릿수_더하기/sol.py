# 실패
# 함수 설정
def solution(n):
    #  엔서
    answer = 0
    # n을 문자열로
    strn = str(n)
    # 문자열의 각 인덱스에 대하여 값을 합산
    answer = sum(strn)
    return answer

# 해답
def solution(n):
    while  n > 0:
        a,b = divmod(n, 10)
        n = a
        answer += b
    return answer

