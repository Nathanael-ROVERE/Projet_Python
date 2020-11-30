from pymel.core import *
import maya.cmds as cmds
from utils import Switch

class Generator:
    def __init__(self):
        self.environment = {}
        self.environment['time'] = 'day'
        self.base = {}
        self.base['shape'] = "circular"

    def generate(self, UI):
        self.updateValues(UI)
        self.buildBase()

    def updateValues(self, UI):
        self.base['shape'] = iconTextRadioCollection(
            UI.base['shape'], q=True, sl=True)

    def buildBase(self):
        with Switch(self.base['shape']) as case:
            if case('circular'):
                cmds.polyCylinder()
            elif case('squarish'):
                cmds.polyCylinder()
            elif case('polygonal'):
                cmds.polyCylinder()
            else:
                print('default')
