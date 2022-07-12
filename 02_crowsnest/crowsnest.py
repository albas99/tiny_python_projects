#!/usr/bin/env python3
"""
Author : faisalalbasu <faisalalbasu@localhost>
Date   : 2022-07-12
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word argument')
    parser.add_argument('--side',
                        '-s',
                        metavar='side',
                        choices=['larbaord', 'starboard'],
                        default='larboard',
                        help='Determine which side the thing is coming from')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    first_letter = word[0].lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    articles = ['a', 'an']
    side = args.side
    if first_letter in vowels:
        say = f"Ahoy, Captain, {articles[1]} {word} off the {side} bow!"
        print(say)
        return say
    say = f"Ahoy, Captain, {articles[0]} {word} off the {side} bow!"
    print(say)

    return say


# --------------------------------------------------
if __name__ == '__main__':
    main()
