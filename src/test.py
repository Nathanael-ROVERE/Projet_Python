from maya import cmds
import maya.cmds as cmds
import random 
import glob
import pymel.core as pm

cmds.file(f=True, new=True)

# def setImport():
#     importPath = "C:/Users/nrovere/Documents/SEMESTRE1/Python/Projet_Python/utils/"
#     name = "Arbres_Tropicale_01"
#     fileType = ".fbx"
    
#     files = cmds.getFileList(folder=importPath, filespec='*.%s' % fileType)
#     print(files)
    
#     if len(files) == 0:
#         cmds.warning("No files found")
        
#     else:
#         for f in files:
#             cmds.file(importPath + f, i=True)
        
#     #cmds.file(importPath + name + fileType, i=True, mergeNamespacesOnClash=True, namespace=':');
    


#  def translateXSliderButton(HUD):
#     cmds.undoInfo(swf=True)
#     selList = cmds.ls(sl=True)
#     for object in selList:
#         if cmds.objectType(object, isType='transform'):
#             cmds.setAttr(
#                 object+".tx", cmds.hudSliderButton(HUD, query=True, v=True))

#         # Create our slider button.  Use lambda to create an "anonymous" function that invokes the
#         # callback with the desired button name argument.
#         #
# cmds.hudSliderButton('HUDTranslateXSliderButton', s=5, b=5, vis=True, sl='Slider:', value=0, type='int', min=-10, max=10, slw=50,
#                     vw=50, sln=100, si=1, bl='Button', bw=60, bsh='rectangle', brc=lambda: translateXSliderButton('HUDTranslateXSliderButton'))



# cmds.window(width=200)
# cmds.formLayout('theForm')
# cmds.nodeTreeLister('theTreeLister')
# cmds.formLayout('theForm', e=True,
#                 af=(('theTreeLister', 'top', 0),
#                     ('theTreeLister', 'left', 0),
#                     ('theTreeLister', 'bottom', 0),
#                     ('theTreeLister', 'right', 0)))
# cmds.showWindow()

def selectTreeCallBack(*args):
  print 'selection :- str= ' + args[0] + ' onoff= ' + str(args[1])
  return True


def pressTreeCallBack(*args):
  print 'press :- str= ' + args[0] + ' onoff= ' + str(args[1])


# window = cmds.window()
# layout = cmds.formLayout()

# control = cmds.treeView(parent=layout, numberOfButtons=3, abr=False)

# cmds.formLayout(layout, e=True, attachForm=(control, 'top', 2))
# cmds.formLayout(layout, e=True, attachForm=(control, 'left', 2))
# cmds.formLayout(layout, e=True, attachForm=(control, 'bottom', 2))
# cmds.formLayout(layout, e=True, attachForm=(control, 'right', 2))

# cmds.showWindow(window)

# cmds.treeView(control, e=True, addItem=("layer 1", ""))
# cmds.treeView(control, e=True, addItem=("layer 2", ""))
# cmds.treeView(control, e=True, addItem=("layer 3", ""))
# cmds.treeView(control, e=True, addItem=("layer 4", ""))
# cmds.treeView(control, e=True, addItem=("layer 5", ""))
# cmds.treeView(control, e=True, addItem=("layer 6", ""))
# cmds.treeView(control, e=True, addItem=("layer 7", "layer 2"))
# cmds.treeView(control, e=True, addItem=("layer 8", "layer 2"))
# cmds.treeView(control, e=True, addItem=("layer 9", "layer 2"))
# cmds.treeView(control, e=True, addItem=("layer 10", "layer 8"))
# cmds.treeView(control, e=True, addItem=("layer 11", "layer 2"))
# cmds.treeView(control, e=True, addItem=("layer 12", ""))
# cmds.treeView(control, e=True, addItem=("layer 13", "layer 10"))
# cmds.treeView(control, edit=True, pressCommand=[
#               (1, pressTreeCallBack), (2, pressTreeCallBack), (3, pressTreeCallBack)])
# cmds.treeView(control, edit=True, selectCommand=selectTreeCallBack)


# cmds.treeView(control, edit=:True, removeAll = True)

w = cmds.window(width=200)
fl = cmds.formLayout()
tl = cmds.treeLister()
cmds.formLayout(fl, e=True,
                af=((tl, 'top', 0),
                    (tl, 'left', 0),
                    (tl, 'bottom', 0),
                    (tl, 'right', 0)))
cmds.showWindow(w)
items = ['root/branchone/leafone',
         'root/branchone/leaftwo',
         'root/branchtwo/leafthree']
cmds.treeLister(
    tl, e=True, add=[(i, 'sphere.png', cmds.sphere) for i in items])
