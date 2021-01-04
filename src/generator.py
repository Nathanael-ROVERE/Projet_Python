from pymel.core import *
import maya.cmds as cmds
import random
from utils import Switch
import mtoa.utils as mutils


class Generator:
    def __init__(self):
        self.environment = {}
        self.environment['time'] = 'day'
        self.environment['season'] = 'spring'
        self.base = {}
        self.base['shape'] = "squarish"
        self.base['size'] = 10
        self.base['height'] = 2
        self.elements = {}
        self.camera = {}
        self.camera['enabled'] = True
        self.camera['focal'] = 50
        self.elements = []
        self.generated = ''

    def updateValues(self, UI):
        self.elements = []
        self.environment['time'] = iconTextRadioCollection(
            UI.environment['time'], q=True, sl=True)
        self.environment['season'] = iconTextRadioCollection(
            UI.environment['season'], q=True, sl=True)
        self.base['shape'] = iconTextRadioCollection(
            UI.base['shape'], q=True, sl=True)
        self.base['size'] = intSliderGrp(
            UI.base['size'], q=True, v=True)
        self.base['height'] = intSliderGrp(
            UI.base['height'], q=True, v=True)
        self.camera['focal'] = optionMenuGrp(
            UI.camera['focal'], q=True, v=True)
        elements = treeView(UI.treeView, q=True, ch=None)
        for el in elements:
            if treeView(UI.treeView, q=True, itemParent=el) != '':
                self.elements.append(el)
    def generate(self, UI):
        self.generated = cmds.group(n="Generated_Island_#", em=True)

        self.updateValues(UI)
        self.buildBase()
        self.buildLights()
        self.buildCamera()
        self.buildElements()

    def regenerate(self, UI):
        if self.generated != '':
            cmds.delete(self.generated)
        self.generate(UI)

    def buildBase(self):

        grp = cmds.group(name="Floor", em=True)

        base = cmds.polyCube(width=self.base['size'], height=self.base['height'],
                      depth=self.base['size'], sx=10, sy=1, sz=10, name="Island_Floor_#")
        cmds.rotate('180deg', 0, 0, r=True)

        shd = cmds.shadingNode('lambert', asShader=True, n='%s_lmb' % base)
        sg = cmds.sets(n='%s_sg' % base, renderable=True,
                       noSurfaceShader=True, empty=True)

        with Switch(self.environment['season']) as case:
            if case('spring'):
                cmds.setAttr(shd+".color", 0.6,
                             1, 0.541, type="double3")
            elif case('summer'):
                cmds.setAttr(shd+".color", 1,
                             0.835, 0.541, type="double3")
            elif case('automn'):
                cmds.setAttr(shd+".color", 0.996,
                             0.407, 0.282, type="double3")
            elif case('winter'):
                cmds.setAttr(shd+".color", 0.560,
                             0.941, 1, type="double3")
        cmds.connectAttr('%s.outColor' % shd, '%s.surfaceShader' % sg, f=True)
        cmds.sets(base, e=True, fe=sg)

        self.bbox = cmds.exactWorldBoundingBox(base)
        cmds.parent(base, grp)

        with Switch(self.base['shape']) as case:
            if case('circular'):
                CreateCircularFloor(base[0])
            elif case('squarish'):
                CreateSquareFloor(base[0])
            elif case('polygonal'):
                CreateTriangleFloor(base[0])
                
            else:
                print('default')
        cmds.parent(grp, self.generated)

    def buildCamera(self):
        pos = self.base['size']
        camera = cmds.camera(focalLength=float(self.camera['focal']), 
                                rotation=(-35, 45, 0),
                                position=(pos, pos, pos),
                                n="Camera_Island_#")
        cmds.parent(camera, self.generated)

    def buildLights(self):
        skydome = mutils.createLocator("aiSkyDomeLight", asLight=True)
        if self.environment['time'] == 'day':
            cmds.setAttr(skydome[0] + ".aiColorTemperature", 4652)
            cmds.setAttr(skydome[0] + ".intensity", 0.454545)
            cmds.setAttr(skydome[0] + ".aiUseColorTemperature", 1)
            cmds.setAttr(skydome[0] + ".resolution", 2000)
            cmds.setAttr(skydome[0] + ".aiSamples", 4)
        elif self.environment['time'] == 'night':
            cmds.setAttr(skydome[0] + ".aiColorTemperature", 8565)
            cmds.setAttr(skydome[0] + ".intensity", 0.005)
            cmds.setAttr(skydome[0] + ".aiUseColorTemperature", 1)
            cmds.setAttr(skydome[0] + ".resolution", 2000)
            cmds.setAttr(skydome[0] + ".aiSamples", 4)
            cmds.setAttr(skydome[0] + ".color",  0.01, 0.01, 0.01, type='double3')
        cmds.parent(skydome, self.generated)

    def buildElements(self):
        elements = cmds.group(n="Elements", em=True)
        for i in range(len(self.elements)):
            instance = cmds.instance(self.elements[i], n=self.elements[i]+'_#')
            cmds.showHidden(instance)
            #Selecting a random point between minX and maxX
            xRand = random.uniform(self.bbox[0], self.bbox[3])
            #Selecting a random point between minY and maxY
            # yRand = random.uniform(self.bbox[1], self.bbox[4])
            yRand = self.bbox[4]
            #Selecting a random point between minZ and maxZ
            zRand = random.uniform(self.bbox[2], self.bbox[5])

       	    cmds.move(xRand, yRand, zRand, instance, ws=True, a=True, rpr=True)
            cmds.parent(instance, elements)
        cmds.parent(elements, self.generated);




