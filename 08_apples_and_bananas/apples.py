#!/usr/bin/env python3
"""
Author : faisalalbasu <faisalalbasu@localhost>
Date   : 2022-07-28
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and Bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Text input')

    parser.add_argument('-v',
                        '--vowel',
                        help='Vowel to be replaced with',
                        metavar='str',
                        type=str,
                        default='a',
                        choices=['a', 'e', 'i', 'o', 'u'])

    parser.add_argument('-f',
                        '--file',
                        help='A readable file input',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    vowel = args.vowel
    file = args.file
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']



    if file:
        for line in file:
            for char in line:
                if char in vowels:
                    print(line.replace(char, vowel))

    for char in text:
        if text.isupper():
            vowel = vowel.upper()
        if char in vowels:
            text = text.replace(char, vowel)
    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
