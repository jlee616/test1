import sys

class FASTQ:
    def __init__(self,file_name):
        self.file_name = file_name
        self.count = 0

    def count_lead(self):
        with open(self.file_name,'r') as handle:
            for line in handle:
                if line.startswith("@"):
                    self.count += 1
        #return self.count

if __name__=="__main__":
    if len(sys.argv) != 2:
        print(f"#usage: python {sys.argv[0]} [fastq]")
    fn = sys.argv[1]
    q = FASTQ(fn)
    q.count_lead()
    print(q.count)
