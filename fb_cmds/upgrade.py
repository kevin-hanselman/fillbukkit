#!/usr/bin/python3

import argparse

def cmd(args):
    print('upgrade: %r' % args)
    
def add_parser(sub):
    parser = sub.add_parser('upgrade',help='Upgrade installed plugins')
    parser.add_argument('-c','--craftbukkit', help='Upgrade the Craftbukkit JAR', action='store_true')
    parser.set_defaults(func=cmd)