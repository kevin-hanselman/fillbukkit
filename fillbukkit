#! /usr/bin/python3
'''A command-line plugin manager for Craftbukkit Minecraft servers.'''

import argparse
import os

from cmds import *

def main():
    # change working directory to where the script/config files are located
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    parser = init_argparse()
    args = parser.parse_args()
    args.func(args)
    
def init_argparse():
    op_parser = argparse.ArgumentParser(description=__doc__)
    op_parser.add_argument('-V','--version',
                            help='display the version of %(prog)s',
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