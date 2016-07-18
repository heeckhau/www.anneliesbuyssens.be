def process_info(info, site):
    if 'layout' in info:
        if info['layout']=='gallery2':
            process_gallery(info)

from os import getcwd
from os import listdir
from os.path import isfile, join
def process_gallery(info):
    if 'folder' in info:
       mypath=getcwd()+"/images/fotos/"+info['folder']+"/"
       onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
       #print(onlyfiles)
       info['fotos'] = onlyfiles
