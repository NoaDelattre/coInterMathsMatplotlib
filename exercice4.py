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

for i in range(5,15):
    for j in range(3,6):
        x1 = i
        y = j+2
        listex.append(x1)
        listey.append(y)
        plot(x1,y,'*r')
        j == j+2
show()

for j in range(3,6):
    for i in range(5,15):
        x1 = i
        y = j
        listex.append(x1)
        listey.append(y)
        plot(x1,y,'*g')
    j == j+2
show()
