#! /usr/bin/python3
'''Handling web downloads for fillbukkit'''

import sys
import os
import filecmp
import shutil
import zipfile
from urllib.request import urlretrieve, urlopen, FancyURLopener, urlcleanup

class HTTPError(Exception):
    pass

def download(url, filename):
    furlo = FBURLopener({})
    try:
        tmpfile, msg = furlo.retrieve(url)
    except HTTPError as ex:
        urlcleanup()
        sys.exit(ex)

    if os.path.exists(filename) and filecmp.cmp(filename,tmpfile):
        print('[placeholder] You already have the newest version')
    else:
        shutil.copyfile(tmpfile,filename)
        print('[placeholder] Updated successfully')
    urlcleanup()

class FBURLopener(FancyURLopener):
    def http_error_default(self, url, fp, errorcode, errmsg, headers):
        if errorcode >= 400:
            raise HTTPError(str(errorcode) + ': ' + errmsg)
        else:
            FancyURLopener.http_error_default(self, url, fp, errorcode, errmsg, headers)

if __name__ == "__main__":
    download("http://ess.ementalo.com/repository/download/bt2/.lastSuccessful/Essentials.zip?guest=1", "Ess.zip")