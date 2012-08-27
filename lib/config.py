#! /usr/bin/python3
'''Wrapper classes for parsing config files used in fillbukkit'''

import configparser
import sys
import os

class NoPluginError(Exception):
    pass

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
            self.fatal_report(ex)
        return keys

    def report(self, err):
        return str(self.filename + ': '+ str(err))

    def fatal_report(self, err):
        sys.exit(self.report(err))
        
class FBConfig(ConfigWrap):
    '''Wrapper for the fillbukkit config file'''
    def __init__(self):
        ConfigWrap.__init__(self, 'fillbukkit.cfg')
        
    def get_dir(self, dir):
        try:
            dir = self.get('Directories', dir)
        except configparser.Error as ex:
            self.fatal_report(ex)
        return os.path.expanduser(dir)
        
    def base_dir(self):
        return get_dir(self, 'craftbukkit')
        
    def plugin_dir(self):
        return get_dir(self, 'plugins')
        
    def disabled_dir(self):
        return get_dir(self, 'disabled')
    
class FBDownloadList(ConfigWrap):       
    '''Wrapper for the download list file'''
    def __init__(self):
        ConfigWrap.__init__(self, 'dl.cfg')
    
    def plugin(self, pname):
        try:
            plug = self[pname]
        except KeyError as ex:
            raise NoPluginError('Could not find plugin: ' + pname)
        return plug
    
    def plugins(self):
        p = self.sections()
        try:
            p.remove('craftbukkit')
        except configparser.NoSectionError as ex:
            self.fatal_report(ex)
        return p

    def keys(self, key):
        return ConfigWrap.keys(self, key, self.plugins())
        
class FBPlugins(ConfigWrap):
    '''Wrapper for the lists of enabled/disabled plugins'''
    def __init__(self):
        ConfigWrap.__init__(self, 'plugins.cfg')