voca_list = []
for i in range(int(input())):               
    voca_list.append(input())              
 
set_voca_list = list(set(voca_list))       

sort_voca_list = []
 
for j in set_voca_list:
    sort_voca_list.append((len(j), j))      
 
sort_voca_list.sort()                       
 
for len_voca, voca in sort_voca_list:       
    print(voca)