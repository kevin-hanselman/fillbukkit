#!/usr/bin/python3

import argparse

def cmd(args):
    print('add: %r' % args)
    
def add_parser(sub):
    parser = sub.add_parser('add', help='Add/install a plugin')
    parser.add_argument('-r','--release', 
                        choices=('stable','beta','dev'), 
                        default='stable', 
                        help='Select the plugin release to add')
    parser.set_defaults(func=cmd)