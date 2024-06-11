import math
def circumference_and_area_of_a_circle(r):
    return [round( 2 * math.pi * r ,2), round( r * ((math.pi)**2) ,2)]

print(circumference_and_area_of_a_circle(3))
print(circumference_and_area_of_a_circle(2))
print(circumference_and_area_of_a_circle(1))