#!/usr/bin/env python3
"""
Author : faisalalbasu <faisalalbasu@localhost>
Date   : 2022-07-25
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letters',
                        metavar='str',
                        nargs='+',
                        help='Letter to look up')
    parser.add_argument('-f',
                        '--file',
                        help='A readable input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    letters = args.letters
    file = args.file
    sentences = {}
    for line in file:
        sentences[line[0]] = line
    for letter in letters:
        letter = letter.upper()
        if letter in sentences:
            print(sentences[letter], end='')
        else:
            print(f"I do not know \"{letter}\".")
    # for letter in letters:
    #     if letter in sentences:
    #         print(sentences[letter])



# --------------------------------------------------
if __name__ == '__main__':
    main()
