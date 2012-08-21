#! /usr/bin/python3
'''Remove installed plugins'''

import argparse

def cmd(args):
    print('rm: %r' % args)
    
def add_parser(sub):
    parser = sub.add_parser('rm', help=__doc__, description=__doc__)
    parser.set_defaults(func=cmd)