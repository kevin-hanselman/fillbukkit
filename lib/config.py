#! /usr/bin/python3
'''Wrapper classes for parsing config files used in fillbukkit'''

import configparser
import sys
import os

class ConfigWrap:
    '''Base class wrapper'''
    def __init__(self, filename):
        self.parser = configparser.ConfigParser()
        try:
            self.parser.read(filename)
        except configparser.ParsingError as ex:
            sys.exit(ex)
        if not os.path.exists(filename):
            sys.exit('Error: Could not find file: ' + filename)

    def keys(self, key, sects=None):
        if not sects:
            sects = self.parser.sections()
        try:
            keys = [self.parser.get(s, key) for s in sects]
        except configparser.Error as ex:
            sys.exit(ex)
        return keys

class FBConfig(ConfigWrap):
    '''Wrapper for the fillbukkit config file'''
    def __init__(self):
        ConfigWrap.__init__(self, 'fillbukkit.cfg')
        
    def base_dir():
        try:
            dir = self.parser.get('Directories', 'craftbukkit')
        except configparser.Error as ex:
            sys.exit(ex)
        return dir
        
    def plugin_dir():
        try:
            dir = self.parser.get('Directories', 'plugins')
        except configparser.Error as ex:
            sys.exit(ex)
        return dir
        
    def disabled_dir():
        try:
            dir = self.parser.get('Directories', 'disabled')
        except configparser.Error as ex:
            sys.exit(ex)
        return dir
    
class FBDownloadList(ConfigWrap):
    '''Wrapper for the download list file'''
    def __init__(self):
        ConfigWrap.__init__(self, 'dl.cfg')
        
    def plugins(self):
        p = self.parser.sections()
        try:
            p.remove('craftbukkit')
        except configparser.NoSectionError as ex:
            sys.exit(ex)
        return p

    def keys(self, key):
        return ConfigWrap.keys(self, key, self.plugins())