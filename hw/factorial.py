import sys

cnt = int(sys.argv[1])
res = 1

while cnt>0:
    res*=cnt
    cnt-=1
print(res)
