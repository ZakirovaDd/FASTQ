def txt_file(f):
    x = open(f, "r")
    a = x.read(1000) # use as many lines as u want
    x.close()
    file = open('3.txt', 'w', encoding='utf-8')
    return file.write(a)


f = r'C:\Users\Сергей\Desktop\sra-tools\sratoolkit.3.0.2-win64\bin\SRR23674700_1.fasta'  # write ur path
txt_file(f)