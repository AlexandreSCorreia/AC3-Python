def enigma1():
    m = 0
    while True:
        n = int(input('número: '))
        if n < 0: break
        m += n
    return m

def enigma2():
    m = 0
    while True:
        n = int(input('número: '))
        if n < 0: continue
        m += n
    return m

enigma2()

