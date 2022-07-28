#!/usr/bin/env python3
"""
Author : faisalalbasu <faisalalbasu@localhost>
Date   : 2022-07-28
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
import os.path


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

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    vowel = args.vowel
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for char in text:
        if text.isupper():
            vowel = vowel.upper()
        if char in vowels:
            text = text.replace(char, vowel)
    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
