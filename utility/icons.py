import maya.cmds as cmds
 
alphabet= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
icons = [x for x in cmds.resourceManager(nameFilter = "*")]
if cmds.window('mayaIcon', q=1, ex=1):
    cmds.deleteUI('mayaIcon')  
 
cmds.window('mayaIcon', t='Maya Icons', h=500, w=800, s=1)
for b in alphabet:
    cmds.tabLayout(b,p='mayaIcon')
    cmds.gridLayout('%s'%b, p=b, nc=24)
    alpha = b[0]
    for x in icons:
        if x.startswith(alpha):
            cmds.iconTextButton(style='iconOnly', image1=x ,h=30, w=30, ann=x)
cmds.showWindow()