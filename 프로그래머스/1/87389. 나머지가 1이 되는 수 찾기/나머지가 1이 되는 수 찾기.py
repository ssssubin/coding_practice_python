def solution(n):
    x= [i for i in range(1,n + 1)]
    result = []
    for i in range(len(x)):
        if n % x[i] == 1:
            result.append(x[i])
    return min(result)