def solution(n):
    answer = sum(range(2, n + 1, 2))
    return answer


print(solution(10))
print(solution(4))
print(solution(1))
print(solution(0))
#  => 30
#  => 6 