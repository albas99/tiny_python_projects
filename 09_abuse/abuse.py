#!/usr/bin/env python3
"""
Author : faisalalbasu <faisalalbasu@localhost>
Date   : 2022-08-15
Purpose: Rock the Casbah
"""

import argparse
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a',
                        '--adjectives',
                        help='Number of adjectives',
                        metavar='adj',
                        type=int,
                        default=2)

    parser.add_argument('-n',
                        '--number',
                        help='Number of insults',
                        metavar='int',
                        type=int,
                        default=3)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)
    parser.add_argument('-aa',
                        '--alt-adj',
                        help='Alternative adjectives from files',
                        metavar='alt-adj',
                        type=argparse.FileType('rt'),
                        default=None)
    parser.add_argument('-an',
                        '--alt-nouns',
                        help='Alternative nouns from files',
                        metavar='alt-noun',
                        type=argparse.FileType('rt'),
                        default=None)

    args =  parser.parse_args()

    if args.adjectives < 1:
        return parser.error(f'--adjectives "{args.adjectives}" must be > 0')
    if args.number < 1:
        return parser.error(f'--number "{args.number}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    adjective = args.adjectives
    insults = args.number
    alt_adj = args.alt_adj
    alt_nouns = args.alt_nouns


    adjectives = """bankrupt base caterwauling corrupt cullionly detestable dishonest false filthsome filthy
foolish foul gross heedless indistinguishable infected insatiate irksome lascivious lecherous loathsome lubbery old peevish rascaly rotten ruinous scurilous scurvy slanderous
sodden-witted thin-faced toad-spotted unmannered vile wall-eyed""".strip().split()

    nouns = """Judas Satan ape ass barbermonger beggar block boy braggart butt carbuncle coward
coxcomb cur dandy degenerate fiend fishmonger fool gull harpy jack jolthead knave liar
lunatic maw milksop minion ratcatcher recreant rogue scold slave swine traitor varlet
villain worm""".strip().split()

    if alt_adj:
        adjectives = alt_adj.read().strip().split()
        for insult in range(insults):
            selected_adjectives = ', '.join(random.sample(adjectives, adjective))
            noun = random.choice(nouns)
            insult = f"You {selected_adjectives} {noun}!"
            print(insult)
    if alt_nouns:
        nouns = alt_nouns.read().strip().split()
        for insult in range(insults):
            selected_adjectives = ', '.join(random.sample(adjectives, adjective))
            noun = random.choice(nouns)
            insult = f"You {selected_adjectives} {noun}!"
            print(insult)
    else:
        for insult in range(insults):
            selected_adjectives = ', '.join(random.sample(adjectives, adjective))
            noun = random.choice(nouns)
            insult = f"You {selected_adjectives} {noun}!"
            print(insult)



# --------------------------------------------------
if __name__ == '__main__':
    main()