def CreateCircularFloor(name):
    #boucle pour extruder les vertex les plus bas
    for i in range(11, 132, 3):
        if((12 < i < 43) or (99 < i < 132) or (i % 11 == 0) or (i % 11 == 1) or (i % 11 == 2) or (i % 11 == 8) or (i % 11 == 9) or (i % 11 == 10)):
            rand_nb = random.uniform(3.0, 8.0)
            cmds.polyMoveVertex(name + '.vtx['+str(i)+']', ty=-rand_nb)
        else:
            rand_nb = random.uniform(6.0, 11.0)
            cmds.polyMoveVertex(name + '.vtx['+str(i)+']', ty=-rand_nb)
    #boucle pour extruder les vertex qui restaient au sol
    for i in range(12, 130, 2):
        rand_nb = random.uniform(0.5, 1.5)
        cmds.polyMoveVertex(name + '.vtx['+str(i)+']', ty=-rand_nb)

    cmds.polySmooth(name + '.vtx[11:131]', dv=3, kb=False)


def CreateTriangleFloor(name):
    for i in range (11,132,2):
        if( (11 < i < 43) or (99 < i < 132) or (i%11 == 0) or (i%11 == 1) or (i%11 == 2) or (i%11 == 8) or (i%11 == 9) or (i%11 == 10) ):
            rand_nb = random.uniform(1.0, 4.0);
            cmds.polyMoveVertex(
                name + '.vtx['+str(i)+']', ty=-rand_nb)
        else:
            rand_nb = random.uniform(3.0, 8.0);
            cmds.polyMoveVertex(
                name + '.vtx['+str(i)+']', ty=-rand_nb)
    
    for i in range (12,130,2):
        rand_nb = random.uniform(0.0, 1.0);
        cmds.polyMoveVertex(name + '.vtx['+str(i)+']', ty=-rand_nb)

def CreateSquareFloor(name, n=10):
    for i in range(n, n*n+n):
        if((i < n*(1+n/3)) or (i >= n*(n+1-n/3)) or n*(1+n/3) <= i < (n*(1+n/3)+(n/3)) or n*(2+n/3) <= i < (n*(2+n/3)+(n/3)) or n*(3+n/3) <= i < (n*(3+n/3)+(n/3)) or n*(4+n/3) <= i < (n*(4+n/3)+(n/3)) or (n*(1+n/3)+2*n/3) < i < (n*(1+n/3)+n) or (n*(2+n/3)+2*n/3) < i < (n*(2+n/3)+n) or (n*(3+n/3)+2*n/3) < i < (n*(3+n/3)+n) or (n*(4+n/3)+2*n/3) < i < (n*(4+n/3)+n)):
            # hauteur d'extrude des faces aux contours
            rand_nb = random.uniform(1.0, 4.0)
            cmds.polyExtrudeFacet(
                name + '.f['+str(i)+']', kft=False, ltz=rand_nb, ls=(1, 1, 0))
        else:
            # hauteur d'extrude des faces centrales
            rand_nb = random.uniform(3.0, 8.0)
            cmds.polyExtrudeFacet(
                name + '.f['+str(i)+']', kft=False, ltz=rand_nb, ls=(1, 1, 0))
