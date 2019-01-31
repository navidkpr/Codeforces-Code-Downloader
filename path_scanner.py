import os

def scan(path, filt = []):
    fileNames = []
    dirName = path
    for (dirName, dirs, files) in os.walk(dirName):

        filtfiles = []
        for filename in files:
            if len(filt) == 0:
                fileNames += [str(os.path.join(dirName, filename))]
    return fileNames

