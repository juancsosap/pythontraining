import os, shutil, json

class FileUtils:
    @staticmethod
    def mvfiles(srcfolder, dstfolder, ffilters=None, movefolder=False):
        flist = os.listdir(srcfolder)
        dstfolder = dstfolder[:-1] if dstfolder[-1] in ['/', '\\'] else dstfolder
        
        foldername = srcfolder[srcfolder.rfind('/')+1:] if '/' in srcfolder else srcfolder[srcfolder.rfind('\\')+1:]
        if movefolder:
            dstfolder = f'{dstfolder}/{foldername}'
            
        FileUtils.mkfolder(dstfolder)
        for file in flist:
            try:
                if ffilters is None:
                    shutil.move(f'{srcfolder}/{file}', f'{dstfolder}/')
                else:
                    for ffilter in ffilters:
                        if ffilter in file:
                            shutil.move(f'{srcfolder}/{file}', f'{dstfolder}/')
            except: pass
        
        if movefolder:
            try: os.rmdir(srcfolder)
            except: pass
    
    @staticmethod
    def mkfolder(folder):
        if not os.path.exists(folder):
            os.mkdir(folder)
    
    # Open the file and return the content as string
    @staticmethod
    def readfile(path):
        with open(path) as file:
            text = file.read()
        return text
    
    # read a JSON file and return the content as dictionary
    @staticmethod
    def readjson(path):
        text = FileUtils.readfile(path)
        return json.loads(text)
    
    # list the files present within a directory and return
    # the a list of paths
    # optional a path filter could be indicated
    @staticmethod
    def listfiles(dirpath, pathfilters=[]):
        # list the files within the directory
        filenames = os.listdir(dirpath) if os.path.exists(dirpath) else []

        # append the dirpath to the filenames and sort them
        filepaths = [os.path.join(dirpath, filename) for filename in filenames]
        filepaths.sort()

        # filter the path list
        result = []
        for filepath in filepaths:
            valid = True
            for pathfilter in pathfilters:
                if type(pathfilter) is str: 
                    if pathfilter not in filepath:
                        valid = False
                        break
                else:
                    orvalid = False
                    for pathfilteritem in pathfilter:
                        if pathfilteritem in filepath:
                            orvalid = True
                            break
                    if not orvalid:
                        valid = False
                        break
            if valid: 
                result.append(filepath)

        return result
