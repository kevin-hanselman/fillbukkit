#!/usr/bin/python3

import argparse

def cmd(args):
    print('rm: %r' % args)
    
def add_parser(sub):
    parser_rm = sub.add_parser('rm',help='Remove installed plugins')
    parser_rm.set_defaults(func=cmd)