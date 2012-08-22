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
            sys.exit('Error: Could not find file: ' + cfg)

    def keys(self, key, sects=None):
        if not sects:
            sects = self.parser.sections()
        return [self.parser[s].get(key) for s in sects]

class FBConfig(ConfigWrap):
    '''Wrapper for the fillbukkit config file'''
    def __init__(self):
        ConfigWrap.__init__(self, 'fillbukkit.cfg')
        
    def base_dir():
        return self.parser.get('Directories', 'craftbukkit')
        
    def plugin_dir():
        return self.parser.get('Directories', 'plugins')
        
    def disabled_dir():
        return self.parser.get('Directories', 'disabled')
    
class FBDownloadList(ConfigWrap):
    '''Wrapper for the download list file'''
    def __init__(self):
        ConfigWrap.__init__(self, 'dl.cfg')
        
    def plugins(self):
        p = self.parser.sections()
        p.remove('craftbukkit')
        return p

    def keys(self, key):
        return ConfigWrap.keys(self, key, self.plugins())