import sys
#Change the path to your directory
PATH = "C:\Users\macou\ATI\python\Projet_Python\src"
sys.path.append(PATH)

import ui
reload(ui)

window = ui.UI('Diorama Generator')