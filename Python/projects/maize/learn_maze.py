import sys
from random import shuffle

def make_field(width, height, cellsize):
    cellsize1 = cellsize+1
    field_width = width*cellsize1
    field_height = height*cellsize1
    field = [0]*(field_width * field_height)
    print field






if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise SystemExit('Wrong inputs')
    width, height, cellsize = map(int, sys.argv[1:])
    make_field(width, height, cellsize)
