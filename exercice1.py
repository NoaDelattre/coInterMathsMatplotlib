from pylab import*
x=[2,5,8]           # Définit les coordonnées des sommets du triangle par rapport à l'axe des abscisses
y=[2,8,2]           # Définit les coordonnées des sommets du triangle par rapport à l'axe des ordonnées
x2=[2,8]            # Définit les coordonnées de la base du triangle par rapport à l'axe des abscisses
y2=[2,2]            # Définit les coordonnées de la base du triangle par rapport à l'axe des ordonnées
plot(x,y,'-r')      # Trace les deux arêtes supérieures du triangle
plot(x2,y2,'-r')    # Trace la base du triangle
show()              # Affiche le triangle sur un onglet interactif