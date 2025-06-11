#معادله درجه دوم
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
a= int(input("a:"))
b= int(input("b:"))
c= int(input("c:"))
if a==0:
    print("a cant be 0")
else:
    findroots(a,b,c)

#حالت دوم
import cmath  
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
  
d = (b**2) - (4*a*c)  
  
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(sol1,sol2))  