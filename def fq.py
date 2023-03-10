import fastq as fq


def read_fq(txt):
    x = open(txt, 'r')
    a = fq.x.read(1000)
    x.close()
    # a = list(x)
    return a


print(read_fq('1.txt'))
