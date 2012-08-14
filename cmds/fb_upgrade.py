#!/usr/bin/python3

import argparse

def cmd(args):
    print('upgrade: %r' % args)
    
def add_parser(sub):
    parser_upgrade = sub.add_parser('upgrade',help='Upgrade installed plugins')
    parser_upgrade.set_defaults(func=cmd)