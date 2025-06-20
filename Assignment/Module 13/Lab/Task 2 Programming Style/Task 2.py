# Calculate the area of a rectangle  <--- comments

def calculate_area(length, width):
    """Return the area of a rectangle."""    # <--- comments
    area = length * width        #<---  indentation  (means 4-space indentation)
    return area

# Set dimensions
length = 5        #<-- variable (length)
width = 3          #<-- variable (width)

# Get area
area = calculate_area(length, width)

# Show result
print("Area of rectangle:", area)
