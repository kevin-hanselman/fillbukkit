#! /usr/bin/python3
'''List installed plugins'''

import argparse

def cmd(args):
    print('ls: %r' % args)
    
def add_parser(sub):
    parser = sub.add_parser('ls', help=__doc__, description=__doc__)
    parser.set_defaults(func=cmd)