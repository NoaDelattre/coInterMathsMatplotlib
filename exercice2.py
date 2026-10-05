from pylab import*

# Si la forme est bien un carré, l'affichage des deux axes aux tailles différentes donne l'impression de voir un rectangle.

# Arête inférieure du rectangle
x=[3,7]
y=[3,3]

# Arête gauche du rectangle
x2=[3,3]
y2=[3,7]

# Arête droite du rectangle
x3=[7,7]
y3=[3,7]

# Arête supérieure du rectangle
x4=[3,7]
y4=[7,7]

plot(x,y,'-r')
plot(x2,y2,'-r')
plot(x3,y3,'-r')
plot(x4,y4,'-r')

show()
