#! /usr/bin/python3
'''Wrapper classes for parsing config files used in fillbukkit'''

import configparser
import sys
import os
import errno

class NoPluginError(Exception):
    pass

class ConfigWrap(configparser.ConfigParser):
    '''Base class wrapper'''
    def __init__(self, cfgpath, must_exist=True):
        configparser.ConfigParser.__init__(self)
        cfgpath = os.path.expanduser(cfgpath)
        if must_exist and not os.path.exists(cfgpath):
            sys.exit('Error: Could not locate file: ' + cfgpath)
        try:
            self.read(cfgpath)
        except configparser.ParsingError as ex:
            sys.exit(ex)
        self.path = cfgpath
        self.filename = os.path.split(cfgpath)[-1]

    def keys(self, key, sects=None):
        if not sects:
            sects = self.sections()
        try:
            keys = [self.get(s, key) for s in sects]
        except configparser.Error as ex:
            self.fatal_report(ex)
        return keys

    def links(self, section):
        try:
            links = {ver:url for ver,url in self.items(section) if ver != 'description' and ver != 'format'}
        except configparser.Error as ex:
            self.fatal_report(ex)
        return links

    def report(self, err):
        return ': '.join(('Error', self.filename, str(err)))

    def fatal_report(self, err):
        sys.exit(self.report(err))

class FBConfig(ConfigWrap):
    '''Wrapper for the fillbukkit config file'''
    def __init__(self):
        ConfigWrap.__init__(self, 'fillbukkit.cfg')

    def get_dir(self, dir, create=True):
        try:
            dir = self.get('Directories', dir)
        except configparser.Error as ex:
            self.fatal_report(ex)
        dirpath = os.path.expanduser(dir)
        if create:
            try:
                os.makedirs(dirpath)
            except OSError as ex:
                if ex.errno != errno.EEXIST:
                    sys.exit(ex)
        return dirpath

    def base_dir(self):
        return self.get_dir('craftbukkit')

    def update_dir(self):
        return self.get_dir('update')
        
    def plugin_dir(self):
        return self.get_dir('plugins')

    def disabled_dir(self):
        return self.get_dir('disabled')
        
    def cache_dir(self):
        return self.get_dir('dlcache')

class FBDownloadList(ConfigWrap):
    '''Wrapper for the download list file'''
    def __init__(self):
        ConfigWrap.__init__(self, 'dl.cfg')
    
    def plugin(self, pname):
        try:
            plug = self[pname]
        except KeyError as ex:
            raise NoPluginError('Error: Could not find plugin: ' + pname)
        return plug
    
    def plugins(self):
        p = self.sections()
        try:
            p.remove('craftbukkit')
        except configparser.NoSectionError as ex:
            self.fatal_report(ex)
        return p

class FBPluginInfo(ConfigWrap):
    '''Wrapper for the lists of enabled/disabled plugins'''
    def __init__(self):
        fb_cfg = FBConfig()
        path = os.path.join(fb_cfg.base_dir(), 'plugin.info')
        ConfigWrap.__init__(self, path, False)
    
    def is_installed(self, plugin):
        return self.has_option('disabled', plugin) \
            or self.has_option('enabled', plugin)
    
    def add_disabled(self, plugin, release):
        try:
            self.remove_option('enabled', plugin)
        except configparser.NoSectionError:
            pass
        try:
            self.set('disabled', plugin, release)
        except configparser.NoSectionError:
            self['disabled'] = {}
            self.set('disabled', plugin, release)
        self.save()
        
    def add_enabled(self, plugin, release):
        try:
            self.remove_option('disabled', plugin)
        except configparser.NoSectionError:
            pass
        try:
            self.set('enabled', plugin, release)
        except configparser.NoSectionError:
            self['enabled'] = {}
            self.set('enabled', plugin, release)
        self.save()
        
    def rm_entry(self, plugin):
        try:
            self.remove_option('disabled', plugin)
        except configparser.NoSectionError:
            pass
        try:
            self.remove_option('enabled', plugin)
        except configparser.NoSectionError:
            pass
        self.save()
        
    def save(self):
        with open(self.path, 'w') as configfile:
            self.write(configfile)
