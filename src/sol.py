import maya.cmds as cmds
import random
cmds.file(f=True, new=True) #permet de vider la scène à chaque exécution

#variables de generation du sol
largeur_ile = 10;
longueur_ile = 10;
hauteur_ile = 0.01;
n = 10; #nombre de subdiviions

groupe = cmds.group(name="Ile",em=True) 

def creer_sol_carre():   
    #creation du sol
    ile_carre = cmds.polyCube(width=largeur_ile, height=hauteur_ile, depth=longueur_ile, sx=n , sy=1, sz=n , name="sol_ile");
    #on oriente le sol vers le bas
    cmds.rotate('180deg', 0, 0, r=True);
    cmds.parent(ile_carre, groupe);
    
    for i in range (n, n*n+n):
        if( (i<n*(1+n/3)) or (i>=n*(n+1-n/3)) or n*(1+n/3) <= i < (n*(1+n/3)+(n/3)) or n*(2+n/3) <= i < (n*(2+n/3)+(n/3)) or n*(3+n/3) <= i < (n*(3+n/3)+(n/3)) or n*(4+n/3) <= i < (n*(4+n/3)+(n/3)) or (n*(1+n/3)+2*n/3) < i < (n*(1+n/3)+n) or (n*(2+n/3)+2*n/3) < i < (n*(2+n/3)+n) or (n*(3+n/3)+2*n/3) < i < (n*(3+n/3)+n) or (n*(4+n/3)+2*n/3) < i < (n*(4+n/3)+n) ):
            # hauteur d'extrude des faces aux contours
            rand_nb = random.uniform(1.0, 4.0);
            cmds.polyExtrudeFacet( 'sol_ile.f['+str(i)+']', kft=False, ltz=rand_nb, ls=(1, 1, 0));
        else:
            # hauteur d'extrude des faces centrales
            rand_nb = random.uniform(3.0, 8.0);
            cmds.polyExtrudeFacet( 'sol_ile.f['+str(i)+']', kft=False, ltz=rand_nb, ls=(1, 1, 0));

def creer_sol_triangle():
    #creation du sol
    cmds.polyCube(width=largeur_ile, height=hauteur_ile, depth=longueur_ile, sx=n , sy=1, sz=n , name="sol_ile");
    #on oriente le sol vers le bas
    ile_triangle = cmds.rotate('180deg', 0, 0, r=True);
    cmds.parent(ile_triangle, groupe);
    
    for i in range (11,132,2):
        if( (11 < i < 43) or (99 < i < 132) or (i%11 == 0) or (i%11 == 1) or (i%11 == 2) or (i%11 == 8) or (i%11 == 9) or (i%11 == 10) ):
            rand_nb = random.uniform(1.0, 4.0);
            cmds.polyMoveVertex( 'sol_ile.vtx['+str(i)+']', ty=-rand_nb );
        else:
            rand_nb = random.uniform(3.0, 8.0);
            cmds.polyMoveVertex( 'sol_ile.vtx['+str(i)+']', ty=-rand_nb );
    
    for i in range (12,130,2):
        rand_nb = random.uniform(0.0, 1.0);
        cmds.polyMoveVertex( 'sol_ile.vtx['+str(i)+']', ty=-rand_nb );

def creer_sol_rond():    
    #creation du sol
    ile_ronde = cmds.polyCube(width=largeur_ile, height=hauteur_ile, depth=longueur_ile, sx=n , sy=1, sz=n , name="sol_ile");
    #on oriente le sol vers le bas
    cmds.rotate('180deg', 0, 0, r=True);
    cmds.parent(ile_ronde, groupe);
    
    #boucle pour extruder les vertex les plus bas
    for i in range (11,132,3):
        if( (12 < i < 43) or (99 < i < 132) or (i%11 == 0) or (i%11 == 1) or (i%11 == 2) or (i%11 == 8) or (i%11 == 9) or (i%11 == 10) ):
            rand_nb = random.uniform(3.0, 8.0);
            cmds.polyMoveVertex( 'sol_ile.vtx['+str(i)+']', ty=-rand_nb );
        else:
            rand_nb = random.uniform(6.0, 11.0);
            cmds.polyMoveVertex( 'sol_ile.vtx['+str(i)+']', ty=-rand_nb );
    #boucle pour extruder les vertex qui restaient au sol
    for i in range (12,130,2):
        rand_nb = random.uniform(0.5, 1.5);
        cmds.polyMoveVertex( 'sol_ile.vtx['+str(i)+']', ty=-rand_nb );    
    
    cmds.polySmooth( 'sol_ile.vtx[11:131]', dv=3, kb=False )


creer_sol_rond()

#sol = cmds.polyCube(width=largeur_ile, height=hauteur_ile, depth=longueur_ile, sx=n , sy=1, sz=n , name="plane_ile");
sol = cmds.polyPlane(name="sol")
cmds.scale(10,10,10)
cmds.parent(sol, groupe);

def placement(nombre_max = 8, type = "carre"):
    tmp = nombre_max;
    for i in range(11,110):
        if (i%11 != 0) and (i%11 != 10): #on exclue les rebords de l'île
            p=cmds.xform("sol.vtx["+str(i)+"]", q=True, translation=True, worldSpace=True)
            rand = random.randrange(0,98) # random parmi les cases qu'on veut occuper
            if(rand<nombre_max) and (tmp!=0):
                if(type == "carre"):
                    cmds.polyCube(w=0.5, d=0.5, h=0.5);
                    cmds.move(p[0], p[1], p[2]);
                    tmp = tmp - 1;
                if(type == "rond"):
                    cmds.polySphere(r=0.25);
                    cmds.move(p[0], p[1], p[2]);
                    tmp = tmp - 1;
                if(type == "triangle"):
                    cmds.polyCone(r=0.25, h=2);
                    cmds.move(p[0], p[1], p[2]);
                    tmp = tmp - 1;

placement(5, "triangle");

#def placement_arbres(type, nombre):
    
    



