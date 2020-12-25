import os
import re
import glob
from mutagen.easyid3 import EasyID3

def downloadLink(URL):
    PathIDM = "C:\\Program Files (x86)\\Internet Download Manager\\IDMan.exe"
    os.system('"{}" /d {} /n'.format(PathIDM, URL))

def renameFile():
    dirPath = "C:\\Users\\Le Van Cuong\\Downloads\\Music\\"
    files = glob.glob(dirPath + "*.mp3")
    
    #rename file:
    newFiles = list()
    for fi in files:
        m = re.search("(\d+)", str(os.path.basename(fi)))
        print(m.group(0))
        if m:
            newfile = fi.replace(m.string, "Pham_Nhan_Tu_Tien_" + m.group(0) + ".mp3")
            os.rename(fi, newfile)
            newFiles.append(newfile)
    
    for fi in newFiles:
        audio = EasyID3(fi)
        audio['title'] = str(os.path.basename(fi))
        audio.save()