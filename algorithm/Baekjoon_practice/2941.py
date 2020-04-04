a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alpha = input()

for t in a:
    alpha = alpha.replace(t, '1')

print(len(alpha))