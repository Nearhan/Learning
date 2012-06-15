##Maze project

filename = 'maze1.txt'
f = open(filename, 'w')
dot = '.'


## make a square first
def make_solid_square(n):

    filename = 'maze1.txt'
    dot = '.'
    f = open(filename, 'w')
    for x in range(1,n**2+1):
        if x % n == 0:
            f.write(dot)
            f.write('\n')   
        else:
            f.write(dot)
    make_smaller_solid_square(f, n)

def make_smaller_solid_square(filestream, square):
    smaller = square - 10
    f.seek(0)
    for x in range(1, smaller**2+1):
        if x % smaller == 0:
           f.write('!!')
           f.write('\n')
        else:
            f.write('!!')
    f.close()

make_solid_square(50)
