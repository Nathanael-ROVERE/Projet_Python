import maya.cmds as cmds

import mtoa.utils as mutils; mutils.createLocator("aiSkyDomeLight", asLight=True)
#set up des light
keyLight = cmds.shadingNode('areaLight', asLight = True, name = 'keyLight_LGT')
fillLight = cmds.shadingNode('areaLight', asLight = True, name = 'fillLight_LGT')
rimLight = cmds.shadingNode('areaLight', asLight = True, name = 'rimLight_LGT')


cmds.xform(keyLight, absolute = True, translation = [-21.706,5.408,-23.079], rotation = [0, -128.233, 0], scale = [8, 8, 8])
cmds.xform(fillLight, absolute = True, translation = [14.286,2.970,-0.386], rotation = [0, 93.223, 0], scale = [8, 8, 8])
cmds.xform(rimLight, absolute = True, translation = [0,7.854,10.664], rotation = [-40.253, 00, 00], scale = [8, 8, 8])


	
cmds.setAttr("keyLight_LGT.intensity",500)
cmds.setAttr ("fillLight_LGT.intensity", 500)
cmds.setAttr ("rimLight_LGT.intensity", 500)

cmds.setAttr ("keyLight_LGT.decayRate", 2)
cmds.setAttr ("rimLight_LGT.decayRate", 2)
cmds.setAttr ("fillLight_LGT.decayRate", 2)
cmds.setAttr ("keyLight_LGT.aiExposure", 1.184211)
cmds.setAttr ("rimLight_LGT.aiExposure", 1.184211)
cmds.setAttr ("fillLight_LGT.aiExposure", 1.184211)
cmds.setAttr ("keyLight_LGT.aiSamples", 8)
cmds.setAttr ("rimLight_LGT.aiSamples", 8)
cmds.setAttr ("fillLight_LGT.aiSamples", 8)
	

# SKYDOME JOUR
cmds.setAttr ("aiSkyDomeLightShape1.aiColorTemperature", 4652)
cmds.setAttr ("aiSkyDomeLightShape1.intensity", 0.454545)
cmds.setAttr ("aiSkyDomeLightShape1.aiUseColorTemperature", 1)
cmds.setAttr ("aiSkyDomeLightShape1.resolution", 2000)
cmds.setAttr ("aiSkyDomeLightShape1.aiSamples", 4)



#NUIT
cmds.setAttr ("aiSkyDomeLightShape1.aiColorTemperature", 8565)
cmds.setAttr ("aiSkyDomeLightShape1.intensity", 0.005)
cmds.setAttr ("aiSkyDomeLightShape1.aiUseColorTemperature", 1)
cmds.setAttr ("aiSkyDomeLightShape1.resolution", 2000)
cmds.setAttr ("aiSkyDomeLightShape1.aiSamples", 4)
cmds.setAttr ("aiSkyDomeLightShape1.color",  0.01, 0.01, 0.01, type = 'double3')