import maya.cmds as cmds
import random 
import glob
cmds.file(f=True, new=True)

def setImport():
    importPath = "C:/Users/nrovere/Documents/SEMESTRE1/Python/Projet_Python/utils/"
    name = "Arbres_Tropicale_01"
    fileType = ".fbx"
    
    files = cmds.getFileList(folder=importPath, filespec='*.%s' % fileType)
    print(files)
    
    if len(files) == 0:
        cmds.warning("No files found")
        
    else:
        for f in files:
            cmds.file(importPath + f, i=True)
        
    #cmds.file(importPath + name + fileType, i=True, mergeNamespacesOnClash=True, namespace=':');
    

setImport()

