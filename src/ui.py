import maya.cmds as cmds
from pymel.core import *
# import generator as gen


class UI:
    """Manage UI
    """

    def __init__(self, title):
        self.generator = gen.Generator()

        self.templateName = title.replace(" ", "") + 'Template'

        self.spacing = 10
        self.resetUI()
        self.createTemplate()
        self.createWindow(title)

    def resetUI(self):
        """delete window and template if they are already instantiated
        """
        if cmds.window('window1', ex=True):
            cmds.deleteUI('window1', window=True)
        if cmds.uiTemplate(self.templateName, exists=True):
            cmds.deleteUI(self.templateName, uiTemplate=True)

    def createTemplate(self):
        """Define default parameters for all UI elements
        """
        self.template = uiTemplate(self.templateName, force=True)
        # cmds.uiTemplate()

        # cmds.columnLayout(defineTemplate=self.templateName,
        #                   adjustableColumn=True,
        #                   columnAttach=['both', self.spacing],
        #                   rowSpacing=self.spacing)
        # cmds.rowLayout(defineTemplate=self.templateName)
        # cmds.frameLayout(defineTemplate=self.templateName,
        #                  collapsable=True,
        #                  backgroundColor=[0.2, 0.2, 0.2])

    def createWindow(self, title):

        # cmds.window(title=title)
        cmds.setUITemplate(self.templateName, pushTemplate=True)
        with window(menuBar=True, menuBarVisible=True) as self.win:
            # start the template block
            with self.template:
                with columnLayout(adj=1):
                    with formLayout() as form:
                        self.shapes = iconTextRadioCollection('shapes')
                        rb1 = iconTextRadioButton(l='Circular', i1='polyCylinder.png', st='iconAndTextVertical')
                        rb2 = iconTextRadioButton(l='Squarish', i1='polyCube.png', st='iconAndTextVertical')
                        rb3 = iconTextRadioButton(l='Polygonal', i1='polyPlatonic.png', st='iconAndTextVertical')
                        formLayout(form, edit=True, attachPosition=[
                            (rb1, 'left', 0, 0),
                            (rb2, 'left', 0, 33),
                            (rb3, 'left', 0, 66)
                        ])
        # cmds.columnLayout(adj=1)
        # # =========================================================
        # # BASE
        # # =========================================================
        # cmds.rowLayout(nc=3)
        # self.dioramaShapeRadio = cmds.iconTextRadioCollection('DioramaShape')
        # cmds.iconTextRadioButton(st='iconAndTextVertical',
        #                          i1='polyCylinder.png', l='Circular')
        # cmds.iconTextRadioButton(st='iconAndTextVertical',
        #                          i1='polyCube.png', l='Squarish')
        # cmds.iconTextRadioButton(st='iconAndTextVertical',
        #                          i1='polyPlatonic.png', l='Polygonal')
        # cmds.setParent('..')
