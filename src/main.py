import functools as func
from pymel.core import *
import maya.cmds as cmds
import sys
# Change the path to your directory
# PATH = "C:\Users\macou\ATI\python\Projet_Python\src"
PATH = "C:\Users\nrovere\Documents\SEMESTRE1\Python>\Projet_Python\src"
sys.path.append(PATH)


class Callback(object):
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args):
        return self.func(*self.args, **self.kwargs)


class UI:
    """Manage UI
    """

    def __init__(self, title):
        self.generator = Generator()

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
        self.template.define(frameLayout, collapsable=True,
                             backgroundColor=[0.2, 0.2, 0.2])
        self.template.define(iconTextRadioButton, mw=self.spacing)

    def createWindow(self, title):
        with window() as self.win:
            with self.template:
                with columnLayout(adj=1):
                    with frameLayout("Base"):
                        self.base = {}
                        with rowLayout(nc=3):
                            self.base['shape'] = iconTextRadioCollection(
                                'shapes')
                            iconTextRadioButton('circular',
                                                sl=(False, True)[
                                                    self.generator.base['shape'] == "circular"],
                                                l='Circular', i1='polyCylinder.png', st='iconAndTextVertical')
                            iconTextRadioButton('squarish',
                                                sl=(False, True)[
                                                    self.generator.base['shape'] == "squarish"],
                                                l='Squarish', i1='polyCube.png', st='iconAndTextVertical')
                            iconTextRadioButton('polygonal',
                                                sl=(False, True)[
                                                    self.generator.base['shape'] == "polygonal"],
                                                l='Polygonal', i1='polyPlatonic.png', st='iconAndTextVertical')
                    button(label="Generate", c=Callback( self.generator.generate, self))


class Generator:
    def __init__(self):
        self.base = {}
        self.base['shape'] = "circular"

    def generate(self, UI):
        self.updateValues(UI)
        self.buildBase()

    def updateValues(self, UI):
        self.base['shape'] = iconTextRadioCollection(UI.base['shape'], q=True, sl=True)

    def buildBase(self):
        if(self.base['shape'] == "circular"):
            base = cmds.polyCylinder()
        elif(self.base['shape'] == "squarish"):
            base = cmds.polyCube()
        elif(self.base['shape'] == "polygonal"):
            base = cmds.polyCylinder()


window = UI('Generator')
