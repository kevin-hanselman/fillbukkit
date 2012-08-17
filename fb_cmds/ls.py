#!/usr/bin/python3

import argparse

def cmd(args):
    print('ls: %r' % args)
    
def add_parser(sub):
    parser = sub.add_parser('ls',help='List installed plugins')
    parser.set_defaults(func=cmd)