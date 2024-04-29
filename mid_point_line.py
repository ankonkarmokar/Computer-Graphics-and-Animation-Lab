import matplotlib.pyplot as plt
plt.title("Mid Point Line : ")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

def midpoint(x1, y1, x2, y2):
#Step1:
    dx=x2-x1
    dy=y2-y1
#Step2:
#decesion parameter
    d=2*dy-dx
    dd=2*(dy-dx)

    x=x1
    y=y1

    print('x=%s , y=%s'%(x,y))

    xcoordinates=[x]
    ycoordinates=[y]
#Step3:
    while(x<x2):
        x=x+1
        #Case1:
        if(d<0):
            d=d+(2*dy)
        #Case2:
        else:
            y=y+1
            d=d+dd
        xcoordinates.append(x)
        ycoordinates.append(y)
    print('x=%s , y=%s'%(x,y))
    plt.plot(xcoordinates,ycoordinates)
    plt.grid(True)
    plt.show()
#main:
if __name__=="__main__":
    x1 = int(input("Enter the starting point of x: "))
    y1 = int(input("Enter the starting point of y: "))
    x2 = int(input("Enter the end point of x: "))
    y2 = int(input("Enter the end point of y: "))

    midpoint(x1, y1, x2, y2)