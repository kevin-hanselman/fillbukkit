#! /usr/bin/python3

import sys
import os
import filecmp
import shutil
from urllib.request import urlretrieve, urlopen, FancyURLopener

def download(url, filename):
    tmp = filename+'.tmp'
    furlo = FancyURLopener({})
    try:
        furlo.retrieve(url, tmp)
    except IOError as ex:
        sys.exit(ex)

    if os.path.exists(filename) and filecmp.cmp(filename,tmp):
        print('You already have the newest version')
        os.remove(tmp)
    else:
        shutil.copyfile(tmp,filename)
        print('Updated successfully')
    
if __name__ == "__main__":
    download("http://ess.ementalo.com/repository/download/bt2/.lastSuccessful/Essentials.zip?guest=1", "Ess.zip")