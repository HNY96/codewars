def find_missing(s):
    gap = s[1] - s[0]
    for i in range(len(s)):
        if gap == s[i + 1] - s[i]:
            continue
        else:
            if s[i + 1] - s[i] == gap * 2:
                return s[i] + gap
            else:
                return s[i] - gap
