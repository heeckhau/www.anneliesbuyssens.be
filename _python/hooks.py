def process_info(info, site):
    if 'layout' in info:
        if info['layout']=='gallery2':
            process_gallery(info)
from os import getcwd
from os import listdir
from os.path import isfile, join, dirname

import create_gallery_image

def process_gallery(info):
    if 'folder' in info:
        mypath=getcwd()+"/images/_originals/"+info['folder']+"/"
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        #print(onlyfiles)
        info['fotos'] = onlyfiles
        if not 'thumbnail' in info:
            info['thumbnail'] = onlyfiles[0]
    if 'thumbnail' in info:
        input = "images/fotos/"+info['folder']+"/"+info['thumbnail']
        gallery_thumbnail_path = dirname(input) + "/thumbnails/gallery.png"
        if not isfile(gallery_thumbnail_path):
            create_gallery_image.create_gallery_image(input, gallery_thumbnail_path)

