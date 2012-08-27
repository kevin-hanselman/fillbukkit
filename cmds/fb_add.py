#! /usr/bin/python3
'''Add/install plugins or Craftbukkit'''

import argparse
import os
import configparser
import sys
from lib import *

def cmd(args):
    dl = config.FBDownloadList()
    try:
        plug = dl.plugin(args.plugin)
    except config.NoPluginError as ex:
        sys.exit(ex)
    except configparser.Error as ex:
        sys.exit('Error: ' + ex)
    print(dlfile)
    
def add_parser(sub):
    parser = sub.add_parser('add', help=__doc__, description=__doc__)
    parser.add_argument('-r','--release', 
                        choices=('stable','beta','dev'), 
                        default='stable', 
                        help='select the plugin release to add')
    parser.add_argument('plugin', help='the name of the plugin to add')
    parser.set_defaults(func=cmd)
    