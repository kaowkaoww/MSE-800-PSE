#Activity 1
#Write a code to use round , abs and square functions to calculate the area of a rectangle land 
#try to use both Jupyter Notebook and Py

# Inputs
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Make sure values are positive
length = abs(length)
width = abs(width)

# Calculate area
area = length * width

# Round the area
rounded_area = round(area, 2)

# Output
print(f"Length: {length}")
print(f"Width: {width}")
print(f"Area (rounded): {rounded_area}")