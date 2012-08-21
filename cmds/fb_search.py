#! /usr/bin/python3
'''Search for supported plugins'''

import argparse
import re
from lib import config

def cmd(args):  
    dl = config.FBDownloadList()   
    plugs = [p for p in dl.plugins() if re.search(args.pattern, p)]
    descs = map(lambda p: dl.parser[p].get('description'), plugs)
    for p, d in zip(plugs, descs):
        print('%s\n\t%s\n' % (p, d))

def add_parser(sub):
    p = sub.add_parser('search', help=__doc__, description=__doc__)
    p.add_argument('pattern', help='search pattern for plugin names', nargs='?', default='.')
    p.set_defaults(func=cmd)