import sys

s = sys.argv[1] #ATGTTATAG

for i in range(0,len(s)):
    if s[i:i+2] == "TT":
        print(i,s[i:i+2])
