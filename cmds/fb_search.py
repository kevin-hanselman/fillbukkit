#! /usr/bin/python3
'''Search for supported plugins'''

import argparse
import re
from lib import config

def cmd(args):  
    dl = config.FBDownloadList()
    data = list(zip(dl.plugins(), dl.keys('description')))

    if args.d:
        plugs = [(p,d) for p,d in data if re.search(args.pattern, ' '.join([p, d]), re.IGNORECASE)]
    else:
        plugs = [(p,d) for p,d in data if re.search(args.pattern, p, re.IGNORECASE)]
    
    for p, d in plugs:
        print('%s\n\t%s\n' % (p, d))

def add_parser(sub):
    p = sub.add_parser('search', help=__doc__, description=__doc__)
    p.add_argument('pattern', help='search pattern for plugin names', nargs='?', default='.')
    p.add_argument('-d', help='search plugin description, as well as plugin name', action='store_true')
    p.set_defaults(func=cmd)