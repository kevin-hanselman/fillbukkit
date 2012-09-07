#! /usr/bin/python3
'''Add/install plugins or Craftbukkit'''

import argparse
import os
import configparser
import sys
from lib import *

def cmd(args):
    plinfo = fb_config.FBPluginInfo()
    if plinfo.is_installed(args.plugin):
        sys.exit(args.plugin + ' is already installed')

    try:
        dlcfg = fb_config.FBDownloadList()
        plug = dlcfg.plugin(args.plugin)
        dlman = fb_dl.FBDownloadManager(plugin=plug.name, 
                            url=plug[args.release],
                            format=plug['format'])
    except fb_config.NoPluginError as ex:
        sys.exit(ex)
    except configparser.Error as ex:
        sys.exit('Error: ' + str(ex))
    except KeyError as ex:
        if str(ex) == '\'' + args.release + '\'':
            sys.exit('Error: ' + plug.name + ' does not have a ' 
                    + args.release + ' release')
        else:
            sys.exit('Error: ' + str(ex))
    dlman.download()
    plinfo.add_enabled(plug.name, args.release)
      
def add_parser(sub):
    parser = sub.add_parser('add', help=__doc__, description=__doc__)
    parser.add_argument('-r','--release', 
                        choices=('stable','beta','dev'), 
                        default='stable', 
                        help='select the plugin release to add')
    parser.add_argument('plugin', help='the name of the plugin to add')
    parser.set_defaults(func=cmd)
    