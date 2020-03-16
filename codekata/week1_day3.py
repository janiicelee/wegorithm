#String 형인 str 인자에서 중복되지 않은 알파벳으로 이루어진 제일 긴 단어의 길이를 반환해주세요.
#str = "abcabcabc" return은 3
#=> 'abc' 가 제일 길기 때문

#str = "aaaaa" return은 1
#=> 'a' 가 제일 길기 때문

#str = "sttrg" return은 3
#=> 'trg' 가 제일 길기 때문

def get_len_of_str(string):
    max_len =0
    for i in range(len(string)):
        list = [string[i]]
    
        for k in range(i+1, len(string)):
            if string[k] in list:
                break
            list.append(string[k])
      
        if len(list) > max_len:
            max_len = len(list)
            
    return max_len