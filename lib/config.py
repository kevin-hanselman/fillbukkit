#! /usr/bin/python3
'''Wrapper classes for parsing config files used in fillbukkit'''

import configparser
import sys
import os

class ConfigWrap(configparser.ConfigParser):
    '''Base class wrapper'''
    def __init__(self, cfgpath):
        configparser.ConfigParser.__init__(self)
        if not os.path.exists(cfgpath):
            sys.exit('Error: Could not locate file: ' + cfgpath)
        try:
            self.read(os.path.expanduser(cfgpath))
        except configparser.ParsingError as ex:
            sys.exit(ex)
        self.path, self.filename = os.path.split(cfgpath)

    def keys(self, key, sects=None):
        if not sects:
            sects = self.sections()
        try:
            keys = [self.get(s, key) for s in sects]
        except configparser.Error as ex:
            sys.exit(ex)
        return keys

class FBConfig(ConfigWrap):
    '''Wrapper for the fillbukkit config file'''
    def __init__(self):
        ConfigWrap.__init__(self, 'fillbukkit.cfg')
        
    def base_dir(self):
        try:
            dir = self.get('Directories', 'craftbukkit')
        except configparser.Error as ex:
            sys.exit(ex)
        return dir
        
    def plugin_dir(self):
        try:
            dir = self.get('Directories', 'plugins')
        except configparser.Error as ex:
            sys.exit(ex)
        return dir
        
    def disabled_dir(self):
        try:
            dir = self.get('Directories', 'disabled')
        except configparser.Error as ex:
            sys.exit(ex)
        return dir
    
class FBDownloadList(ConfigWrap):
    '''Wrapper for the download list file'''
    def __init__(self):
        ConfigWrap.__init__(self, 'dl.cfg')
        
    def plugins(self):
        p = self.sections()
        try:
            p.remove('craftbukkit')
        except configparser.NoSectionError as ex:
            sys.exit(ex)
        return p

    def keys(self, key):
        return ConfigWrap.keys(self, key, self.plugins())
        
class FBPlugins(ConfigWrap):
    '''Wrapper for the lists of enabled/disabled plugins'''
    def __init__(self):
        ConfigWrap.__init__(self, 'plugins.cfg')