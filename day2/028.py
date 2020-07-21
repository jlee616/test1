import sys

def comp1(seq: str) -> str:
    comp = ''
    for s in seq:
        if s == 'A':
            comp += 'T'
        elif s == 'T':
            comp += 'A'
        elif s == 'C':
            comp += 'G'
        elif s == 'G':
            comp += 'C'
    return comp

def comp2(seq: str) -> str:
    d_comp = {'A':'T','T':'A','C':'G','G':'C'}
    comp = ''
    for s in seq:
        comp += d_comp[s]
    return comp

seq = sys.argv[1] #ATGTTATAG
c1 = comp1(seq)
c2 = comp2(seq)
print(seq)
print(c1)
print(c2)
