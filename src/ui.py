import maya.cmds as cmds
from pymel.core import *
import generator as gen
import utils
import functools as func
from os import path
reload(gen)
reload(utils)


class UI:
    """Manage UI
    """

    def __init__(self, title):

        self.generator = gen.Generator()

        self.templateName = title.replace(" ", "") + 'Template'

        self.spacing = 10
        self.widthLabel = 50

        self.selectedItems = []

        self.resetUI()
        self.createTemplate()
        self.createWindow(title)

    def resetUI(self):
        """delete window and template if they are already instantiated
        """
        if cmds.window('window1', rtf=True, ex=True):
            cmds.deleteUI('window1', window=True)
        if cmds.uiTemplate(self.templateName, exists=True):
            cmds.deleteUI(self.templateName, uiTemplate=True)

    def createTemplate(self):
        """Define default parameters for all UI elements
        """
        self.template = uiTemplate(self.templateName, force=True)

        #Layouts
        self.template.define(frameLayout, collapsable=False,
                             backgroundColor=[0.2, 0.2, 0.2])
        self.template.define(rowColumnLayout, nc=1, co=(
            1, "both", self.spacing), adj=1)

        #elements
        self.template.define(iconTextRadioButton,
                             mw=self.spacing, mh=self.spacing)
        self.template.define(intSliderGrp, cal=[1, "left"])
        self.template.define(iconTextRadioButton, hlc=[0.2, 0.2, 0.2], mw=5, mh=5)

        #style
        self.template.define(separator, h=self.spacing, style="none")

    @staticmethod
    def toggle(controls):
        for control in controls.values():
            isFloatGroup = cmds.floatSliderGrp(control, q=True, ex=True)
            isIntGroup = cmds.intSliderGrp(control, q=True, ex=True)
            isOptionMenuGroup = cmds.optionMenuGrp(control, q=True, ex=True)
            if (isFloatGroup):
                value = cmds.floatSliderGrp(control, q=True, en=True)
                cmds.floatSliderGrp(control, e=True, en=not value)
            elif (isIntGroup):
                value = cmds.intSliderGrp(control, q=True, en=True)
                cmds.intSliderGrp(control, e=True, en=not value)
            elif(isOptionMenuGroup):
                value = cmds.optionMenuGrp(control, q=True, en=True)
                cmds.optionMenuGrp(control, e=True, en=not value)

    def frameEnvironment(self):
        self.environment = {}
        with frameLayout("Environment"):
            with rowColumnLayout():
                with rowLayout(nc=4, cw=[1, self.widthLabel]):
                    text(l='Time', al="left")
                    self.environment['time'] = iconTextRadioCollection(
                        'time')
                    iconTextRadioButton('day', sl=(False, True)[
                                            self.generator.environment['time'] == "day"],
                                        l='Circular', i1=utils.icon_path() + 't_sun.png', st='iconOnly')
                    iconTextRadioButton('night',
                                        sl=(False, True)[
                                            self.generator.environment['time'] == "night"],
                                        l='Squarish', i1=utils.icon_path() + 't_moon.png', st='iconOnly')
                with rowLayout(nc=5, cw=[1, self.widthLabel]):
                    text(l='Season', al='left')
                    self.environment['season'] = iconTextRadioCollection(
                        'season')
                    iconTextRadioButton('spring', sl=(False, True)
                                        [self.generator.environment['season']
                                            == "spring"],
                                        l='Spring', i1=utils.icon_path() + 'e_spring.png', st='iconOnly')
                    iconTextRadioButton('summer', sl=(False, True)
                                        [self.generator.environment['season']
                                            == "summer"],
                                        l='Spring', i1=utils.icon_path() + 'e_summer.png', st='iconOnly')
                    iconTextRadioButton('automn', sl=(False, True)
                                        [self.generator.environment['season']
                                            == "automn"],
                                        l='Spring', i1=utils.icon_path() + 'e_automn.png', st='iconOnly')
                    iconTextRadioButton('winter', sl=(False, True)
                                        [self.generator.environment['season']
                                            == "winter"],
                                        l='Spring', i1=utils.icon_path() + 'e_winter.png', st='iconOnly')

    def frameBase(self):
        self.base = {}
        with frameLayout("Base"):
            with rowColumnLayout():
                separator()
                with rowLayout(nc=4, cw=[1, self.widthLabel]):
                    text(l='Shape', al='left')
                    self.base['shape'] = iconTextRadioCollection(
                        'shapes')
                    iconTextRadioButton('circular',
                                        sl=(False, True)[
                                            self.generator.base['shape'] == "circular"],
                                        l='Smooth', i1='polyCylinder.png', st='iconAndTextVertical')
                    iconTextRadioButton('squarish',
                                        sl=(False, True)[
                                            self.generator.base['shape'] == "squarish"],
                                        l='Cubic', i1='polyCube.png', st='iconAndTextVertical')
                    iconTextRadioButton('polygonal',
                                        sl=(False, True)[
                                            self.generator.base['shape'] == "polygonal"],
                                        l='Triangle', i1='polyPlatonic.png', st='iconAndTextVertical')
                separator()
                self.base['size'] = intSliderGrp(
                    v=self.generator.base['size'],
                    minValue=5,
                    maxValue=50,
                    f=True, l='Size', cw3=[self.widthLabel, 50, 90])
                self.base['height'] = intSliderGrp(
                    v=self.generator.base['height'],
                    minValue=1,
                    maxValue=10,
                    f=True, l='Height', cw3=[self.widthLabel, 50, 90])
                separator()

    def frameCamera(self):
        self.camera = {}
        with frameLayout("Camera"):
            with rowColumnLayout():
                with columnLayout(cat=['both', 0], rs=self.spacing, adj=1):
                    # self.camera['enabled'] = cmds.checkBoxGrp(numberOfCheckBoxes=1, 
                    #                                             label='Enable',
                    #                                             label1='Camera',
                    #                                             v1=self.generator.camera['enabled'],
                    #                                           cal=[1, 'left'],
                    #                                           cw3=[
                    #                                               self.widthLabel, 10, 90],
                    #                                             onc=Callback(
                    #                                                 self.toggle, self.camera),
                    #                                             ofc=Callback(
                    #                                                 self.toggle, self.camera))
                    self.camera['focal'] = cmds.optionMenuGrp(
                        label='Focal', extraLabel='mm', cal=[1, 'left'],
                        cw3=[self.widthLabel, 50, 90])

                    cmds.menuItem(label='28')
                    cmds.menuItem(label='50')
                    cmds.menuItem(label='120')
                    cmds.menuItem(label='200')

    def addToSelectedItems(self, item, namespace):
        if treeView(self.treeView, q=True, iex=namespace) == 0:
            treeView(self.treeView, e=True, addItem=(namespace, ""))

        _item = (item, namespace)
        treeView(self.treeView, e=True, addItem=_item)
        treeView(self.treeView, e=True, bti=[item, 1, "-"])
        treeView(self.treeView, e=True,
                 displayLabel=[item, item.replace(namespace + ':', '')])

    def removeFromSelectedItems(self, *args):
        treeView(self.treeView, e=True, ri=args[0])

    def createItemsList(self):
        iconPath = utils.icon_path() + "\\types\\"
        filesList = getFileList(fld=utils.model_path(), fs="*.mb")

        for file in filesList:
            namespace = file.replace(".mb", "")
            icon = iconPath + namespace + ".png"
            before = set(cmds.ls(type='transform'))
            cmds.file(utils.model_path() + file,
                      reference=True, namespace=namespace)
            after = set(cmds.ls(type='transform'))
            imported = after - before
            for obj in sorted(imported):
                cmds.hide(obj)
                item = obj.replace(namespace + ":", "").replace("_", "/", 1)
                treeLister(self.treeLister, e=True, add=(
                    namespace + "/" + item, icon, func.partial(self.addToSelectedItems, obj, namespace)))

    def createWindow(self, title):
        with window(title=title, w=800, nde=True) as self.win:
            with self.template:
                with paneLayout(cn="vertical3"):
                    with rowColumnLayout():
                        separator()
                        self.frameEnvironment()
                        self.frameBase()
                        self.frameCamera()
                        separator()
                        button(label="Generate", c=Callback(
                            self.generator.generate, self))
                        separator()
                        button(label='Regenerate', c=Callback(
                            self.generator.regenerate, self
                        ))
                        separator()
                    with rowColumnLayout():
                        separator()
                        with frameLayout("Available Objects"):
                            self.treeLister = treeLister(w=200, h=360)
                            self.createItemsList()
                            separator()
                    with rowColumnLayout():
                        separator()
                        with frameLayout("Selected Objects"):
                            separator()
                            self.treeView = treeView(
                                nb=1,
                                ahp=True,
                                ams=False,
                                adr=False,
                                arp=False,
                                abr=True,
                                w=200,
                                h=330,
                                pressCommand=[(1, func.partial(self.removeFromSelectedItems))])

                            filesList = getFileList(
                                fld=utils.model_path(), fs="*.mb")
                            for file in filesList:
                                namespace = file.replace(".mb", "")
                                treeView(self.treeView, e=True,
                                         addItem=(namespace, ""), hb=True)
                            separator()
