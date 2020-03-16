#twoSum함수에 숫자 리스트와 '특정 수'를 인자로 넘기면,더해서 '특정 수'가 나오는 index를 배열에 담아 return해 주세요.

#nums은 [4, 9, 11, 14]
#target은 13 
#nums[0] + nums[1] = 4 + 9 = 13 이죠?
#그러면 [0, 1]이 return 되어야 합니다.
#target으로 보내는 합계의 조합은 배열 전체 중에 2개 밖에 없다고 가정하겠습니다.

def two_sum(nums, target):
  
  result = []
  
  for i in nums[:len(nums)-1]:
    for j in nums[nums.index(i)+1:len(nums)]:
      if i+j == target:
        a = nums.index(i)
        b = nums.index(j)
        
        result.append(a)
        result.append(b)
        
  return result    
