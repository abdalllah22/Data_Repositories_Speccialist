import xml.etree.ElementTree as ET
import pandas as pd
from glob import glob
import os

cols = ["id","title", "seo_meta_description", "source_id", "developer_name"]
rows = []

# getting all files
def selectAllFiles():
    os.chdir("Explainers")
    global files
    files = glob("*")
    return files

# parse name of each file
def parseRoot(name):
    global root 
    tree = ET.parse(name)
    root = tree.getroot()
    return root


def check_Null(tag):
    if tag  is not None:
            tag = tag.text
    else:
            tag = None
    return tag

def parseElement(root):
    
    for elm in root.findall("."):
        id = elm.attrib["id"]
        
        developer_name = root.find("developer_name")
        developer_name = check_Null(developer_name)
        
        title = root.find("title")
        title = check_Null(title)
        
        seo_meta_description = root.find("seo_meta_description")
        seo_meta_description = check_Null(seo_meta_description)
        
        source_id = root.find("source_id")
        source_id = check_Null(source_id)

        rows.append({
            "id" : id,
            "title": title,
            "seo_meta_description": seo_meta_description,
            "source_id": source_id,
            "developer_name": developer_name
        })
        df = pd.DataFrame(rows, columns=cols)
        
        path='C:\\Users\\ahmed\\Desktop\\DataRepositories_Test\\Output Sample\\Explainers\\'
        df.to_csv(path+'Explainers data.csv')



names = selectAllFiles()

for name in names:
    root = parseRoot(name)
    parseElement(root)