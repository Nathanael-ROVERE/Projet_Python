import sys
import maya.cmds as cmds

# Change the path to your directory
# PATH = "C:\\Users\\macou\\ATI\\python\\Projet_Python"
PATH = "C:\\Users\\macou\\Documents\\maya\\scripts\\Projet_Python"
MODEL_PATH = PATH + "\\models\\"
ICON_PATH = PATH + "\\icons\\"
sys.path.append(PATH + "\\src")

import ui
reload(ui)

window = ui.UI('Generator')

# before = set(cmds.ls(type='transform'))
# after = set(cmds.ls(type='transform'))
# imported = after - before
