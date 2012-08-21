#! /usr/bin/python3
'''Enable installed plugins'''

import argparse

def cmd(args):
    print('enable: %r' % args)
    
def add_parser(sub):
    parser = sub.add_parser('enable', help=__doc__, description=__doc__)
    parser.set_defaults(func=cmd)