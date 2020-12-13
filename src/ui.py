import maya.cmds as cmds
from pymel.core import *
import generator as gen
import utils
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

        #Layouts
        self.template.define(frameLayout, collapsable=True,
                             backgroundColor=[0.2, 0.2, 0.2])
        self.template.define(rowColumnLayout, nc=1, co=(
            1, "both", self.spacing), adj=1)

        #elements
        self.template.define(iconTextRadioButton,
                             mw=self.spacing, mh=self.spacing)
        self.template.define(intSliderGrp, cal=[1, "left"])

        #style
        self.template.define(separator, h=self.spacing, style="none")

    @staticmethod
    def toggle(controls):
        for control in controls.values():
            control.type()
            isFloatGroup = cmds.floatSliderGrp(control, q=True, ex=True)
            isIntGroup = cmds.intSliderGrp(control, q=True, ex=True)
            isRadioButtonGrp = cmds.radioButtonGrp(control, q=True, ex=True)
            if (isFloatGroup):
                value = cmds.floatSliderGrp(control, q=True, en=True)
                cmds.floatSliderGrp(control, e=True, en=not value)
            elif (isIntGroup):
                value = cmds.intSliderGrp(control, q=True, en=True)
                cmds.intSliderGrp(control, e=True, en=not value)
            elif(isRadioButtonGrp):
                value = cmds.radioButtonGrp(control, q=True, en=True)
                cmds.radioButtonGrp(control, e=True, en=not value)

    def frameEnvironment(self):
        self.environment = {}
        with frameLayout("Environment"):
            with rowColumnLayout():
                with rowLayout(nc=4, cw=[1, self.widthLabel]):
                    text(l='Time', al="left")
                    self.environment['time'] = iconTextRadioCollection(
                        'time')
                    iconTextRadioButton('day', sl=(False, True)[self.environment['time'] == "day"],
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
                                        [self.environment['season']
                                            == "spring"],
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
                                        l='Circular', i1='polyCylinder.png', st='iconAndTextVertical')
                    iconTextRadioButton('squarish',
                                        sl=(False, True)[
                                            self.generator.base['shape'] == "squarish"],
                                        l='Squarish', i1='polyCube.png', st='iconAndTextVertical')
                    iconTextRadioButton('polygonal',
                                        sl=(False, True)[
                                            self.generator.base['shape'] == "polygonal"],
                                        l='Polygonal', i1='polyPlatonic.png', st='iconAndTextVertical')
                separator()
                self.base['size'] = intSliderGrp(
                    f=True, l='Size', cw3=[self.widthLabel, 50, 90])
                separator()

    def frameCamera(self):
        self.camera = {}
        with frameLayout("Camera"):
            with rowColumnLayout():
                with columnLayout(cat=['both', 0], rs=self.spacing, adj=1):
                    self.camera['enabled'] = symbolCheckBox(image='out_camera.png',
                                                            v=self.generator.camera['enabled'],
                                                            onc=Callback(
                                                                self.toggle, self.camera),
                                                            ofc=Callback(self.toggle, self.camera))
                    self.camera['focal'] = radioButtonGrp(l="Focal", nrb=4, cw=[1, 50],
                                                          labelArray4=[
                                                              '28mm', '50mm', '120mm', '200mm'],
                                                          cal=[1, "left"],
                                                          cw5=[self.widthLabel, 60, 60, 60, 60])
                    print(self.camera['focal'].type())

    def createItemsList(self):
        iconPath = utils.icon_path() + "\\types\\"
        filesList = getFileList(fld=utils.model_path(), fs="*.mb")

        for file in filesList:
            namespace = file.replace(".mb", "")
            icon = iconPath + namespace + ".png"
            before = set(cmds.ls(type='transform'))
            print(icon)
            cmds.file(utils.model_path() + file,
                      reference=True, namespace=namespace)
            after = set(cmds.ls(type='transform'))
            imported = after - before
            for obj in imported:
                treeLister(self.treeLister, e=True, add=(
                    namespace + "/" + obj.replace(namespace + ":", ""), icon, "cmds.polySphere()"))

    def createWindow(self, title):
        with window(title=title) as self.win:
            with self.template:
                with paneLayout(cn="vertical2"):
                    with rowColumnLayout():
                        separator()
                        self.frameEnvironment()
                        self.frameBase()
                        self.frameCamera()
                        separator()
                        button(label="Generate", c=Callback(
                            self.generator.generate, self))
                        separator()
                    with rowColumnLayout():
                        separator()
                        # with rowLayout(nc=2, cl2=["left", "left"]):
                            # text('search')
                            # text('icon size')
                        self.treeLister = treeLister(h=400)
                        self.createItemsList()
                        separator()
