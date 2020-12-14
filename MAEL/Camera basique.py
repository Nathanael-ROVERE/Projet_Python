import maya.cmds as cmds
cmds.file(f=True, new=True)

cmds.polyCube(n="cube")
cmds.camera(focalLength=120,rotation = (-4,0,0),position = (0,1,11),n="cam_") # focal 120
cmds.camera(focalLength=50,rotation = (-4,-66,0),position = (-8.633,1,4.341),n="cam-")# focal 50 bref voila 