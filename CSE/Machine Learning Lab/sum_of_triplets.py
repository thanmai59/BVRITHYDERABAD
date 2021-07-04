def solution(n):
    a_sum, b_sum, c_sum = [], [], []
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if isTriplet(a, b, c):
                    a_sum.append(a)
                    b_sum.append(b)
                    c_sum.append(c)
    return sum(a_sum) + sum(b_sum) + sum(c_sum)

def isTriplet(a, b, c):
    return a ** 3 + b ** 2 == c ** 2

print(solution(5))
