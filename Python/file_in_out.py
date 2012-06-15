## file in and out tu

filename = 'test.txt'
done = 0
namelist = []
for x in range(1, 101):
    namelist.append(x)

FILE = open(filename, 'w')
for y in namelist:
    if y % 10 == 0:
        FILE.write('\n')
    n = repr(y)
    FILE.write(n)


FILE.close()

