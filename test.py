#type: ignore
import package1.module1, package1.module2
from package1.module1 import * # type: ignore
from package1.module2 import *
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
print("The sum of a and b is :", add(a, b))
print("The sub of a and b is :", sub(a, b))
print("The product of a and b is:", mul(a, b))
print("The quotient of a and b is:",div(a, b))
print("The modulus of a and b is:",mod(a, b))
print("The floor division of a and b is:",floor(a, b))