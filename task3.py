import shutil
import os  
import os.path
import xml.etree.ElementTree as ET
from glob import glob

# copy files
if os.path.exists("C:\\Users\\ahmed\\Desktop\\DataRepositories_Test\\Output Sample\\Updated"):
    pass
else:
    os.chdir('C:\\')
    source = "C:\\Users\\ahmed\\Desktop\\DataRepositories_Test\\Explainers"
    destination = "C:\\Users\\ahmed\\Desktop\\DataRepositories_Test\\Output Sample\\Updated"
    shutil.copytree(source, destination)


def selectAllFiles():
    os.chdir("./Output Sample/Updated")
    global files
    files = glob("*")
    return files


def parseRoot(name):
    global root
    global tree 
    tree = ET.parse(name)
    root = tree.getroot()
    return root


def parseElement(root):
    
    for elm in root.findall('.//td'):
        var = ET.SubElement(elm,'s')
        var.text = elm.text
        elm.text = ''
    
    for elm in root.findall('.//p'):
        var = ET.SubElement(elm,'s')
        var.text = elm.text
        elm.text = ''     




names = selectAllFiles()

for name in names:
    root = parseRoot(name)
    parseElement(root)
    tree.write(name)
