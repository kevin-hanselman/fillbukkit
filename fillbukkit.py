#! /usr/bin/python3

import argparse
import sys
import os

import fb_cmds
from fb_libs import *

def main():
    config = configwrapper.get_fb_config()
    print(config.sections())
    
    parser = init_argparse()
    args = parser.parse_args()
    print(args)
    args.func(args)
    
def init_argparse():
    desc='A command-line plugin manager for Craftbukkit Minecraft servers.'

    op_parser = argparse.ArgumentParser(description=desc)
    op_parser.add_argument('-V','--version',
                            help='Display the version of %(prog)s',
                            action='version', 
                            version='%(prog)s 0.1')
    subs = op_parser.add_subparsers()
    
    fb_cmds.add.add_parser(subs)
    fb_cmds.disable.add_parser(subs)
    fb_cmds.enable.add_parser(subs)
    fb_cmds.ls.add_parser(subs)
    fb_cmds.rm.add_parser(subs)
    fb_cmds.search.add_parser(subs)
    fb_cmds.upgrade.add_parser(subs)

    return op_parser
 
if __name__ == "__main__":
    main()