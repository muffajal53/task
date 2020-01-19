import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Define rows and cols numbers
nrows, ncols = 8,8

# Make a zero matrix according to rows, cols with interger type value
image = np.zeros((nrows,ncols),dtype=int)

# Replace a value 0 to 1 after skip one zero
image[1::2,::2] = 1
image[::2,1::2] = 1

# Reshape matrix
image = image.reshape((nrows, ncols))

# Give the color for each square
cmap = ListedColormap(['k', 'w'])

# Create an image on plot
plt.matshow(image,cmap=cmap)
# Make label
row_labels = range(nrows)
col_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Change rows and cols label
plt.xticks(range(ncols), col_labels)
plt.yticks(range(nrows), row_labels)

# Show plot and storing image

plt.savefig('chess.png')
plt.show()
