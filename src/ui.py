import maya.cmds as cmds

def createWindow():
  print("create")
  if cmds.window('window1', ex=True):
      cmds.deleteUI('window1', window=True)

  w = cmds.window(title=id,
                sizeable=False, resizeToFitChildren=True)
  # cmds.text(label="Diorama Generator", al="center", h=30)
  cmds.showWindow()

  return w

def createTemplate():
  if cmds.uiTemplate('templeTemplate', exists=True):
            cmds.deleteUI('templeTemplate', uiTemplate=True)

  cmds.uiTemplate("templeTemplate")
  cmds.frameLayout(dt="templeTemplate", cll=True, bgc=[0.2, 0.2, 0.2])
  cmds.setUITemplate('templeTemplate', pushTemplate=True)

  
