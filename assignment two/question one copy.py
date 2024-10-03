#The volume of a sphere with radius 'r' is (4/3)*pie*r**2
#What is the volume of the sphere with radius 5
#Make sure the program enters the radius from the keyboard
#and provide the answer in dps

#answers
def volume_of_a_sphere():
 
   radius = int(input("Enter the radius"))
   volume =(4/3)* (22/7) * radius**2

   print(f"The volume of the sphere with radius {radius} is {volume:.2f} ")

volume_of_a_sphere()
