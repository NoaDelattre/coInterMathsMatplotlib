from pylab import* 
listex = []
listey = []

for i in range (5,15):
    x1 = i
    y = 3
    listex.append(x1)
    listey.append(y)
    plot(x1,y,'*b')
show()