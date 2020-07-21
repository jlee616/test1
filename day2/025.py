seq1 = 'ATGTTATAG'

#print every 3
for i in range(0,len(seq1),3):
    print(i, seq1[i])#indexing

#or you could do
print(seq1[0::3])

#print first 3, next 3, so on

for i in range(0,len(seq1),3):
    print(seq1[i:i+3]) #slicing
