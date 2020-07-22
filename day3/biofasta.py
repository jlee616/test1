from Bio import SeqIO

record = SeqIO.read("059.fasta","fasta")

A = record.seq.count("A")
C = record.seq.count("C")
G = record.seq.count("G")
T = record.seq.count("T")

print(f"A: {A}") # A: 497
print(f"C: {C}") # C: 444
print(f"G: {G}") # G: 585
print(f"T: {T}") # T: 514
