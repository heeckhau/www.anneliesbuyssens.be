def process_info(info, site):
    if 'layout' in info:
        if info['layout']=='gallery2':
            process_gallery(info)
from os import getcwd
from os import listdir
from os.path import isfile, join
import test

def process_gallery(info):
    if 'folder' in info:
        mypath=getcwd()+"/images/_originals/"+info['folder']+"/"
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        #print(onlyfiles)
        info['fotos'] = onlyfiles
        if not 'thumbnail' in info:
            info['thumbnail'] = onlyfiles[0]
    if 'thumbnail' in info:
        test.create_gallery_image("images/fotos/"+info['folder']+"/thumbnails/"+info['thumbnail'])

