def solution(s: str):
    max_sub_len = 0
    res = ""
    left = 0
    right = 2
    for right in range(2, len(s)):
        if s[right] != s[right - 1] or s[right - 1] != s[right - 1]:
            continue
        else:
            sub_len = right - left + 1
            if sub_len > max_sub_len:
                max_sub_len = sub_len
                res = s[left:right+1]
            left = right - 1
    if right - left + 1 > max_sub_len:
        res = s[left:right+1]
    return res


if __name__ == '__main__':
    print(solution("aaabccc"))
