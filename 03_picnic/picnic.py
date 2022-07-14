#!/usr/bin/env python3
"""Going on a picnic"""
import argparse


def get_args():
    """Get CLI arguments/parameters"""
    parser = argparse.ArgumentParser(
        description="Store arguments",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        'items',
        metavar='str',
        help='Picnic items',
        nargs='+'
    )
    parser.add_argument(
        '-s',
        '--sorted',
        help='Sort items',
        action='store_true'
    )
    parser.add_argument(
        '-nc',
        '--no_comma',
        help='No comma between items',
        action='store_true'
    )
    parser.add_argument(
        '-sc',
        '--semicolon',
        help='Use semicolon instead of comma',
        action='store_true'
    )

    return parser.parse_args()


def main():
    """Main function -> takes arguments from CLI and prints out the sentence of what to bring"""
    args = get_args()

    items = args.items
    if args.sorted:
        items.sort()
    no_comma = args.no_comma
    semicolon = args.semicolon

    if len(items) == 1:
        result = f"You are bringing {items[0]}."
        print(result)
    if len(items) == 2:
        result = f"You are bringing {items[0]} and {items[1]}."
        print(result)
    if len(items) > 2:
        if no_comma:
            stuff = ' '.join(items[:-1])
            result = f"You are bringing {stuff} and {items[-1]}."
            print(result)
        elif semicolon:
            stuff = '; '.join(items[:-1])
            result = f"You are bringing {stuff}; and {items[-1]}."
            print(result)
        else:
            stuff = ', '.join(items[:-1])
            result = f"You are bringing {stuff}, and {items[-1]}."
            print(result)


if __name__ == "__main__":
    main()
