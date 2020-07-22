import sys

def count_len(filename):
    tot = 0
    with open(filename,'r') as handle:
        for line in handle:
            split = line.strip().split('\t')
            start = int(split[1])
            end = int(split[2])
            tot += (end - start)
    return tot

def chromo_len(filename):
    chr_d = {}
    with open(filename,'r') as handle:
        for line in handle:
            split = line.strip().split('\t')
            chrom = split[0]
            start = int(split[1])
            end = int(split[2])
            if chrom in chr_d:
                chr_d[chrom] += (end - start) 
            else:
                chr_d[chrom] = (end - start)
    return chr_d

if __name__=="__main__":
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} [BED]")
    file_name = sys.argv[1]
    print(chromo_len(file_name))
