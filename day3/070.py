# number of lines without ones starting with #
num = 0
with open("070.vcf",'r') as handle:
    for line in handle:
        if line.startswith('#'):
            continue
        num += 1
print(num)

# number of lines that have PASS in the FILTER column
cnt = 0
with open("070.vcf",'r') as handle:
    for line in handle:
        if line.startswith('##'):
            continue
        elif line.startswith('#'):
            header = line.strip().split('\t')
            ind = header.index("FILTER")
            continue
        split = line.strip().split('\t')
        if split[ind] == "PASS":
            cnt += 1
print(cnt)

# if the value for ID starts with rs, print some of the line's values
with open("070.vcf",'r') as handle:
    for line in handle:
        if line.startswith('##'):
            continue
        elif line.startswith('#'):
            header2 = line.strip().split('\t')
            ind2 = header2.index("ID")
            continue

        split2 = line.strip().split('\t')
        chrom = split2[0]
        pos = split2[1]
        id_ = split2[2]
        ref = split2[3]
        alt = split[4]
        if split2[ind2].startswith("rs"):
            print(f"{chrom}-{pos}-{ref}-{alt}-{id_}")

# count the total number of ALT
alt_cnt = 0
with open("070.vcf",'r') as handle:
    for line in handle:
        if line.startswith('##'):
            continue
        elif line.startswith('#'):
            header3 = line.strip().split('\t')
            alt_ind = header3.index("ALT")
            continue

        splitted = line.strip().split('\t')
        #alt_cnt += len(splitted[alt_ind].split(','))
        alts = splitted[4].split(',')
        for alt in alts:
            alt_cnt += 1
    print(alt_cnt)

# count number of SNP, insertion, deletions
# SNP = Ref and Alt same lenght
# insertion = Ref < Alt
# deletion = Ref > Alt

snp = 0
ins = 0
del_ = 0
with open("070.vcf",'r') as handle:
    for line in handle:
        if line.startswith('##'):
            continue
        elif line.startswith('#'):
            header4 = line.strip().split('\t')
            alt_ind = header4.index("ALT")
            ref_ind = header4.index("REF")
            continue

        splitted2 = line.strip().split('\t')
        alts2 = splitted2[alt_ind].split(',')
        refs2 = splitted2[ref_ind]
        for alt in alts2:
            if len(alt) == len(refs2):
                snp += 1
            elif len(alt) > len(refs2):
                ins += 1
            elif len(alt) < len(refs2):
                del_+= 1
            else: #방어적코딩
                raise
print(f"SNP: {snp}, Insertions: {ins}, Deletions: {del_}")
