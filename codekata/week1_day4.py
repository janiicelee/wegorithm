#숫자인 num을 인자로 넘겨주면, 뒤집은 모양이 num과 똑같은지 여부를 반환해주세요.

# num = 123
# return false 
# => 뒤집은 모양이 321 이기 때문

# num = 1221
# return true 
# => 뒤집은 모양이 1221 이기 때문

# num = -121
# return false 
# => 뒤집은 모양이 121- 이기 때문

def same_reverse(num):
  
  if num < 0:
    return False
  
  reverse_num = str(num)[::-1]

  if num == int(reverse_num): 
    return True
      
  return False