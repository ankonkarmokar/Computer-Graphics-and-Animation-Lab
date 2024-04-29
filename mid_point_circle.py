import matplotlib.pyplot as plt

plt.title("Mid Point Circle : ")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

def midpoint(x0, y0, r):

  x = 0
  y = r

  p = 1 - r

  while x <= y:
    plt.plot(x0 + x, y0 + y, marker='o', color='black')
    plt.plot(x0 - x, y0 + y, marker='o', color='black')
    plt.plot(x0 + x, y0 - y, marker='o', color='black')
    plt.plot(x0 - x, y0 - y, marker='o', color='black')
    plt.plot(x0 + y, y0 + x, marker='o', color='black')
    plt.plot(x0 - y, y0 + x, marker='o', color='black')
    plt.plot(x0 + y, y0 - x, marker='o', color='black')
    plt.plot(x0 - y, y0 - x, marker='o', color='black')

    x += 1

    if p < 0:
      p += 2*x + 1
    else:
      y -= 1
      p += 2*(x - y) + 1

  plt.xlim([x0 - r - 1, x0 + r + 1])
  plt.ylim([y0 - r - 1, y0 + r + 1])
  plt.axis('equal')  # Equal aspect ratio ensures a circular shape
  plt.grid(True)
  plt.show()

if __name__=="__main__":
    x0 = int(input("Enter the center point of circle (x): "))
    y0 = int(input("Enter the center point of circle (y): "))
    r = int(input("Enter the radious of circle: "))

    midpoint(x0, y0, r)