import functools as func
from pymel.core import *
import maya.cmds as cmds
import sys
import ui
reload(ui)

window = ui.UI('Generator')
cmds.file(f=True, new=True)


# Change the path to your directory
# PATH = "C:\\Users\\macou\\ATI\\python\\Projet_Python"
# PATH = "C:\\Users\\macou\\Documents\\maya\\scripts\\Projet_Python"
# MODEL_PATH = PATH + "\\models\\"
# ICON_PATH = PATH + "\\icons\\"
# sys.path.append(PATH + "\\src")


# before = set(cmds.ls(type='transform'))
# cmds.file(MODEL_PATH + "\\COULEURS_OBJETS.mb", reference=True, namespace="objects")
# after = set(cmds.ls(type='transform'))
# imported = after - before
# cmds.hide(imported)
