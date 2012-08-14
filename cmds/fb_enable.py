#!/usr/bin/python3

import argparse

def cmd(args):
    print('enable: %r' % args)
    
def add_parser(sub):
    parser_enable = sub.add_parser('enable',help='Enable installed plugins')
    parser_enable.add_argument('-r','--release', help='Select the plugin release to enable (stable, beta, dev)')
    parser_enable.set_defaults(func=cmd)