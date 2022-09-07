import math
# a^2+b+c=0
print("This is program that finds quardatic eqasion intercepts")
a = int(input("Please enter your a="))
b = int(input("Please enter your b="))
c = int(input("Please enter your c="))

discriminant = b**2-(4*a*c)
print("Your a is", a)
print("Your b is", b)
print("Your c is", c)
print("Discriminant is", discriminant)

if discriminant <0:
    print ("No intercepts")

if discriminant ==0:
    x=(-b+0)/2*a
    print("1 intercept", x)
if discriminant >0:
    x1=(-b+math.sqrt(discriminant))/2*a
    x2=(-b-math.sqrt(discriminant))/2*a
    print("1 intercept", x1)
    print("2 intercept", x2)
