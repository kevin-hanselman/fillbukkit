#! /usr/bin/python3
'''Add/install plugins'''

import argparse
import os
from lib import *

class NoPluginError(Exception):
    pass

def cmd(args):
    print('add: %r' % args)
    dl = config.FBConfig()
    s = os.path.expanduser(dl.plugin_dir())
    
def add_parser(sub):
    parser = sub.add_parser('add', help=__doc__, description=__doc__)
    parser.add_argument('-r','--release', 
                        choices=('stable','beta','dev'), 
                        default='stable', 
                        help='select the plugin release to add')
    parser.add_argument('plugin', help='the name of the plugin to add')
    parser.set_defaults(func=cmd)