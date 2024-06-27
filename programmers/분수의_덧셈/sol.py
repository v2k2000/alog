# 미완

def solution(numer1, denom1, numer2, denom2):
    
    up = (numer1 * denom2 + denom1 * numer2)
    down = (denom1 * denom2)
    
    for n in range(1, 30):
        if (up % n == 0) and (down % n == 0):
            up = up / n
            down = down / n
        else:
            continue
                
    answer = int([up, down])
    
    return answer
    
    
print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))