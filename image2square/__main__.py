#!/usr/bin/env python3

from .image_to_square import image_to_square

import sys

def main():
    argslen = len(sys.argv)

    if argslen != 4:
        print(f'missing required arguments: [input file] [output file] [width]')
        sys.exit(1)

    in_file_name = sys.argv[1]
    out_file_name = sys.argv[2]
    width = int(sys.argv[3])

    image_to_square(in_file_name, out_file_name, width)

if __name__ == '__main__':
    main()
