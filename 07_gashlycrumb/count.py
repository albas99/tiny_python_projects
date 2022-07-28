#!/usr/bin/env python3
"""
Author : faisalalbasu <faisalalbasu@localhost>
Date   : 2022-07-27
Purpose: Rock the Casbah
"""

import argparse
from pprint import pprint
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Program to count how many times each word appears in a document',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file = args.file
    lookup = {}
    num_words = []
    all_words = []
    print(type(num_words))

    for line in file:
        words_list = line.lower().split()
        for words in words_list:
            all_words.append(words)
    for word in all_words:
        word_count = all_words.count(word)
        num_words.append(word_count)
    count_pairs = dict(list(zip(all_words, num_words)))
    pprint(count_pairs)
    # print(all_words)
    # pprint(lookup)

# --------------------------------------------------
if __name__ == '__main__':
    main()
