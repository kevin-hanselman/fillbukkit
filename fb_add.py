#!/usr/bin/python3

import argparse

def cmd(args):
    print('add: %r' % args)
    
def add_parser(sub):
    parser_add = sub.add_parser('add', help='Add/install a plugin')
    parser_add.add_argument('-r','--release', help='Select the plugin release to add (stable, beta, dev)')
    parser_add.set_defaults(func=cmd)