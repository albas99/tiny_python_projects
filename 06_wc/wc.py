#!/usr/bin/env python3
"""
Author : faisalalbasu <faisalalbasu@localhost>
Date   : 2022-07-17
Purpose: Rock the Casbah
"""
import argparse


# --------------------------------------------------
import sys


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc(word counter)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file(s)',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin])
    # not working!!! # todo: add individual flags
    # parser.add_argument('-l',
    #                     '--line',
    #                     help='Output number of lines only',
    #                     action='store_true')
    # parser.add_argument('-b',
    #                     '--bytes',
    #                     help='Output number of bytes only',
    #                     action='store_true')
    # parser.add_argument('-w',
    #                     '--words',
    #                     help='Output number of words only',
    #                     action='store_true')
    # return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    input_files = args.file
    line_flag = args.line
    bytes_flag = args.bytes
    words_flag = args.words
    result = ''
    # total_result = ''

    total_lines = 0
    total_words = 0
    total_bytes = 0
    for file in input_files:
        lines = 0
        words = 0
        num_bytes = 0
        lines_result = f'{lines:8}'
        words_result = f'{words:8}'
        bytes_result = f'{num_bytes:8}'
        file_name = file.name
        for line in file:
            lines += 1
            num_bytes += len(line)
            words += len(line.split())
        # todo: not working correctly
        if line_flag:
            result = result + lines_result
        if bytes_flag:
            result = result + bytes_result
        if words_flag:
            result = result + words_result
        else:
            result = f'{lines:8}{words:8}{num_bytes:8} {file.name}'
        print(result + ' ' + file_name)
        # above block not working correctly
        total_lines += lines
        total_words += words
        total_bytes += num_bytes

    if len(input_files) > 1:
        print(f'{total_lines:8}{total_words:8}{total_bytes:8} total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
