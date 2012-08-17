#! /usr/bin/python3

import configparser
import sys

def get_fb_config():
    cfg='fillbukkit.cfg'
    config = configparser.ConfigParser()
    try:
        config.read(cfg)
    except configparser.ParsingError as ex:
        sys.exit(ex)
    if not config.sections():
        sys.exit('Error: Could not find file: ' + cfg)
    return config
    
def get_dl_list():
    cfg='dl.cfg'
    config = configparser.ConfigParser()
    try:
        config.read(cfg)
    except configparser.ParsingError as ex:
        sys.exit(ex)
    if not config.sections():
        sys.exit('Error: Could not find file: ' + cfg)
    return config