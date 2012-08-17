#!/usr/bin/python3

import argparse

def cmd(args):
    print('disable: %r' % args)
    
def add_parser(sub):
    parser = sub.add_parser('disable', help='Disable installed plugins')
    parser.add_argument('-a','--all', help='Disable all installed plugins', action='store_true')
    parser.set_defaults(func=cmd)