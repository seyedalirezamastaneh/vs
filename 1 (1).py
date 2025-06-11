
import math
def findroots(a,b,c):
    delta = (b**2)-(4*a*c)
    sqrt_delta = math.sqrt(abs(delta))

    if delta > 0:
        print("roots are real and diffrent")
        print((-b+sqrt_delta)/(2*a))
        print((-b-sqrt_delta)/(2*a))
    elif delta == 0:
        print("roots are same but +-")
        print(-b/(2*a),"+i",sqrt_delta)
        print(-b/(2*a),"-i",sqrt_delta)
    else:
        print("roots are complex")
        print(- b / (2 * a), " + i", sqrt_delta)  
        print(- b / (2 * a), " - i", sqrt_delta)  
a=5
b=12
c=8
if a==0:
    print("a cant be 0")
else:
    findroots(a,b,c)

