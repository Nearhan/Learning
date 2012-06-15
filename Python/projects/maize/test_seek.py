## A script to teach file seek()

filename = 'text_seek.txt'

#open file

f = open(filename, 'w+')

print f.tell()
f.write('A')
f.tell()
f.seek(1000, 1)
f.write ('Two Spaces')
for line in f:
    print line
f.close()
