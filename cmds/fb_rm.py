#!/usr/bin/python3

import argparse

def cmd(args):
    print('rm: %r' % args)
    
def add_parser(sub):
    parser = sub.add_parser('rm',help='Remove installed plugins')
    parser.set_defaults(func=cmd)