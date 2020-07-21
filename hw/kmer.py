import sys
import itertools

base_l = 'ATGC'

def kmer(n):
    com = list(itertools.product(base_l,repeat=n))
    for i in com:
        for j in i:
            print(j,end='')
        print() 

def palin(n):
    res = []
    p_cnt = 0
    com = list(itertools.product(base_l,repeat=n))
    for i in com:
        res.append(','.join(list(i)).replace(',',''))
    for j in res:
        if j == j[::-1]:
            print(j)
            p_cnt += 1
    print(p_cnt)

if __name__=="__main__":
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} [number]")
    k = int(sys.argv[1])
    #kmer(k)
    print(palin(k))
