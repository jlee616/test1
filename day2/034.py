l = [3,1,1,2,0,0,2,3,3]

max_val = l[0]
min_val = l[0]

for i in l:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i

print(f"max: {max_val}")
print(f"min: {min_val}")

#count using dictionary
d = {}
for i in l:
    if i in d:
        d[i]+= 1
    else:
        d[i] = 1

print(d)
