#reverse 함수에 정수인 숫자를 인자로 받습니다. 그 숫자를 뒤집어서 return해주세요.
#x: 1234 return: 4321
#x: -1234 return: -4321
#x: 1230 return: 321

def reverse(x):
    if x[0] == '-':
      list_mod =list(x)
      list_mod.pop(0) #끝자리에 0 있으면 제거 
      list_mod.append('-')
      list_mod.reverse()
      join_list = ''.join(list_mod[:]) #연결 
      return join_list
    else:
      reversed_x = x[len(x)::-1]
      return reversed_x