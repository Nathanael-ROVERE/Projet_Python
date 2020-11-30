import maya.cmds as cmds
from pymel.core import *
import generator as gen
import utils
reload(gen)
reload(utils)


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
                                                l='Circular', i1=utils.icon_path() + 't_sun.png', st='iconOnly')
                            iconTextRadioButton('night',
                                                sl=(False, True)[
                                                    self.generator.environment['time'] == "night"],
                                                l='Squarish', i1=utils.icon_path() + 't_moon.png', st='iconOnly')
                        with rowLayout(nc=5):
                            text(l='Season', al='left')
                            self.environment['season'] = iconTextRadioCollection('season')
                            iconTextRadioButton('spring', sl=(False, True)
                                                [self.environment['season'] == "spring"],
                                                l='Spring', i1=utils.icon_path() + 'e_spring.png', st='iconOnly')
                            iconTextRadioButton('summer', sl=(False, True)
                                                [self.environment['season']
                                                    == "summer"],
                                                l='Spring', i1=utils.icon_path() + 'e_summer.png', st='iconOnly')
                            iconTextRadioButton('automn', sl=(False, True)
                                                [self.environment['season']
                                                    == "automn"],
                                                l='Spring', i1=utils.icon_path() + 'e_automn.png', st='iconOnly')
                            iconTextRadioButton('winter', sl=(False, True)
                                                [self.environment['season']
                                                    == "winter"],
                                                l='Spring', i1=utils.icon_path() + 'e_winter.png', st='iconOnly')

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

