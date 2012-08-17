#!/usr/bin/python3

import argparse

def cmd(args):
    print('search: %r' % args)
    
def add_parser(sub):
    parser = sub.add_parser('search',help='Search for a supported plugin')
    parser.set_defaults(func=cmd)