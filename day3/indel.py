from pandas import DataFrame
from matplotlib import pyplot as plt

d = {'snp':0, 'ins':0, 'del':0}

with open("070.vcf",'r') as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        elif line.startswith('#'):
            header = line.strip().split('\t')
            alt_ind = header.index("ALT")
            ref_ind = header.index("REF")
            continue

        splitted = line.strip().split('\t')
        alts = splitted[alt_ind].split(',')
        ref = splitted[ref_ind]
        for alt in alts:
            if len(alt) == len(ref):
                d['snp'] += 1
            elif len(alt) > len(ref):
                d['ins'] += 1
            elif len(alt) < len(ref):
                d['del'] += 1
            else: #defensive coding
                raise #error message
print(d)

df = DataFrame([d])
print(df)
df.plot.bar()
plt.savefig("snp.png")
