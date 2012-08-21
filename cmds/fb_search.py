#! /usr/bin/python3
'''Search for supported plugins'''

import argparse
from lib import config

def cmd(args):
    print('search: %r' % args)   
    
def add_parser(sub):
    parser = sub.add_parser('search', help=__doc__, description=__doc__)
    parser.set_defaults(func=cmd)