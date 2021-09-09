def solution(num, m):
    temp = str(num)
    count = 0
    stack = [temp[0]]
    for i in range(1, len(temp)):
        while len(stack) != 0 and temp[i] > stack[-1] and count < m:
            stack.pop()
            count += 1
        stack.append(temp[i])
    return int("".join(stack[:len(stack) - (m - count)]))


print(solution(1543241234, 3))
