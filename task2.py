import xml.etree.ElementTree as ET
import pandas as pd
from glob import glob
import os

cols = ["question id","media identifier", "question title", "question start-time", "question end-time"]
rows = []

def selectAllFiles():
    os.chdir("Video Transcripts")
    global files
    files = glob("*")
    return files

def parseRoot(name):
    global root 
    tree = ET.parse(name)
    root = tree.getroot()
    return root

def parseId():
    for elm in root.findall("."):
        video_id = elm.attrib["video_id"]
    return video_id    

def parseElement(root):
    for elm in root.findall("./transcript/question"):
        
        #   handle question_id   #
        if 'id' not in elm.attrib:
            elm.attrib["id"] = ''
        if 'id' in elm.attrib :
            question_id = elm.attrib["id"]
        if elm.attrib["id"] is '':
            question_id = ''
        
        #  handle media_identifier   #
        if 'media_identifier' not in elm.attrib:
            elm.attrib["media_identifier"] = ''
        if 'media_identifier' in elm.attrib :
            media_identifier = elm.attrib["media_identifier"]
        if elm.attrib["media_identifier"] is '':
            media_identifier = ''
    

        question_title = elm.find("question_title")
        if question_title is not None:
            question_title = elm.find("question_title").text
        else:
            question_title = None
        
        start_time = elm.find("./p/s").attrib["start_time"]
        end_time = elm.findall("./p/s")[-1].attrib["end_time"]
        
        
        rows.append({
            "question id" : question_id,
            "media identifier": media_identifier,
            "question title": question_title,
            "question start-time": start_time,
            "question end-time": end_time
        })
        

names = selectAllFiles()

for name in names:
    root = parseRoot(name)
    parseElement(root)
    df = pd.DataFrame(rows, columns=cols)
    path='C:\\Users\\ahmed\\Desktop\\DataRepositories_Test\\Output Sample\\Video Transcripts\\'
    df.to_csv(path+parseId()+'.csv')
    rows.clear()