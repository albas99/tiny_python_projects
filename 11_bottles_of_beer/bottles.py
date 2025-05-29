#!/usr/bin/env python3
"""
Author : faisalalbasu <faisalalbasu@localhost>
Date   : 2023-08-28
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--number',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default=10)
    
    args = parser.parse_args()
    
    if args.number <= 0:
        parser.error(f'--num {args.number} must be greater than 0')

    return args
    
    
def verse(bottle):
    """Sing a verse"""
    pass
    
def test_verse():
    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,' '1 bottle of beer,'
        'Take one down, pass it around,'
        'No bottles of beer on the wall!'
    ])
    
    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,' '2 bottles of beer,'
        'Take one down, pass it around,'
        '1 bottle of beer on the wall!'
    ])


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.positional

    print(f'str_arg = "{str_arg}"')
    print(f'int_arg = "{int_arg}"')
    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    print(f'flag_arg = "{flag_arg}"')
    print(f'positional = "{pos_arg}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
