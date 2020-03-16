# strs은 단어가 담긴 배열입니다.
# 공통된 시작 단어(prefix)를 반환해주세요.  

# 예를 들어
# strs = ['start', 'stair', 'step']
# return은 'st'

# strs = ['start', 'wework', 'today']
# return은 ''

def get_prefix(string):
    if len(string)==0:
        return ''
    
    minlen = len(string[0])
    for i in range(len(string)):
        minlen = min(len(string[i]), minlen)
    
    fst =''
    i = 0
    while i < minlen:
        char = string[0][i]
        for j in range(1, len(string)):
            if string[j][i] != char:
                return fst
        
        fst = fst + char
        i += 1
    return fst