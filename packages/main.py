from shapes.circle import area as circle_area 
from shapes.circle import perimeter as circle_perimeter
from shapes.rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from shapes.triangle import area as triangle_area, perimeter as triangle_perimeter

radius = 5
length = 4
width = 6
base = 4
height = 3

print(f"Circle area: {round(circle_area(radius),2)}")
print(f"Rectangle area: {rectangle_area(length, width)}")
print(f"Triangle area: {triangle_area(base, height)}")

print(f"Circle perimeter: {round(circle_perimeter(radius),2)}")
print(f"Rectangle area: {rectangle_perimeter(length, width)}")
print(f"Triangle area: {triangle_perimeter(3,4,5)}")