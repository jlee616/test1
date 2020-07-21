import sys

d={}

with open('059.fasta','r') as handle:
    for line in handle:
        line = line.strip()
        if line.startswith(">"):
            continue
        for b in line:
            if b in d:
                d[b] += 1
            else:
                d[b] = 1

print(d)
