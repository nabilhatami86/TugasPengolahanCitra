# Import the Image and ImageFilter classes from the PIL (Python Imaging Library) package.
from PIL import Image, ImageFilter

# Open the image file "st_peter.jpeg" for reading and assign the Image object to the variable 'before'.
before = Image.open("me.jpg")

# Apply a Box Blur filter with a radius of 5 to the image stored in 'before'. The blurred image is assigned to 'after'.
after = before.filter(ImageFilter.BoxBlur(5))

# Save the blurred image to a new file named "out_st_peter.jpeg".
after.save("out_me.jpeg")

# Apply an edge detection filter (FIND_EDGES) to the original image 'before' to highlight its edges. The result is assigned to 'after_edges'.
after_edges = before.filter(ImageFilter.FIND_EDGES)

# Save the edge-detected image to a new file named "out_edges_st_peter.jpeg".
after_edges.save("out_edges_me.jpeg")
