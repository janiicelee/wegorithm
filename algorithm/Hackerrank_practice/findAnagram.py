def find_ana(l):
    a=[]
    for i in range(len(l)):
        for j in range(len(l)): 
            if (l[i]!=l[j]) and (sorted(l[i])==sorted(l[j])):
                a.append(l[i])
                a.append(l[j])

    #print(list(set(a)))
    return list(set(a))

print(find_ana(['car', 'arc', 'asdf', 'fdsa','yes']))