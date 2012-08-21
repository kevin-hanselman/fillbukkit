#! /usr/bin/python3
'''Search for supported plugins'''

import argparse
import re
from lib import config

def cmd(args):
    # print('search: %r' % args)   
    dl = config.FBDownloadList()
    data = list(zip(dl.plugins(), list(dl.parser[p].get('description') for p in dl.plugins())))

    if args.d:
        plugs = [(k,v) for k,v in data if re.search(args.pattern, ' '.join([k, v]))]
    else:
        plugs = [(k,v) for k,v in data if re.search(args.pattern, k)]
    
    for p, d in plugs:
        print('%s\n\t%s\n' % (p, d))

def add_parser(sub):
    p = sub.add_parser('search', help=__doc__, description=__doc__)
    p.add_argument('pattern', help='a pattern to search plugin names for', nargs='?', default='.')
    p.add_argument('-d', help='search plugin description, as well as plugin name', action='store_true')
    p.set_defaults(func=cmd)
