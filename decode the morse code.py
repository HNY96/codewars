def decodeMorse(morse):
    morse = morse.strip()
    pre = -1
    now = 0
    result = ''
    while True:
        now = morse.find(' ', pre+1)
        if now == -1:
            if morse[pre+1:] == '':
                break
            result += MORSE_CODE[morse[pre+1:]]
            break
        if morse[now+1] != ' ':
            if morse[pre+1:now] == '':
                break
            result += MORSE_CODE[morse[pre+1:now]]
            pre = now
        else:
            if morse[pre+1:now] == '':
                break
            result += MORSE_CODE[morse[pre+1:now]]
            result += ' '
            pre = now+2
    return result