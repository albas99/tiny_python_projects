#!/usr/bin/env python3
"""
Author : faisalalbasu <faisalalbasu@localhost>
Date   : 2022-08-16
Purpose: Rock the Casbah
"""

import argparse
import random
import os
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Randomly mutating strings',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input string')

    parser.add_argument('-m',
                        '--mutations',
                        help='Mutations to add',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if args.mutations <= 0 or args.mutations >= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    mutations = args.mutations
    random.seed(args.seed)

    
    # print(f'I heard : "{text}"')

    heard = text
    num_mutations = round(len(text) * mutations)
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))

    indexes = random.sample(range(len(text)), num_mutations)
    # for i in indexes:
    #     print(f'{i:2} {text[i]} changes to {random.choice(alpha) if i != alpha[i] else "same"}')
    for i in indexes:
        replacement = random.choice(alpha.replace(heard[i], ''))
        heard = heard[:i] + replacement + heard[i+1:]
    print(f'You said: "{text}"')
    print(f'I heard : "{heard}"')
        

# --------------------------------------------------
if __name__ == '__main__':
    main()
