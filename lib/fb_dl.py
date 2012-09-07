#! /usr/bin/python3
'''Handles web downloads for fillbukkit'''

import sys
import os
import filecmp
import shutil
from urllib.request import urlretrieve, urlopen, FancyURLopener, urlcleanup, URLError

from lib import fb_config

class HTTPError(Exception):
    pass

class FBDownloadManager:
    def __init__(self, plugin, url, format):
        self.plugin = plugin
        self.url = url
        self.format = format
        
        fbcfg = fb_config.FBConfig()
        if plugin == 'craftbukkit':
            self.dest_dir = fbcfg.base_dir()
        else:
            self.dest_dir = fbcfg.plugin_dir()
            
        if format == 'jar':
            dl_dir = self.dest_dir
        else:
            dl_dir = fbcfg.cache_dir()
                    
        self.dlpath = os.path.join(dl_dir, plugin + '.' + format)
        
    def download(self):
        furlo = FBURLopener({})
        try:
            tmpfile, msg = furlo.retrieve(self.url, reporthook=self.rhook)
            print()
        except HTTPError as ex:
            urlcleanup()
            sys.exit(ex)
        except URLError as ex:
            urlcleanup()
            sys.exit(ex)
        if os.path.exists(self.dlpath) and filecmp.cmp(self.dlpath, tmpfile):
            print('You already have the newest version of ' + self.plugin)
            done = True
        else:
            shutil.copyfile(tmpfile, self.dlpath)
            print(self.plugin + ' downloaded.')
            done = False
        urlcleanup()
        if done or self.format == 'jar':
            return
        try:
            shutil.unpack_archive(self.dlpath, self.dest_dir, self.format)
        except ValueError as ex:
            sys.exit('Error: ' + str(ex))
    
    def rhook(self, blocks_read, block_size, total_size):
        amount_read = blocks_read * block_size
        if total_size > 0:
            sys.stdout.write("\rDownloading: %2d%% of %s" 
                            % (amount_read/total_size*100, sizeof_fmt(total_size)))
        else:
            # unknown size
            sys.stdout.write("\rDownloading: %s" % sizeof_fmt(amount_read))
        sys.stdout.flush()       
    
def sizeof_fmt(num):
    for x in [' bytes','KB','MB','GB']:
        if num < 1024.0:
            return "%4.2f%s" % (num, x)
        num /= 1024.0
    
class FBURLopener(FancyURLopener):
    def http_error_default(self, url, fp, errorcode, errmsg, headers):
        if errorcode >= 400:
            raise HTTPError(str(errorcode) + ': ' + errmsg)
        else:
            FancyURLopener.http_error_default(self, url, fp, errorcode, errmsg, headers)
