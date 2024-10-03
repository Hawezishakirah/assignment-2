#Create a program to calculate, calculate the area of a triangle(1/2*base*height)
#Base and height should be entered using the keyword
#answers
def calculate_area(base, height):
    area = 0.5 * base * height
    return area
#base and height
base =int(input("Enter the base of the triangle:"))
height = int(input("Enter the height of the triangle:"))
#area calculations
area = calculate_area(base,height)

print(f"The area of the triangle with base {base} and height {height} is: {area:2f}")