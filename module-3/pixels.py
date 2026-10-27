# pixels_starter.py -- an image is an array (Pod 5). Copy this file to pixels.py and work on the copy.
# Run from the repository folder:  python module-3/pixels.py
import numpy as np
from matplotlib.pyplot import imread, imsave

I = imread("clean_io_small.png")     # rows, columns, 3 colour channels; values 0.0 to 1.0
print(I.size)
J = I.copy()
J[20:40, 20:40, :] = 1
J[356, :, :] = 0
imsave("pixels_out.png", J)
H = I.copy()
H[:10, : , : ] = 1
H[:, :10, : ] = 1
H[698:, :, : ] = 1
H[:, 684:, : ] = 1
imsave("creative.png", H)
F = H.copy()
F[:, :, 2] = 1 - F[:, :, 0]


imsave("creative_2.png", F)
if __name__ == "__main__":
    print("shape:", I.shape)
