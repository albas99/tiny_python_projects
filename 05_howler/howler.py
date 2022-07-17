#!/usr/bin/env python3
"""
Author : faisalalbasu <faisalalbasu@localhost>
Date   : 2022-07-16
Purpose: Rock the Casbah
"""

import argparse

# --------------------------------------------------
import os.path


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        metavar='str',
                        help='Text Input: either a string or from a file',
                        nargs='+')
    parser.add_argument('-o',
                        '--outfile',
                        help='The output saved in a file',
                        metavar='str',
                        type=str,
                        default='')
    parser.add_argument('-lc',
                        '--lowercase',
                        help='Set to lower case',
                        action='store_true')

    args = parser.parse_args()

    if os.path.isfile(args.input):
        args.input = open(args.input).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file_arg = args.outfile
    input_arg = args.input
    lower_case = args.lowercase
    if lower_case:
        result = input_arg.lower()
    else:
        result = input_arg.upper()

    if file_arg:
        with open(file_arg, 'wt', encoding='utf8') as o_f:
            o_f.write(result)
    else:
        print(result)


# --------------------------------------------------
if __name__ == '__main__':
    main()
