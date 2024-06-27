def solution(n, k):
    t_yang = n * 12000
    t_drink = (k - n // 10) * 2000 
    return t_yang + t_drink

print(solution(10, 3))
print(solution(64, 6))