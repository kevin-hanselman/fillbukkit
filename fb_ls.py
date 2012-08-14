#!/usr/bin/python3

import argparse

def cmd(args):
    print('ls: %r' % args)
    
def add_parser(sub):
    parser_ls = sub.add_parser('ls',help='List installed plugins')
    parser_ls.set_defaults(func=cmd)