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

pm.window()
# Result: ui.Window('window1') #
pm.frameLayout(labelVisible=False)
# Result: ui.FrameLayout('window1|frameLayout15') #
panel = pm.outlinerPanel()
outliner = pm.outlinerPanel(panel, query=True, outlinerEditor=True)
pm.outlinerEditor(outliner, edit=True, 
mainListConnection='worldList', 
selectionConnection='modelList', 
showShapes=False, 
showReferenceNodes=False, 
showReferenceMembers=False, 
showAttributes=False, 
showConnected=False, 
showAnimCurvesOnly=False, 
autoExpand=False, 
showDagOnly=True,          
ignoreDagHierarchy=False, 
expandConnections=False, 
showNamespace=True, 
showCompounds=True, 
showNumericAttrsOnly=False, 
highlightActive=True, 
autoSelectNewObjects=False, 
doNotSelectNewObjects=False, 
transmitFilters=False, 
showSetMembers=True, 
setFilter='defaultSetFilter')
# Result: ui.OutlinerEditor('window1|frameLayout15|outlinerPanel2|outlinerPanel2|outlinerPanel2|outlinerPanel2') #
pm.showWindow()
