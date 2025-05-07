import math
def find_area_of_circle(radius):
    return math.pi * radius ** 2
def find_area_of_rectangle(width, height):
    return width * height
def main():
    shape = int(input("Enter 1 for circle, 2 for rectangle: "))
    if shape == 1:
        radius = int(input("Enter radius: "))
        print(f"The area of the circle is {find_area_of_circle(radius)}")
    elif shape == 2:
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        print(f"The area of the rectangle is {find_area_of_rectangle(width, height)}")
       
if __name__ == "__main__":
    main()