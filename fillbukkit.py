#! /usr/bin/python3

import argparse
import fb_cmds

def main():
    parser = init_argparse()
    args = parser.parse_args()
    args.func(args)
    
def init_argparse():
    desc='A command-line plugin manager for Craftbukkit Minecraft server plugins.'

    op_parser = argparse.ArgumentParser(description=desc)
    op_parser.add_argument('-V','--version',help='Display the version of %(prog)s',action='version', version='%(prog)s 0.1')
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