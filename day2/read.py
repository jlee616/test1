import sys

def read_txt(filename: str) -> str:
    ret = ""
    with open(filename,'r') as handle:
        for line in handle:
            if line.startswith('>'):
                continue
            ret += line.strip()
    return ret

def read_csv(filename: str) -> list:
    ret = []
    with open(filename,'r') as handle:
        for line in handle:
            if line.startswith('#'):
                header = line.strip().lstrip('#').split(",")
                continue
            splitted = line.strip().split(",")
            d = dict(zip(header,splitted))
            ret.append(d)
    return ret

def read_tsv(filename: str) -> list:
    ret = []
    with open(filename,'r') as handle:
        for line in handle:
            if line.startswith('#'):
                header = line.strip().lstrip('#').split("\t")
                continue
            splitted = line.strip().split("\t")
            d = dict(zip(header,splitted))
            ret.append(d)
    return ret

if __name__=="__main__":
    if len(sys.argv) != 4:
        print(f"#usage: python {sys.argv[0]} [txt] [csv] [tsv]")
        sys.exit()

    txt_name = sys.argv[1]
    txt = read_txt(txt_name)
    print(txt)
    csv_name = sys.argv[2]
    csv = read_csv(csv_name)
    print(csv)
    tsv_name = sys.argv[3]
    tsv = read_tsv(tsv_name)
    print(tsv)
