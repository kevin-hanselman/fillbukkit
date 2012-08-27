#! /usr/bin/python3
'''Handles web downloads for fillbukkit'''

import sys
import os
import filecmp
import shutil
from urllib.request import urlretrieve, urlopen, FancyURLopener, urlcleanup

from lib import fb_config

class HTTPError(Exception):
    pass

class FBDownloadManager:
    def __init__(self, plugin, url, format, jars):
        self.plugin = plugin
        self.url = url
        self.format = format
        self.jars = jars

    def download(self):
        furlo = FBURLopener({})
        try:
            tmpfile, msg = furlo.retrieve(self.url, reporthook=rhook)
            print()
        except HTTPError as ex:
            urlcleanup()
            sys.exit(ex)
        filename = self.filename()
        if os.path.exists(filename) and filecmp.cmp(filename, tmpfile):
            print('You already have the newest version of ' + self.plugin)
        else:
            shutil.copyfile(tmpfile, filename)
            print(self.plugin + ' updated successfully.')
        urlcleanup()
    
    def filename(self):
        return self.plugin + '.' + self.format
    
def rhook(blocks_read, block_size, total_size):
    amount_read = blocks_read * block_size
    if total_size > 0:
        sys.stdout.write("\rDownloading: %2d%% of %s" 
                        % (amount_read/total_size*100, sizeof_fmt(total_size)))
        sys.stdout.flush()
    else:
        # unknown size
        sys.stdout.write("\rDownloading: %s" % sizeof_fmt(amount_read))
        sys.stdout.flush()
    
def sizeof_fmt(num):
    for x in ['bytes','KB','MB','GB']:
        if num < 1024.0:
            return "%4.2f%s" % (num, x)
        num /= 1024.0
    
class FBURLopener(FancyURLopener):
    def http_error_default(self, url, fp, errorcode, errmsg, headers):
        if errorcode >= 400:
            raise HTTPError(str(errorcode) + ': ' + errmsg)
        else:
            FancyURLopener.http_error_default(self, url, fp, errorcode, errmsg, headers)
