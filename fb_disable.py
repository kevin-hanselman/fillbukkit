#!/usr/bin/python3

import argparse

def cmd(args):
    print('disable: %r' % args)
    
def add_parser(sub):
    parser_disable = sub.add_parser('disable', help='Disable installed plugins')
    parser_disable.add_argument('-a','--all', help='Disable all installed plugins', action='store_true')
    parser_disable.set_defaults(func=cmd)