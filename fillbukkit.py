#! /usr/bin/python3

import argparse
import sys
import os

from cmds import *
from lib import *

def main():
    config = configwrapper.get_dl_list()
    print(config.sections())
    
    parser = init_argparse()
    args = parser.parse_args()
    args.func(args)
    
def init_argparse():
    desc='A command-line plugin manager for Craftbukkit Minecraft servers.'

    op_parser = argparse.ArgumentParser(description=desc)
    op_parser.add_argument('-V','--version',
                            help='Display the version of %(prog)s',
                            action='version', 
                            version='%(prog)s 0.1')
    subs = op_parser.add_subparsers()
    
    fb_add.add_parser(subs)
    fb_disable.add_parser(subs)
    fb_enable.add_parser(subs)
    fb_ls.add_parser(subs)
    fb_rm.add_parser(subs)
    fb_search.add_parser(subs)
    fb_upgrade.add_parser(subs)

    return op_parser
 
if __name__ == "__main__":
    main()