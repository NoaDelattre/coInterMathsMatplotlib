from pylab import*

# Fonction x² affichée grâce à la bibilothèque matplotlib
def f(x):
    y=x**2
    return y

for i in range(-10,10):
    x=i
    plot(x,f(x),'*')
show()