from formuls import *
import math
#print(recta(3, 4))

# print(square(4))

# print(circle(14))

S_square = square(4)
S_circle = circle(14)

result = S_circle - S_square

if result > 0:
    print('circle is bigger than a square')
elif result < 0:
    print("square is bigger than a circle")
else:
    print ("circle is equal to square")