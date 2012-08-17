#!/usr/bin/python3

import argparse

def cmd(args):
    print('enable: %r' % args)
    
def add_parser(sub):
    parser = sub.add_parser('enable',help='Enable installed plugins')
    parser.add_argument('-r','--release', help='Select the plugin release to enable (stable, beta, dev)')
    parser.set_defaults(func=cmd)