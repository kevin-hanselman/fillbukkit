#! /usr/bin/python3

import configparser
import sys
import os

class ConfigWrap:
    def __init__(self, filename):
        self.parser = configparser.ConfigParser()
        try:
            self.parser.read(filename)
        except configparser.ParsingError as ex:
            sys.exit(ex)
        if not os.path.exists(filename):
            sys.exit('Error: Could not find file: ' + cfg)

class FBConfig(ConfigWrap):
    def __init__(self):
        ConfigWrap.__init__(self, 'fillbukkit.cfg')
    
class FBDownloadList(ConfigWrap):
    def __init__(self):
        ConfigWrap.__init__(self, 'dl.cfg')
        
    def plugins(self):
        p = self.parser.sections()
        p.remove('craftbukkit')
        return p