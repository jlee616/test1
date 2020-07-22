import sys

def mer(l1,l2,k):
    ltmp = []
    if k == 1:
        return l2
    else:
        for i in l1:
            for j in l2:
                ltmp.append(i+j)
        return mer(l1,ltmp,k-1)

n = int(input("Input a number k for k-mer: "))
print(mer(['A','C','G','T'],['A','C','G','T'],n))
