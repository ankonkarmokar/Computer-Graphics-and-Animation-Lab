import matplotlib.pyplot as plt

plt.title("DDA Algorithm : ")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

def dda_algo(x1, y1, x2, y2):

    dx=abs(x2-x1)
    dy=abs(y2-y1)

    steps=max(dx,dy)

    xinc=float(dx/steps)
    yinc=float(dy/steps)

    x=float(x1)
    y=float(y1)

    x_coordinates=[]
    y_coordinates=[]

    for i in range(steps):
        x_coordinates.append(x)
        y_coordinates.append(y)
        print('x=%s , y=%s'%(x,y))
        x+=xinc
        y+=yinc

    plt.plot(x_coordinates, y_coordinates)
    plt.grid(True)
    plt.show()     

#main:
if __name__=="__main__":
    x1 = int(input("Enter the starting point of x: "))
    y1 = int(input("Enter the starting point of y: "))
    x2 = int(input("Enter the ending point of x: "))
    y2 = int(input("Enter the ending point of y: "))

    dda_algo(x1, y1, x2, y2)