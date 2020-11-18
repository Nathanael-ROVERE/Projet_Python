from maya import cmds 

class UI:
  """Manage UI
  """
  def __init__(self, title):
    """[summary]

    Args:
        id (string): window title
    """
    self.title = title.replace(" ", "")
    self.resetUI()
    self.createTemplate()
    self.createWindow(title)
    cmds.showWindow()

  def resetUI(self):
    """delete window and template if they are already instantiated
    """
    if cmds.window('window1', ex=True):
        cmds.deleteUI('window1', window=True)
    if cmds.uiTemplate(self.title + 'Template', exists=True):
        cmds.deleteUI(self.title + 'Template', uiTemplate=True)

  def createWindow(self, title):
    cmds.window(title=title, resizeToFitChildren=True, nestedDockingEnabled=True)
    cmds.setUITemplate(self.title + 'Template', pushTemplate=True)

    # =========================================================
    # BASE
    # =========================================================
    cmds.frameLayout(label='Base')
    cmds.rowLayout(adj=True, nc=3)
    self.dioramaShapeRadio = cmds.iconTextRadioCollection('DioramaShape')
    cmds.iconTextRadioButton(st='iconAndTextVertical',
                             i1='polyCylinder.png', l='Circular')
    cmds.iconTextRadioButton(st='iconAndTextVertical', i1='polyCube.png', l='Squarish')
    cmds.iconTextRadioButton(st='iconAndTextVertical', i1='polyPlatonic.png', l='Polygonal')
    cmds.setParent('..')
    cmds.setParent('..')

  def createTemplate(self):
    """Define default parameters for all UI elements
    """
    cmds.uiTemplate(self.title + 'Template')
    cmds.frameLayout(dt=self.title + 'Template', cll=True, bgc=[0.2, 0.2, 0.2])

  
