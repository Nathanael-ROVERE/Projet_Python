import functools as func
from pymel.core import *
import maya.cmds as cmds
import sys
# Change the path to your directory
# PATH = "C:\\Users\\macou\\ATI\\python\\Projet_Python"
PATH = "C:\\Users\\macou\\Documents\\maya\\scripts\\Projet_Python"
MODEL_PATH = PATH + "\\models\\"
ICON_PATH = PATH + "\\icons\\"
sys.path.append(PATH + "\\src")

cmds.file(f=True, new=True)

# before = set(cmds.ls(type='transform'))
# cmds.file(MODEL_PATH + "\\COULEURS_OBJETS.mb", reference=True, namespace="objects")
# after = set(cmds.ls(type='transform'))
# imported = after - before
# cmds.hide(imported)

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
        self.template.define(iconTextRadioButton, mw=self.spacing, mh=self.spacing)
        self.template.define(frameLayout, collapsable=True,
                             backgroundColor=[0.2, 0.2, 0.2])
        self.template.define(intSliderGrp, cal=[1, "left"])
    def createWindow(self, title):
        with window(title=title) as self.win:
            with self.template:
                with rowColumnLayout(nc=1, co=(1, "both", 15), adj=1):
                    with frameLayout("Environment"):
                        self.environment = {}
                        with rowLayout(nc=4):
                            text(l='Time', al="left")
                            self.environment['time'] = iconTextRadioCollection(
                                'time')
                            iconTextRadioButton('day', sl=(False, True)[self.environment['time'] == "day"],
                                                l='Circular', i1=ICON_PATH + 't_sun.png', st='iconOnly')
                            iconTextRadioButton('night',
                                                sl=(False, True)[
                                                    self.generator.environment['time'] == "night"],
                                                l='Squarish', i1=ICON_PATH + 't_moon.png', st='iconOnly')
                        with rowLayout(nc=5):
                            text(l='Season', al='left')
                            self.environment['season'] = iconTextRadioCollection('season')
                            iconTextRadioButton('spring', sl=(False, True)
                                                [self.environment['season'] == "spring"],
                                                l='Spring', i1=ICON_PATH + 'e_spring.png', st='iconOnly')
                            iconTextRadioButton('summer', sl=(False, True)
                                                [self.environment['season']
                                                    == "summer"],
                                                l='Spring', i1=ICON_PATH + 'e_summer.png', st='iconOnly')
                            iconTextRadioButton('automn', sl=(False, True)
                                                [self.environment['season']
                                                    == "automn"],
                                                l='Spring', i1=ICON_PATH + 'e_automn.png', st='iconOnly')
                            iconTextRadioButton('winter', sl=(False, True)
                                                [self.environment['season']
                                                    == "winter"],
                                                l='Spring', i1=ICON_PATH + 'e_winter.png', st='iconOnly')

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
                        self.base['size'] = intSliderGrp(
                            f=True, l='Size', cw3=[40,50, 90])
                    separator(h=10, style='none')
                    button(label="Generate", c=Callback( self.generator.generate, self))


class Switch:
    def __init__(self, value):
        self.value = value

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        return False  # Allows a traceback to occur

    def __call__(self, *values):
        return self.value in values



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
        self.base['shape'] = iconTextRadioCollection(UI.base['shape'], q=True, sl=True)

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
    


window = UI('Generator')
