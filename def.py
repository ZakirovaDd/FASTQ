def read_fasta(txt):
    x = open(txt, "r")
    a = x.read(500)
    x.close()
    c = a.replace('>SRR23674700', '')
    q = ''.join(i for i in c if i.isalpha())
    z = q.replace('length', '\n')
    # q = ''.join(i for i in z if i.isalpha())
    return z

print(read_fasta('1.txt'))
