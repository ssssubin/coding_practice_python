def solution(s):
    arr = []
    for num in s.split(" "):
        arr.append(int(num))
    min_num = min(arr)
    max_num = max(arr)
    return f"{min_num} {max_num}"